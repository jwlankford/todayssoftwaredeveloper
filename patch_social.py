import re

with open('src/App.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the social buttons block
grid_start = content.find('<div class="grid grid-cols-2 gap-2 mt-6 mb-4">')
if grid_start == -1:
    print("Could not find grid container")
    exit(1)

# Find the end of the div
div_end_idx = content.find('</div>', grid_start)
if div_end_idx != -1:
    grid_end = content.find('</div>', div_end_idx + 1)
    
# Actually let's use regex to find each a tag
# We'll replace the grid with a flex container
new_content = content.replace('<div class="grid grid-cols-2 gap-2 mt-6 mb-4">', '<div class="flex justify-between gap-2 mt-6 mb-4">')

def replace_a_tag(match):
    full_a = match.group(0)
    href = match.group(1)
    color_classes = match.group(2)
    svg = match.group(3)
    text = match.group(4).strip()
    
    # Increase svg size for 50x50 button
    svg = svg.replace('h-3 w-3', 'h-[22px] w-[22px]')
    svg = svg.replace('<svg ', '<svg class="transition-opacity duration-300 group-hover:opacity-0" ')
    
    new_class = f"group relative flex items-center justify-center w-[50px] h-[50px] {color_classes} text-white rounded-md shadow-sm transition overflow-hidden shrink-0"
    
    span_overlay = f'<span class="absolute inset-0 flex items-center justify-center bg-black/70 opacity-0 group-hover:opacity-100 transition-opacity duration-300 text-[10px] font-bold text-center leading-tight px-1 z-10">{text}</span>'
    
    # We reconstruct the anchor tag
    return f'<a href="{href}" target="_blank" rel="noopener noreferrer" class="{new_class}">\n            {svg}\n            {span_overlay}\n          </a>'

pattern = r'<a href="([^"]+)" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-1\.5 w-full py-1\.5 px-2 text-xs ([^"]+) text-white rounded-md shadow-sm transition font-bold">\s*(<svg.*?</svg>)\s*([^<]+)\s*</a>'

new_content = re.sub(pattern, replace_a_tag, new_content, flags=re.DOTALL)

with open('src/App.vue', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Replaced!")
