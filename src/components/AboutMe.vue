<template>
  <section class="rounded-lg bg-slate-100 dark:bg-dark-card p-8 md:p-10">
    <div class="flex flex-col items-center gap-8 md:flex-row md:items-start">
      <div class="flex h-36 w-36 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-primary to-secondary shadow-lg overflow-hidden">
        <img src="../assets/images/me_logo.jpg" alt="Jeremy Lankford" class="h-full w-full object-cover" />
      </div>

      <div class="flex-1 text-center md:text-left">
        <h2 class="mb-2 text-3xl font-bold text-slate-900 md:text-4xl dark:text-white">Jeremy Lankford</h2>
        <p class="mb-5 text-lg font-medium text-slate-600 dark:text-slate-400">Senior Software Engineer & Aspiring IT Educator</p>
        
        <div class="space-y-4 text-base leading-relaxed text-slate-600 md:text-lg dark:text-slate-400">
          <p>
            With over 30 years in software development, from Java and C++ to modern Vue and React, I specialize in full-stack architecture and cloud-native solutions.
          </p>
          <p>
            I am completing my MBA in IT Management and preparing for doctoral studies in AI, with a strong focus on leadership, performance management systems, and mentoring the next generation of developers.
          </p>
        </div>

        <div class="mt-7 flex flex-wrap justify-center gap-2 md:justify-start">
          <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-semibold text-primary dark:bg-primary/20 dark:text-indigo-300">Software Architecture</span>
          <span class="rounded-full bg-secondary/10 px-3 py-1 text-xs font-semibold text-secondary dark:bg-secondary/20 dark:text-purple-300">AI Education</span>
          <span class="rounded-full bg-teal-500/10 px-3 py-1 text-xs font-semibold text-teal-600 dark:bg-teal-500/20 dark:text-teal-300">IT Leadership</span>
        </div>
      </div>
    </div>
  </section>
</template>