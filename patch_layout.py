import re

with open('src/App.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the end of the navigation
nav_end_idx = content.find('</nav>') + len('</nav>')

# The replacement cluster to inject right after </nav>
injected_content = """

      <!-- Social Buttons & Resources -->
      <div class="mt-6 mb-2">
        <div class="grid grid-cols-2 gap-2 mb-4">
          <a href="https://www.youtube.com/@TodaysSoftwareDev" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1.5 w-full py-1.5 px-2 text-xs bg-red-600 hover:bg-red-700 text-white rounded-md shadow-sm transition font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 fill-current" viewBox="0 0 24 24">
              <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z" />
            </svg>
            YouTube
          </a>
          <a href="https://github.com/jwlankford" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1.5 w-full py-1.5 px-2 text-xs bg-slate-800 hover:bg-slate-900 dark:bg-slate-700 dark:hover:bg-slate-600 text-white rounded-md shadow-sm transition font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 fill-current" viewBox="0 0 24 24">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub
          </a>
          <a href="https://www.gitlab.com/jwlankford" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1.5 w-full py-1.5 px-2 text-xs bg-[#FC6D26] hover:bg-[#E24329] text-white rounded-md shadow-sm transition font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 fill-current" viewBox="0 0 24 24">
              <path d="M23.955 13.587l-2.242-6.903c-.201-.617-1.084-.617-1.285 0l-1.465 4.512h-4.3l-1.465-4.512c-.201-.617-1.084-.617-1.285 0L9.67 13.587l-3.344-10.297c-.201-.617-1.084-.617-1.285 0L2.8 10.192H.316c-.452 0-.678.547-.358.866l11.455 11.411a.488.488 0 0 0 .69 0L23.559 11.06c.32-.32.094-.867-.358-.867h-2.484l2.238 6.892z" fill="#E24329"/><path d="M12 22.47L2.8 13.587H15.17l-3.17 8.883z" fill="#FC6D26"/><path d="M2.8 13.587L.316 11.06c-.32-.32-.094-.866.358-.866h2.483l5.042 10.294-5.4-6.892z" fill="#FCA326"/><path d="M12 22.47l9.2-8.883H8.83l3.17 8.883z" fill="#E24329"/><path d="M21.2 13.587l2.484-2.527c.32-.32.094-.866-.358-.866h-2.483L15.8 20.488l5.4-6.901z" fill="#FCA326"/>
            </svg>
            GitLab
          </a>
          <a href="https://www.linkedin.com/in/jwlankford" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1.5 w-full py-1.5 px-2 text-xs bg-[#0a66c2] hover:bg-[#004182] text-white rounded-md shadow-sm transition font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 fill-current" viewBox="0 0 24 24">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
            </svg>
            LinkedIn
          </a>
        </div>

        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 dark:text-slate-500 mb-3 mt-6">Companion Resources</h3>
        <ul class="space-y-3 text-xs font-medium text-slate-600 dark:text-slate-400">
          <li>
            <a href="#" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
              Download Setup Guide
            </a>
          </li>
          <li>
            <a href="https://github.com/jwlankford/todayssoftwaredeveloper" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" /></svg>
              Source Code Repository
            </a>
          </li>
          <li>
            <a href="#" class="flex items-center gap-2 hover:text-primary dark:hover:text-secondary transition">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" /></svg>
              Author Podcast Interview
            </a>
          </li>
        </ul>
      </div>"""

content = content[:nav_end_idx] + injected_content + content[nav_end_idx:]

# Remove the right aside by finding its boundaries
# It starts at: <!-- Secondary Content Column (Right Sidebar for links and guides) -->
# Or `<aside class="hidden xl:block w-72 shrink-0">`
# and ends at the corresponding `</aside>`

aside_start_comment = '<!-- Secondary Content Column (Right Sidebar for links and guides) -->'
start_idx = content.find(aside_start_comment)

if start_idx != -1:
    end_idx = content.find('</aside>', start_idx) + len('</aside>')
    # Let's remove the extra newline around it too
    content = content[:start_idx] + content[end_idx:]

# Also we might want to trim any gap from the flex row where it used to be.
# It used to say: <div class="flex-1 w-full max-w-6xl mx-auto px-6 py-10 lg:px-12 flex flex-col xl:flex-row gap-16">
# Let's change gap-16 to gap-0 or remove xl:flex-row to make it just flex flex-col items-center

with open('src/App.vue', 'w', encoding='utf-8') as f:
    f.write(content)
