<script setup>
import { ref, onMounted } from 'vue'
import { useDark, useToggle } from '@vueuse/core'
import { RouterLink, RouterView } from 'vue-router'
import { msalInstance, loginRequest } from './authConfig'
import md5 from 'md5'

const isDark = useDark()
const toggleDark = useToggle(isDark)

// Set to false when you are ready to launch!
const isUnderConstruction = ref(false)
const showSignIn = ref(false)
const currentUser = ref(null)
const isMobileMenuOpen = ref(false)

// Close mobile menu when route changes
import { watch } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
watch(() => route.path, () => { isMobileMenuOpen.value = false })

const azureSignIn = async () => {
  showSignIn.value = false;
  try {
    // Switch to redirect flow for better single-window context and reliability
    await msalInstance.loginRedirect({ ...loginRequest, prompt: 'select_account' });
  } catch (error) {
    console.error("Login failed", error);
  }
}

const handleSignOut = async () => {
  showSignIn.value = false;
  try {
    if (currentUser.value) {
      await msalInstance.logoutRedirect({
        account: currentUser.value,
        postLogoutRedirectUri: window.location.origin
      });
    }
  } catch (error) {
     console.error("Logout failed", error);
     currentUser.value = null;
  }
}

// Helper to fetch user's Azure profile picture
const fetchAzureProfilePicture = async (accessToken, account) => {
  // First, check if the ID token already contains the picture URL
  if (account?.idTokenClaims?.picture) {
    return account.idTokenClaims.picture;
  }

  try {
    const response = await fetch("https://graph.microsoft.com/v1.0/me/photo/$value", {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });

    if (response.ok) {
      const blob = await response.blob();
      return await new Promise((resolve) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result);
        reader.readAsDataURL(blob);
      });
    }
  } catch (err) {
    console.warn("Could not fetch Azure profile picture", err);
  }

  // Final fallback to uniquely generated Gravatar
  if (account?.username) {
    const hash = md5(account.username.toLowerCase().trim());
    return `https://www.gravatar.com/avatar/${hash}?d=identicon`;
  }

  return null;
}

onMounted(async () => {
  try {
    // Must handle the redirect promise when the page reloads after login
    const response = await msalInstance.handleRedirectPromise();
    if (response) {
      currentUser.value = { ...response.account, name: response.account.name, photoURL: await fetchAzureProfilePicture(response.accessToken, response.account) };
      return;
    }
    
    // Check if a user is already logged in securely
    const accounts = msalInstance.getAllAccounts();
    if (accounts.length > 0) {
      try {
        const tokenResponse = await msalInstance.acquireTokenSilent({
          ...loginRequest,
          account: accounts[0]
        });
        currentUser.value = { 
          ...accounts[0], 
          name: accounts[0].name, 
          photoURL: await fetchAzureProfilePicture(tokenResponse.accessToken, accounts[0]) 
        };
      } catch (err) {
        currentUser.value = { ...accounts[0], name: accounts[0].name };
      }
    }
  } catch (error) {
    console.error("Authentication redirect error:", error);
  }
})


//const response = await fetch('http://localhost:8787/api/articles')
//const articles = await response.json()
</script>

