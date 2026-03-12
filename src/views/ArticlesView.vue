<script setup>
import { ref, onMounted, computed } from 'vue'

const articles = ref([])
const loading = ref(true)
const error = ref(null)
const selectedFilter = ref('All')
const searchQuery = ref('')

const getUnsplashImage = (article) => {
  const workingPhotos = [
    '1498050108023-c5249f4df085', '1555066931-4365d14bab8c', 
    '1515694346937-94d85e41e6f0', '1550751827-4bd374c3f58b', 
    '1518770660439-4636190af475', '1504164996022-09080787b6b3', 
    '1526374965328-7f61d4dc18c5', '1555949963-aa79dcee981c', 
    '1573164713988-8665fc963095', '1522071820081-009f0129c71c', 
    '1504384308090-c894fdcc538d'
  ];

  // Use the article ID to deterministically select the photo
  const strId = String(article.id || '');
  const hash = strId.length > 0 ? (strId.charCodeAt(0) + strId.charCodeAt(strId.length - 1) + strId.length) : Math.floor(Math.random() * 100);
  const photoId = workingPhotos[hash % workingPhotos.length];

  return `https://images.unsplash.com/photo-${photoId}?w=800&h=450&fit=crop&q=80&auto=format`;
}

onMounted(async () => {
  try {
    // Calling the API exposed by our Cloudflare Worker!
    // Handled by Vite proxy in development, and native routing in production!
    const res = await fetch('/api/articles')
    if (!res.ok) throw new Error('Failed to fetch articles')
    articles.value = await res.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})

const availableMonths = computed(() => {
  const months = new Set()
  articles.value.forEach(article => {
    if (article.createdAt) {
      const date = new Date(article.createdAt)
      if (!isNaN(date)) {
        const label = date.toLocaleDateString(undefined, { month: 'long', year: 'numeric' })
        months.add(label)
      }
    }
  })
  
  const sorted = Array.from(months).sort((a, b) => {
     return new Date(b) - new Date(a)
  })
  
  return ['All', ...sorted]
})

const filteredArticles = computed(() => {
  let result = articles.value

  // Apply month filter
  if (selectedFilter.value !== 'All') {
    result = result.filter(article => {
      if (!article.createdAt) return false
      const date = new Date(article.createdAt)
      if (isNaN(date)) return false
      const label = date.toLocaleDateString(undefined, { month: 'long', year: 'numeric' })
      return label === selectedFilter.value
    })
  }

  // Apply search query filter
  if (searchQuery.value.trim() !== '') {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(article => {
      const titleMatch = article.title?.toLowerCase().includes(query)
      const abstractMatch = article.content?.replace(/<[^>]*>?/gm, '')?.toLowerCase().includes(query)
      return titleMatch || abstractMatch
    })
  }

  return result
})
</script>

<template>
  <div class="space-y-0">
    <header class="border-b border-slate-200 pb-8 dark:border-slate-700/80">
      <h1 class="text-4xl font-bold tracking-tight text-slate-900 dark:text-white sm:text-5xl">
        Articles
      </h1>
      <p class="mt-4 text-lg text-slate-600 dark:text-slate-400 mb-8">
        Thoughts, tutorials, and deep dives into software architecture, AI education, and IT leadership.
      </p>

      <div class="flex flex-col sm:flex-row gap-4 mt-8">
        <!-- Search Bar -->
        <div class="relative flex-1">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search articles by title or content..."
            class="block w-full pl-10 pr-3 py-2 border border-slate-300 rounded-lg bg-white dark:bg-slate-800 dark:border-slate-700 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-shadow transition-colors"
          />
        </div>

        <!-- Month Filter -->
        <div class="sm:w-64">
          <select 
            v-model="selectedFilter"
            class="block w-full py-2 px-3 border border-slate-300 rounded-lg bg-white dark:bg-slate-800 dark:border-slate-700 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-shadow transition-colors appearance-none cursor-pointer"
          >
            <option v-for="month in availableMonths" :key="month" :value="month">
              {{ month === 'All' ? 'All Months' : month }}
            </option>
          </select>
        </div>
      </div>
    </header>

    <div class="space-y-0">
      
      <div v-if="loading" class="text-slate-500 animate-pulse">Loading articles from Cosmos DB...</div>
      
      <div v-else-if="error" class="text-red-500">Error: {{ error }}</div>
      
      <div v-else-if="filteredArticles.length === 0" class="text-slate-500 py-8 text-center bg-slate-50 dark:bg-slate-800/50 rounded-xl">
        <p class="text-lg mb-2">No articles found matching your criteria.</p>
        <button @click="searchQuery = ''; selectedFilter = 'All'" class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-800 font-medium">Clear Filters</button>
      </div>

      <!-- Real Articles from Cosmos DB -->
      <article
        v-for="article in filteredArticles"
        :key="article.id"
        class="group relative flex flex-col sm:flex-row items-center justify-start gap-6 rounded-2xl p-6 transition-all hover:bg-slate-50 dark:hover:bg-slate-800/50 h-auto sm:h-[150px] overflow-hidden"
      >
        <!-- Preview Image -->
        <div class="relative w-full sm:w-48 h-48 sm:h-full shrink-0 overflow-hidden rounded-xl bg-slate-200 dark:bg-slate-700">
          <img :src="article.imageUrl || getUnsplashImage(article)" :alt="article.title" class="object-cover w-full h-full transition-transform duration-500 group-hover:scale-105" />
        </div>

        <div class="flex flex-col justify-center h-full w-full overflow-hidden">
          <div class="flex items-center gap-x-4 text-xs mb-2">
            <time :datetime="article.createdAt" class="text-slate-500">
              {{ new Date(article.createdAt).toLocaleDateString() }}
            </time>
            <span class="relative z-10 rounded-full bg-slate-100 px-3 py-1 font-medium text-slate-600 dark:bg-slate-800 dark:text-slate-300">
              {{ article.category || 'Tech' }}
            </span>
          </div>
          <div class="group relative flex-1">
            <h3 class="text-lg sm:text-xl font-semibold leading-tight text-slate-900 dark:text-white group-hover:text-amber-600 dark:group-hover:text-amber-400 line-clamp-2">
              <RouterLink :to="`/articles/${article.id}`">
                <span class="absolute inset-0"></span>
                {{ article.title.replace(/\*\*/g, '').replace(/"/g, '') }}
              </RouterLink>
            </h3>
            <p class="mt-2 line-clamp-2 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
              {{ article.content.replace(/<[^>]*>?/gm, '').substring(0, 150) }}...
            </p>
          </div>
        </div>
      </article>

      <!-- Old Placeholder (Commented out) -->
      <!--
      <article class="group relative flex flex-col items-start justify-between rounded-2xl p-6 transition-all hover:bg-slate-50 dark:hover:bg-slate-800/50">
        ... (old mock design)
      </article>
      -->
    </div>
  </div>
</template>
