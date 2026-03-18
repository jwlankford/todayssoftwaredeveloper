import re

with open('worker.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the 404 return with an env.ASSETS fallback
old_catch_all = "// 404 for any other route\n      return new Response('Not Found', { status: 404, headers: corsHeaders });"

new_catch_all = """// Handle API 404s
      if (url.pathname.startsWith('/api/')) {
        return new Response('API Route Not Found', { status: 404, headers: corsHeaders });
      }

      // Serve static assets via env.ASSETS
      // Try fetching the actual file
      const assetResponse = await env.ASSETS.fetch(request);
      
      // If it's a SPA route (not a file like .css) and resulted in a 404, fallback to index.html
      if (assetResponse.status === 404 && request.method === 'GET' && !url.pathname.includes('.')) {
         return env.ASSETS.fetch(new Request(new URL('/', request.url)));
      }
      return assetResponse;"""

if old_catch_all in code:
    code = code.replace(old_catch_all, new_catch_all)
    with open('worker.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("worker.js updated")
else:
    print("Could not find the target string to replace")

