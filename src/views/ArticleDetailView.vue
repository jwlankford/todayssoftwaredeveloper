<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const article = ref(null)
const loading = ref(true)
const error = ref(null)

const getUnsplashImage = (articleInfo) => {
  if (!articleInfo) return '';
  const workingPhotos = [
    '1498050108023-c5249f4df085', '1555066931-4365d14bab8c', 
    '1515694346937-94d85e41e6f0', '1550751827-4bd374c3f58b', 
    '1518770660439-4636190af475', '1504164996022-09080787b6b3', 
    '1526374965328-7f61d4dc18c5', '1555949963-aa79dcee981c', 
    '1573164713988-8665fc963095', '1522071820081-009f0129c71c', 
    '1504384308090-c894fdcc538d'
  ];

  const strId = String(articleInfo.id || '');
  const hash = strId.length > 0 ? (strId.charCodeAt(0) + strId.charCodeAt(strId.length - 1) + strId.length) : Math.floor(Math.random() * 100);
  const photoId = workingPhotos[hash % workingPhotos.length];

  return `https://images.unsplash.com/photo-${photoId}?w=1200&h=600&fit=crop&q=80&auto=format`;
}

onMounted(async () => {
  try {
    const id = route.params.id
    const res = await fetch(`/api/articles/${id}`)
    
    if (res.status === 404) {
      throw new Error('Article not found.')
    }
    
    if (!res.ok) {
      throw new Error('Failed to fetch article data.')
    }
    
    article.value = await res.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="px-4 py-8 md:px-8 max-w-4xl mx-auto">
    <!-- Back button -->
    <button 
      @click="router.push('/articles')"
      class="mb-8 inline-flex items-center gap-2 text-sm font-medium text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-200 transition-colors"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
      </svg>
      Back to Articles
    </button>

    <div v-if="loading" class="text-slate-500 animate-pulse text-lg">
      Loading full article...
    </div>

    <div v-else-if="error" class="rounded-md bg-red-50 p-6 text-red-800 dark:bg-red-900/30 dark:text-red-300">
      <h3 class="text-lg font-bold mb-2">Error Loading Article</h3>
      <p>{{ error }}</p>
    </div>

    <article v-else-if="article">
      <header class="mb-4 pb-0">
        <!-- Hero Splash Image -->
        <div class="relative w-full h-64 md:h-96 mb-8 overflow-hidden rounded-2xl bg-slate-200 dark:bg-slate-700 shadow-md">
          <img :src="article.imageUrl || getUnsplashImage(article)" :alt="article.title" class="object-cover w-full h-full" />
        </div>
        
        <div class="flex items-center gap-x-4 text-sm mb-4 bg-slate-100 dark:bg-slate-800 rounded-full px-4 py-1.5 w-fit">
          <span class="font-medium text-slate-800 dark:text-slate-200">{{ article.category || 'Technology' }}</span>
          <span class="text-slate-400 dark:text-slate-500">&bull;</span>
          <time :datetime="article.createdAt" class="text-slate-600 dark:text-slate-400">
            {{ new Date(article.createdAt).toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) }}
          </time>
        </div>

        <h1 class="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white sm:text-3xl leading-tight mb-4">
          {{ article.title.replace(/\*\*/g, '').replace(/"/g, '') }}
        </h1>

        <div class="mt-8 flex items-center gap-x-4 border-t border-slate-200 dark:border-slate-800 pt-6">
          <div class="h-12 w-12 rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-center overflow-hidden">
            <template v-if="article.authorPhoto">
              <img :src="article.authorPhoto" :alt="article.author" class="h-full w-full object-cover"/>
            </template>
            <template v-else>
               <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
               </svg>
            </template>
          </div>
          <div>
            <div class="text-base font-semibold text-slate-900 dark:text-white">{{ article.author || 'Jeremy Lankford' }}</div>
            <div class="text-sm text-slate-500 dark:text-slate-400">AI Software Developer</div>
          </div>
        </div>
      </header>
      <!-- The content is now pre-formatted as HTML from the AI and admin generator -->
      <div 
        class="prose prose-slate prose-lg max-w-none prose-h2:font-bold dark:prose-invert"
        v-html="article.content">
      </div>
    </article>
  </div>
</template>