<script setup>
import AboutMe from '../components/AboutMe.vue'
import Skills from '../components/Skills.vue'
</script>

<template>
  <main class="mx-auto max-w-6xl px-4 py-10 md:px-6 md:py-14">
    <section class="text-center my-16">
      <h1 class="text-4xl md:text-6xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent pb-2">
        Modern Portfolio
      </h1>
      <p class="mt-4 text-lg md:text-xl text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">
        A clean and professional design inspired by modern tech websites.
      </p>
    </section>

    <div id="about" class="mb-10">
      <AboutMe />
    </div>

    <div id="skills" class="mb-10">
      <Skills />
    </div>

    <div id="projects" class="mb-10 rounded-lg bg-slate-100 dark:bg-dark-card p-8 text-center">
      <h3 class="text-lg font-semibold text-slate-500 md:text-xl border-b border-primary/20 pb-4 mb-4">
        Recent Projects
      </h3>
      <p class="text-slate-600 dark:text-slate-400 mb-6">Explore some of the applications and systems I've built to streamline processes and optimize performance.</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-left">
        <div class="rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-dark-bg p-6 hover:shadow-lg transition">
          <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-2">EPMS</h4>
          <p class="text-slate-600 dark:text-slate-400 text-sm mb-4">Employee Performance Management System highlighting organizational tracking and review metrics.</p>
          <span class="text-xs font-semibold text-primary bg-primary/10 px-2 py-1 rounded-full">Vue.js</span>
          <span class="text-xs font-semibold text-secondary bg-secondary/10 px-2 py-1 rounded-full ml-2">Node.js</span>
        </div>
      </div>
    </div>
  </main>
</template>