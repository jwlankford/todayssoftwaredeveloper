<script setup>
const aiTools = [
  {
    name: 'GitHub Copilot',
    description: 'Your AI pair programmer that suggests code and entire functions in real-time right from your editor.',
    link: 'https://github.com/features/copilot',
    gradient: 'from-blue-500 to-indigo-500'
  },
  {
    name: 'ChatGPT (OpenAI)',
    description: 'A conversational powerhouse for brainstorming architecture, debugging errors, and drafting documentation.',
    link: 'https://chat.openai.com/',
    gradient: 'from-purple-500 to-pink-500'
  },
  {
    name: 'Cursor',
    description: 'An AI-first code editor built for pair programming with an intelligent agent, making massive codebases easy to refactor.',
    link: 'https://cursor.sh/',
    gradient: 'from-emerald-500 to-teal-500'
  },
  {
    name: 'v0.dev',
    description: 'A generative UI system by Vercel that converts natural language into React/Tailwind code ready to drop into your project.',
    link: 'https://v0.dev/',
    gradient: 'from-orange-500 to-red-500'
  },
  {
    name: 'Claude (Anthropic)',
    description: 'Anthropic’s top AI model. Extremely capable at reasoning, coding, and following complex multi-step instructions with massive context windows.',
    link: 'https://claude.ai/',
    gradient: 'from-amber-500 to-orange-400'
  },
  {
    name: 'Codeium',
    description: 'A free, ultra-fast AI code acceleration toolkit with intelligent autocomplete, localized chat, and impressive cross-IDE support.',
    link: 'https://codeium.com/',
    gradient: 'from-cyan-500 to-blue-500'
  },
  {
    name: 'Phind',
    description: 'An AI search engine specifically fine-tuned for developers. Cuts through SEO spam to find documentation and stack-traces instantly.',
    link: 'https://www.phind.com/',
    gradient: 'from-slate-600 to-slate-900'
  },
  {
    name: 'Amazon Q Developer',
    description: 'AWS’s generative AI-powered assistant designed to write code, design features, and upgrade applications directly within IDEs.',
    link: 'https://aws.amazon.com/q/developer/',
    gradient: 'from-yellow-400 to-amber-600'
  },
  {
    name: 'Tabnine',
    description: 'Privacy-focused AI code assistant that learns your codebase directly and offers completions without leaking IP to external servers.',
    link: 'https://www.tabnine.com/',
    gradient: 'from-indigo-400 to-cyan-400'
  },
  {
    name: 'Bolt.new',
    description: 'Browser-based AI web development agent capable of generating full-stack applications with databases and hosting securely.',
    link: 'https://bolt.new/',
    gradient: 'from-rose-500 to-pink-600'
  }
];
</script>

<template>
  <main class="mx-auto max-w-6xl px-4 py-10 md:px-6 md:py-14">
    <section class="text-center my-16">
      <h1 class="text-4xl md:text-6xl font-bold bg-gradient-to-r from-teal-500 to-primary bg-clip-text text-transparent pb-2">
        Top Developer AI Tools
      </h1>
      <p class="mt-4 text-lg md:text-xl text-slate-600 dark:text-slate-400 max-w-2xl mx-auto">
        A curated list of the best AI-powered tools to 10x your development workflow, debugging, and code generation.
      </p>
    </section>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      
      <div v-for="tool in aiTools" :key="tool.name" class="rounded-xl flex flex-col border border-slate-200 dark:border-slate-700 bg-white dark:bg-dark-card overflow-hidden transition-all hover:shadow-xl hover:-translate-y-1">
        <div :class="`h-3 bg-gradient-to-r ${tool.gradient}`"></div>
        <div class="p-6 flex flex-col flex-grow">
          <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-3">{{ tool.name }}</h3>
          <p class="text-slate-600 dark:text-slate-400 mb-6 flex-grow">
            {{ tool.description }}
          </p>
          <a :href="tool.link" target="_blank" rel="noopener noreferrer" class="inline-block mt-auto text-primary font-semibold hover:text-secondary hover:underline">Learn more &rarr;</a>
        </div>
      </div>

    </div>
  </main>
</template>