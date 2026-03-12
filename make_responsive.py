with open('src/App.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add isMobileMenuOpen state
content = content.replace("const currentUser = ref(null)", "const currentUser = ref(null)\nconst isMobileMenuOpen = ref(false)\n\n// Close mobile menu when route changes\nimport { watch } from 'vue'\nimport { useRoute } from 'vue-router'\nconst route = useRoute()\nwatch(() => route.path, () => { isMobileMenuOpen.value = false })")

# 2. Modify side nav classes
orig_aside = '<aside class="hidden md:flex fixed top-0 left-0 h-screen w-72 border-r border-slate-200/70 bg-slate-50/50 dark:border-slate-700/80 dark:bg-slate-900/50 flex-col pt-8 pb-6 px-6 overflow-y-auto z-50">'

new_aside = '''
    <!-- Mobile Menu Backdrop -->
    <div v-if="isMobileMenuOpen" @click="isMobileMenuOpen = false" class="fixed inset-0 bg-slate-900/50 z-40 md:hidden backdrop-blur-sm transition-opacity"></div>

    <!-- Fixed Side Navigation -->
    <aside :class="['flex fixed top-0 left-0 h-screen w-72 border-r border-slate-200/70 bg-slate-50 dark:border-slate-700/80 dark:bg-slate-900 flex-col pt-8 pb-6 px-6 overflow-y-auto z-50 transition-transform duration-300 ease-in-out md:translate-x-0', isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full']">
'''
if orig_aside in content:
    content = content.replace(orig_aside, new_aside)
else:
    print("WARNING: aside not found. Trying flexible replacement.")
    # More flexible regex
    import re
    content = re.sub(r'<aside class="hidden md:flex fixed[^>]+>', new_aside, content)

# 3. Add mobile header above <main>
orig_main = '<main class="flex-1 ml-0 md:ml-72 flex flex-col min-h-screen relative">'

mobile_header = '''
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
    <main class="flex-1 md:ml-72 flex flex-col min-h-screen relative w-full pt-16 md:pt-0">
'''

# Wait, there's a margin issue. I should be careful how `flex-1 ml-0 md:ml-72...` behaves. I'll just keep the main class but inject mobile_header before it. Wait, the `aside` has a mobile backdrop, which is good. But we need a top bar.
# Also I'll change <div v-else class="flex min-h-screen ..."> to not `flex` or to handle column setup? No, `flex` works if we specify `flex-col md:flex-row`.
content = content.replace('<div v-else class="flex min-h-screen text-slate-800 dark:text-slate-200 bg-white dark:bg-dark-bg">', '<div v-else class="flex flex-col md:flex-row min-h-screen text-slate-800 dark:text-slate-200 bg-white dark:bg-dark-bg w-full">')

# Modify main tag explicitly
content = content.replace(orig_main, orig_main) # keep main as is just prepend header
if '<main ' in content:
    content = content.replace('<main class="flex-1 ml-0 md:ml-72 flex flex-col min-h-screen relative">', mobile_header.replace('pt-16 md:pt-0', ''))

with open('src/App.vue', 'w', encoding='utf-8') as f:
    f.write(content)

print("Responsive changes applied")
