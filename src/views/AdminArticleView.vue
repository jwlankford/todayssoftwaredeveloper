<script setup>
import { ref } from 'vue'
import { msalInstance } from '../authConfig'
import md5 from 'md5'

const title = ref('')
const description = ref('')
const date = ref(new Date().toISOString().split('T')[0])
const content = ref('')
const imageUrl = ref('')
const isGenerating = ref(false)
const isPublishing = ref(false)
const publishSuccess = ref(false)
const errorMsg = ref('')

function generateImage() {
  const workingPhotos = [
    '1498050108023-c5249f4df085', // Code/Tech
    '1555066931-4365d14bab8c',    // Code/Tech
    '1515694346937-94d85e41e6f0', // Tech/Abstract
    '1550751827-4bd374c3f58b',    // Default/Tech
    '1518770660439-4636190af475', // Hardware/Tech
    '1504164996022-09080787b6b3', // Abstract/Lines
    '1526374965328-7f61d4dc18c5', // Matrix/Tech
    '1555949963-aa79dcee981c',    // Clean Tech
    '1573164713988-8665fc963095', // Tech
    '1522071820081-009f0129c71c', // Strategy/Chess
    '1504384308090-c894fdcc538d'  // Tech/Geometric
  ];
  const photoId = workingPhotos[Math.floor(Math.random() * workingPhotos.length)]
  return `https://images.unsplash.com/photo-${photoId}?w=1200&h=630&fit=crop&q=80&auto=format`
}

async function formatArticle() {
  if (!title.value || !description.value) {
    errorMsg.value = 'Please provide a title and article content.'
    return
  }
  
  errorMsg.value = ''
  
  // Format the HTML locally
  content.value = `<div class="article-body">\n${description.value}\n</div>`
}

async function publishArticle() {
  if (!title.value || !content.value) {
    errorMsg.value = 'Title and content are required to publish.'
    return
  }

  errorMsg.value = ''
  isPublishing.value = true

  let authorName = 'Jeremy Lankford'
  let authorPhoto = ''

  // Attempt to get the signed-in user's details
  const account = msalInstance.getActiveAccount() || msalInstance.getAllAccounts()[0]
  if (account) {
    authorName = account.name || account.username
    
    // 1. First check if it's already in the ID token claims
    if (account.idTokenClaims?.picture) {
      authorPhoto = account.idTokenClaims.picture;
    } else {
      // 2. Otherwise try fetching from Microsoft Graph
      try {
        const tokenResponse = await msalInstance.acquireTokenSilent({
          scopes: ["User.Read"],
          account: account
        });
        const photoRes = await fetch("https://graph.microsoft.com/v1.0/me/photo/$value", {
          headers: { Authorization: `Bearer ${tokenResponse.accessToken}` }
        });
        if (photoRes.ok) {
           const blob = await photoRes.blob();
           authorPhoto = await new Promise((resolve) => {
             const reader = new FileReader();
             reader.onloadend = () => resolve(reader.result);
             reader.readAsDataURL(blob);
           });
        }
      } catch (err) {
         console.warn("Could not fetch Azure avatar for article", err)
      }
      
      // Gravatar fallback for published articles
      if (!authorPhoto && account.username) {
         const hash = md5(account.username.toLowerCase().trim());
         authorPhoto = `https://www.gravatar.com/avatar/${hash}?d=identicon`;
      }
    }
  }

  // Generate image right at the time of publishing
  imageUrl.value = generateImage()

  try {
    const response = await fetch('/api/articles', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: title.value,
        content: content.value,
        author: authorName,
        authorPhoto: authorPhoto,
        imageUrl: imageUrl.value,
        createdAt: new Date(date.value).toISOString()
      })
    })

    if (!response.ok) {
      throw new Error('Failed to save the article to the database')
    }

    publishSuccess.value = true
    setTimeout(() => {
      publishSuccess.value = false
      imageUrl.value = ''
    }, 3000)

    // Clear form
    title.value = ''
    description.value = ''
    content.value = ''
    imageUrl.value = ''
  } catch (err) {
    errorMsg.value = err.message
  } finally {
    isPublishing.value = false
  }
}
</script>

<template>
  <div class="px-4 py-8 md:px-8">
    <div class="mb-8 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
      <div>
        <h1 class="text-3xl font-bold tracking-tight text-slate-900 dark:text-slate-100">Add New Article</h1>
        <p class="mt-2 text-lg text-slate-600 dark:text-slate-400">Manually publish articles to Cosmos DB.</p>
      </div>
    </div>

    <!-- Error Banner -->
    <div v-if="errorMsg" class="mb-6 rounded-md bg-red-50 p-4 text-red-800 dark:bg-red-900/30 dark:text-red-300">
      {{ errorMsg }}
    </div>
    
    <!-- Success Banner -->
    <div v-if="publishSuccess" class="mb-6 rounded-md bg-green-50 p-4 text-green-800 dark:bg-green-900/30 dark:text-green-300">
      Article published successfully!
      <div v-if="imageUrl" class="mt-4">
        <p class="text-sm font-medium mb-2">Assigned Image:</p>
        <img :src="imageUrl" alt="Assigned Image" class="w-full h-auto max-h-48 object-cover rounded-md border border-slate-300 dark:border-slate-700 shadow-sm" />
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Form Input Column -->
      <div class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Article Title</label>
          <input 
            v-model="title" 
            type="text" 
            placeholder="e.g., The Future of Vue.js in 2026"
            class="w-full rounded-md border border-slate-300 bg-white px-4 py-2 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100 focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
          />
        </div>

        <div>
           <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Date</label>
           <input 
             v-model="date" 
             type="date" 
             class="w-full rounded-md border border-slate-300 bg-white px-4 py-2 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100 focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
           />
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Article Body / Content</label>
          <textarea 
            v-model="description" 
            rows="4" 
            placeholder="Paste your raw article content here to automatically format it."
            class="w-full rounded-md border border-slate-300 bg-white px-4 py-2 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100 focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
          ></textarea>
        </div>

        <button 
          @click="formatArticle" 
          :disabled="isPublishing"
          class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-4 rounded-lg transition disabled:opacity-50"
        >
          <span>Format Content</span>
        </button>
      </div>

      <!-- Preview / Editor Column -->
      <div class="space-y-6 flex flex-col h-full">

        <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Content Editor (HTML)</label>
        <textarea 
          v-model="content" 
          class="w-full flex-1 min-h-[400px] rounded-md border border-slate-300 bg-slate-50 p-4 font-mono text-sm dark:border-slate-700 dark:bg-slate-900/80 dark:text-slate-300 focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary shadow-inner whitespace-pre-wrap leading-relaxed"
          placeholder="Enter your HTML content here."
        ></textarea>
        
        <button 
          @click="publishArticle" 
          :disabled="!content || isPublishing"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-lg transition disabled:opacity-50 mt-4"
        >
          <span v-if="isPublishing">Publishing to Cosmos DB...</span>
          <span v-else>Publish Article</span>
        </button>
      </div>
    </div>
  </div>
</template>