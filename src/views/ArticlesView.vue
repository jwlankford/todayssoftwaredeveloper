<template>
  <div class="space-y-12">
    <header class="border-b border-slate-200 pb-8 dark:border-slate-700/80">
      <h1 class="text-4xl font-bold tracking-tight text-slate-900 dark:text-white sm:text-5xl">
        Articles
      </h1>
      <p class="mt-4 text-lg text-slate-600 dark:text-slate-400">
        Thoughts, tutorials, and deep dives into software architecture, AI education, and IT leadership.
      </p>
    </header>

    <div class="space-y-10">
      <!-- Article Placeholder -->
      <article class="group relative flex flex-col items-start justify-between rounded-2xl p-6 transition-all hover:bg-slate-50 dark:hover:bg-slate-800/50">
        <div class="flex items-center gap-x-4 text-xs">
          <time datetime="2026-03-11" class="text-slate-500">March 11, 2026</time>
          <span class="relative z-10 rounded-full bg-slate-100 px-3 py-1.5 font-medium text-slate-600 dark:bg-slate-800 dark:text-slate-300">Software Architecture</span>
        </div>
        <div class="group relative">
          <h3 class="mt-3 text-2xl font-semibold leading-6 text-slate-900 dark:text-white group-hover:text-slate-600 dark:group-hover:text-slate-300">
            <a href="#">
              <span class="absolute inset-0"></span>
              Coming Soon: The Evolution of Cloud-Native Deployments
            </a>
          </h3>
          <p class="mt-4 line-clamp-3 text-base leading-relaxed text-slate-600 dark:text-slate-400">
            A comprehensive look at how container orchestration and emerging AI-driven deployment strategies are changing the landscape of modern applications.
          </p>
        </div>
        <div class="relative mt-4 flex items-center gap-x-4">
          <div class="text-sm leading-6">
            <p class="font-semibold text-slate-900 dark:text-white">
              <a href="#">
                <span class="absolute inset-0"></span>
                Jeremy Lankford
              </a>
            </p>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>
