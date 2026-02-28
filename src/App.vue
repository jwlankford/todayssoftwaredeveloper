<script setup>
import { useDark, useToggle } from '@vueuse/core'
import { RouterLink, RouterView } from 'vue-router'

const isDark = useDark()
const toggleDark = useToggle(isDark)
</script>

<template>
  <div class="text-slate-800 dark:text-slate-200">
    <nav class="sticky top-0 z-50 border-b border-slate-200/70 bg-white/80 backdrop-blur-md dark:border-slate-700/80 dark:bg-dark-bg/80">
      <div class="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <RouterLink to="/" class="font-bold text-lg text-primary hover:text-secondary transition">
          Today's Software Developer
        </RouterLink>
        <div class="hidden items-center gap-7 text-sm font-semibold text-slate-600 md:flex dark:text-slate-400">
          <RouterLink to="/#about" class="transition hover:text-primary dark:hover:text-secondary">About</RouterLink>
          <RouterLink to="/#skills" class="transition hover:text-primary dark:hover:text-secondary">Skills</RouterLink>
          <RouterLink to="/ai-tools" class="transition hover:text-primary dark:hover:text-secondary">AI Tools</RouterLink>
          <button @click="toggleDark()" class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-secondary">
            <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
            </svg>
          </button>
          <button class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-secondary">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </button>
        </div>
      </div>
    </nav>
    
    <RouterView />

    <footer class="border-t border-slate-200 dark:border-slate-700 py-10 mt-auto">
      <div class="mx-auto max-w-6xl px-6 text-center">
        <p class="text-base font-semibold text-slate-900 dark:text-slate-200">Jeremy Lankford</p>
        <p class="mt-2 text-sm text-slate-500 dark:text-slate-400">© 2026 | Software Engineer & IT Educator</p>
      </div>
    </footer>
  </div>
</template>

<style>
/* Smooth scrolling for the navigation links */
html {
  scroll-behavior: smooth;
}
</style>
