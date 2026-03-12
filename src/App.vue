<script setup>
import { ref } from 'vue'
import { useDark, useToggle } from '@vueuse/core'
import { RouterLink, RouterView } from 'vue-router'

const isDark = useDark()
const toggleDark = useToggle(isDark)

// Set to false when you are ready to launch!
const isUnderConstruction = ref(true)
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

  <div v-else class="flex min-h-screen text-slate-800 dark:text-slate-200 bg-white dark:bg-dark-bg">
    <!-- Fixed Side Navigation -->
    <aside class="hidden md:flex fixed top-0 left-0 h-screen w-72 border-r border-slate-200/70 bg-slate-50/50 dark:border-slate-700/80 dark:bg-slate-900/50 flex-col pt-8 pb-6 px-6 overflow-y-auto z-50">
      <!-- Logo -->
      <div class="mb-10 flex justify-center mt-4">
        <RouterLink to="/" class="transition hover:opacity-80">
          <img src="./assets/logos/newlogo.png" alt="Today's Software Developer Logo" class="h-24 w-auto mix-blend-multiply dark:invert dark:mix-blend-screen">
        </RouterLink>
      </div>

      <!-- Navigation Links -->
      <nav class="flex flex-col gap-3 text-base font-medium text-slate-600 dark:text-slate-400">
        <RouterLink to="/#about" class="px-3 py-2 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary">About the Book</RouterLink>
        <RouterLink to="/#skills" class="px-3 py-2 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary">Core Skills</RouterLink>
        <RouterLink to="/ai-tools" class="px-3 py-2 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary">AI Tools & Guides</RouterLink>
        <RouterLink to="/articles" class="px-3 py-2 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary">Articles</RouterLink>
        <a href="https://www.youtube.com/@TodaysSoftwareDev" target="_blank" rel="noopener noreferrer" class="mt-2 flex items-center justify-center gap-2 w-full py-2.5 px-4 bg-red-600 hover:bg-red-700 text-white rounded-lg shadow-sm transition font-bold">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 fill-current" viewBox="0 0 24 24">
            <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z" />
          </svg>
          YouTube Channel
        </a>
        
        <!-- Divider -->
        <div class="my-4 border-t border-slate-200/70 dark:border-slate-700/80"></div>
        
        <a href="#" class="px-3 py-2 rounded-md transition hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary flex items-center gap-2 font-bold">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          Get the Book
        </a>
      </nav>

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
        <button class="p-2 rounded-full text-slate-600 dark:text-slate-400 hover:bg-slate-200/50 hover:text-primary dark:hover:bg-slate-800/50 dark:hover:text-secondary transition">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
        </button>
      </div>
    </aside>

    <!-- Main Content Reader Experience -->
    <main class="flex-1 ml-0 md:ml-72 flex flex-col min-h-screen relative">
      <div class="flex-1 w-full max-w-6xl mx-auto px-6 py-10 lg:px-12 flex flex-col xl:flex-row gap-16">
        
        <!-- Primary Reading Area -->
        <div class="flex-1 max-w-3xl text-lg leading-relaxed antialiased">
          <RouterView />
        </div>

        <!-- Secondary Content Column (Right Sidebar for links and guides) -->
        <aside class="hidden xl:block w-72 shrink-0">
          <div class="sticky top-12 border-l border-slate-200 dark:border-slate-700 pl-8 pb-8">
            <a href="https://www.amazon.com/" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 w-full py-3 px-4 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg shadow-sm transition font-bold mb-10">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
              Buy
            </a>

            <h3 class="text-sm font-bold uppercase tracking-widest text-slate-400 dark:text-slate-500 mb-6">Companion Resources</h3>
            <ul class="space-y-4 text-sm font-medium text-slate-600 dark:text-slate-400">
              <li>
                <a href="#" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
                  Download Setup Guide
                </a>
              </li>
              <li>
                <a href="#" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>
                  Source Code Repository
                </a>
              </li>
              <li>
                <a href="#" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" /></svg>
                  Author Podcast Interview
                </a>
              </li>
            </ul>
          </div>
        </aside>
      </div>

      <footer class="border-t border-slate-200 dark:border-slate-700 py-8 mt-auto mx-6 lg:mx-12">
        <div class="text-center md:text-left">
          <p class="text-base font-semibold text-slate-900 dark:text-slate-200">Jeremy Lankford</p>
          <p class="mt-2 text-sm text-slate-500 dark:text-slate-400">© 2026 | Software Engineer & IT Educator</p>
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