<template>
  <!-- Under Construction Screen -->
  <div v-if="isUnderConstruction" class="flex min-h-screen w-full items-center justify-center bg-white dark:bg-dark-bg p-6 text-slate-800 dark:text-slate-200">
    <div class="text-center max-w-2xl flex flex-col items-center">
      <img src="./assets/logos/newlogo.png" alt="Today's Software Developer Logo" class="mx-auto mb-8 h-40 w-auto mix-blend-multiply dark:invert dark:mix-blend-screen" />
      <h1 class="mb-4 text-4xl font-bold tracking-tight md:text-5xl">Site Under Construction</h1>
      <p class="mb-8 text-lg text-slate-600 dark:text-slate-400">
        We are building the definitive home for <strong>Today's Software Developer</strong>. 
        Stay tuned for the book, articles, and companion resources.
      </p>
      <a href="https://www.youtube.com/@TodaysSoftwareDev" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 rounded-lg bg-red-600 px-6 py-3 font-bold text-white shadow-sm transition hover:bg-red-700">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 fill-current" viewBox="0 0 24 24">
          <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z" />
        </svg>
        Subscribe on YouTube
      </a>
    </div>
  </div>

  <div v-else class="flex flex-col md:flex-row min-h-screen text-slate-800 dark:text-slate-200 bg-white dark:bg-dark-bg w-full">
    <!-- Fixed Side Navigation -->
    
    <!-- Mobile Menu Backdrop -->
    <div v-if="isMobileMenuOpen" @click="isMobileMenuOpen = false" class="fixed inset-0 bg-slate-900/50 z-40 md:hidden backdrop-blur-sm transition-opacity"></div>

    <!-- Fixed Side Navigation -->
    <aside :class="['flex fixed top-0 left-0 h-screen w-72 border-r border-slate-200/70 bg-slate-50 dark:border-slate-700/80 dark:bg-slate-900 flex-col pt-8 pb-6 px-6 overflow-y-auto z-50 transition-transform duration-300 ease-in-out md:translate-x-0', isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full']">

      <!-- Logo -->
      <div class="mb-10 flex justify-center mt-4">
        <RouterLink to="/" class="transition hover:opacity-80">
          <img src="./assets/logos/newlogo.png" alt="Today's Software Developer Logo" class="h-24 w-auto mix-blend-multiply dark:invert dark:mix-blend-screen">
        </RouterLink>
      </div>

      <!-- Navigation Links -->
      <nav class="flex flex-col gap-1.5 text-base font-medium text-slate-600 dark:text-slate-400">
        <RouterLink to="/#about" class="px-3 py-1 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary">About the Book</RouterLink>
        <RouterLink to="/articles" class="px-3 py-1 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary">Articles</RouterLink>
        <RouterLink v-if="currentUser && (currentUser.username === 'jwlankford@gmail.com' || currentUser.email === 'jwlankford@gmail.com')" to="/admin" class="px-3 py-1 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary font-bold text-emerald-600 dark:text-emerald-500">Admin Portal</RouterLink>
      </nav>

      <!-- Social Buttons & Resources -->
      <div class="mt-6 mb-2">
        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 dark:text-slate-500 mb-3">MEDIA</h3>
        <ul class="space-y-1.5 text-xs font-medium text-slate-600 dark:text-slate-400">
          <li>
            <a href="#" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
              Download Setup Guide
            </a>
          </li>
          <li>
            <a href="https://github.com/jwlankford/todayssoftwaredeveloper" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>
              Source Code Repository
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" /></svg>
              Podcast
            </a>
          </li>
          <li>
            <a href="https://www.youtube.com/@TodaysSoftwareDev" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              YouTube Channel
            </a>
          </li>
        </ul>

        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 dark:text-slate-500 mb-3 mt-4">REPOS and RESUME</h3>
        <div class="flex gap-2 mb-4">
          <a href="https://github.com/jwlankford" target="_blank" rel="noopener noreferrer" class="group relative flex items-center justify-center w-[35px] h-[35px] bg-slate-800 hover:bg-slate-900 dark:bg-slate-700 dark:hover:bg-slate-600 text-white rounded-md shadow-sm transition overflow-hidden shrink-0">
            <svg class="transition-opacity duration-300 group-hover:opacity-0 h-[16px] w-[16px] fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            <span class="absolute inset-0 flex items-center justify-center bg-black/70 opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-[8px] font-bold text-center leading-tight px-1 z-10">GitHub</span>
          </a>
          <a href="https://www.gitlab.com/jwlankford" target="_blank" rel="noopener noreferrer" class="group relative flex items-center justify-center w-[35px] h-[35px] bg-[#FC6D26] hover:bg-[#E24329] text-white rounded-md shadow-sm transition overflow-hidden shrink-0">
            <svg class="transition-opacity duration-300 group-hover:opacity-0 h-[16px] w-[16px] fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M23.955 13.587l-2.242-6.903c-.201-.617-1.084-.617-1.285 0l-1.465 4.512h-4.3l-1.465-4.512c-.201-.617-1.084-.617-1.285 0L9.67 13.587l-3.344-10.297c-.201-.617-1.084-.617-1.285 0L2.8 10.192H.316c-.452 0-.678.547-.358.866l11.455 11.411a.488.488 0 0 0 .69 0L23.559 11.06c.32-.32.094-.867-.358-.867h-2.484l2.238 6.892z" fill="#E24329"/><path d="M12 22.47L2.8 13.587H15.17l-3.17 8.883z" fill="#FC6D26"/><path d="M2.8 13.587L.316 11.06c-.32-.32-.094-.866.358-.866h2.483l5.042 10.294-5.4-6.892z" fill="#FCA326"/><path d="M12 22.47l9.2-8.883H8.83l3.17 8.883z" fill="#E24329"/><path d="M21.2 13.587l2.484-2.527c.32-.32.094-.866-.358-.866h-2.483L15.8 20.488l5.4-6.901z" fill="#FCA326"/>
            </svg>
            <span class="absolute inset-0 flex items-center justify-center bg-black/70 opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-[8px] font-bold text-center leading-tight px-1 z-10">GitLab</span>
          </a>
          <a href="https://www.linkedin.com/in/jwlankford" target="_blank" rel="noopener noreferrer" class="group relative flex items-center justify-center w-[35px] h-[35px] bg-[#0a66c2] hover:bg-[#004182] text-white rounded-md shadow-sm transition overflow-hidden shrink-0">
            <svg class="transition-opacity duration-300 group-hover:opacity-0 h-[16px] w-[16px] fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
            </svg>
            <span class="absolute inset-0 flex items-center justify-center bg-black/70 opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-[8px] font-bold text-center leading-tight px-1 z-10">LinkedIn</span>
          </a>
        </div>

      </div>

      <!-- Bottom Actions -->
      <div class="mt-auto pt-6 flex items-center justify-between border-t border-slate-200/70 dark:border-slate-700/80">
        <button @click="toggleDark()" class="p-2 rounded-full text-slate-600 dark:text-slate-400 hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary transition" title="Toggle Theme">
          <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
        </button>
        <div class="relative">
          <button @click="currentUser ? (showSignIn = !showSignIn) : azureSignIn()" class="p-2 rounded-full text-slate-600 dark:text-slate-400 hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary transition" :title="currentUser ? currentUser.name : 'Sign In'">
            <div v-if="currentUser" class="h-6 w-6 rounded-full bg-emerald-600 text-white flex items-center justify-center text-xs font-bold uppercase overflow-hidden">
              <img v-if="currentUser.photoURL" :src="currentUser.photoURL" :alt="currentUser.name" class="w-full h-full object-cover" />
              <span v-else>{{ currentUser.name ? currentUser.name.charAt(0) : 'U' }}</span>
            </div>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </button>

          <!-- Sign In Popup Menu -->
          <div v-if="showSignIn && currentUser" class="absolute bottom-[110%] right-0 w-60 transform origin-bottom-right bg-white dark:bg-slate-800 rounded-xl shadow-xl border border-slate-200 dark:border-slate-700 p-4 z-50 flex flex-col gap-3 mb-2">
            <h4 class="text-sm font-bold text-slate-900 dark:text-slate-100 border-b border-slate-200 dark:border-slate-700 pb-2">Welcome, {{ currentUser.name || currentUser.username }}</h4>
            <a href="https://portal.azure.com/" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center w-full px-3 py-1 text-sm font-medium rounded-md bg-blue-50 hover:bg-blue-100 dark:bg-blue-900/30 dark:hover:bg-blue-900/50 text-blue-600 dark:text-blue-400 transition-colors border border-blue-200 dark:border-blue-800">
              Azure Portal
            </a>
            <button @click="handleSignOut" class="flex items-center justify-center w-full px-3 py-1 text-sm font-medium rounded-md bg-red-50 hover:bg-red-100 dark:bg-red-900/30 dark:hover:bg-red-900/50 text-red-600 dark:text-red-400 transition-colors border border-red-200 dark:border-red-800">
              Sign Out
            </button>
          </div>
        </div>
      </div>
    </aside>

    <!-- Main Content Reader Experience -->
    
    <!-- Mobile Header -->
    <header class="md:hidden flex items-center justify-between px-6 py-4 border-b border-slate-200 dark:border-slate-700 bg-white dark:bg-dark-bg sticky top-0 z-30">
      <div class="flex items-center gap-3">
        <button @click="isMobileMenuOpen = true" class="p-2 -ml-2 rounded-md text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-primary">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
        <RouterLink to="/" class="flex items-center">
          <img src="./assets/logos/newlogo.png" alt="Logo" class="h-8 w-auto mix-blend-multiply dark:invert dark:mix-blend-screen" />
        </RouterLink>
      </div>
      <div>
        <button @click="toggleDark()" class="p-2 rounded-full text-slate-600 dark:text-slate-400 hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary transition" title="Toggle Theme">
          <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
        </button>
      </div>
    </header>

    <!-- Main Content Reader Experience -->
    <main class="flex-1 md:ml-72 flex flex-col min-h-screen relative w-full ">

      <div class="flex-1 w-full max-w-6xl mx-auto px-6 py-10 lg:px-12 flex flex-col xl:flex-row gap-16">
        
        <!-- Primary Reading Area -->
        <div class="flex-1 max-w-3xl text-lg leading-relaxed antialiased">
          <RouterView />
        </div>

        
      </div>

      <footer class="border-t border-slate-200 dark:border-slate-700 py-8 mt-auto mx-6 lg:mx-12">
        <div class="text-center md:text-left">
          <p class="text-base font-semibold text-slate-900 dark:text-slate-200">AI Generated Website by Vibe Codingthe content ai generation</p>
          <p class="mt-2 text-sm text-slate-500 dark:text-slate-400">© 2026  Today's Software Develope</p>
          
          <div class="mt-6 flex flex-col md:flex-row items-center gap-3 text-xs text-slate-500 dark:text-slate-400">
            <span>Built solely with:</span>
            <div class="flex flex-wrap items-center justify-center md:justify-start gap-4">
              <a href="https://code.visualstudio.com/" target="_blank" rel="noopener noreferrer" title="VS Code" class="flex items-center gap-1.5 font-medium hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" alt="VS Code" class="w-4 h-4" />
                <span>VS Code</span>
              </a>
              <a href="https://github.com/features/copilot" target="_blank" rel="noopener noreferrer" title="GitHub Copilot" class="flex items-center gap-1.5 font-medium hover:text-slate-900 dark:hover:text-white transition-colors">
                <img src="https://cdn.simpleicons.org/githubcopilot" alt="Copilot AI" class="w-4 h-4 dark:invert" />
                <span>Copilot AI</span>
              </a>
              <a href="https://azure.microsoft.com/en-us/products/cosmos-db/" target="_blank" rel="noopener noreferrer" title="Azure Cosmos DB" class="flex items-center gap-1.5 font-medium hover:text-blue-500 dark:hover:text-blue-300 transition-colors">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/azure/azure-original.svg" alt="Azure Cosmos DB" class="w-4 h-4" />
                <span>Azure Cosmos DB</span>
              </a>
              <a href="https://workers.cloudflare.com/" target="_blank" rel="noopener noreferrer" title="Cloudflare" class="flex items-center gap-1.5 font-medium hover:text-orange-500 dark:hover:text-orange-400 transition-colors">
                <img src="https://cdn.simpleicons.org/cloudflare" alt="Cloudflare" class="w-4 h-4" />
                <span>Cloudflare</span>
              </a>
            </div>
          </div>
        </div>
      </footer>
    </main>
  </div>
</template>

<style>
/* Smooth scrolling for the navigation links */
html {
  scroll-behavior: smooth;
}
</style>
