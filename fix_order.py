with open('src/App.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Grab the whole div after <!-- Social Buttons & Resources -->
start_str = "      <!-- Social Buttons & Resources -->\n      <div class=\"mt-6 mb-2\">"

idx = content.find(start_str)

if idx != -1:
    end_idx = content.find("      </div>", idx) + len("      </div>")
    block = content[idx:end_idx]
    
    # Inside the block, there is `<div class="grid grid-cols-2 gap-2 mb-4">`
    buttons_start = block.find('<div class="grid grid-cols-2')
    buttons_end = block.find('</div>', buttons_start) + len('</div>')
    buttons = block[buttons_start:buttons_end]
    
    resources_start = block.find('<h3 class="text-xs focus') # Wait I'll just split by <h3
    resources_start = block.find('<h3 class="text-xs font-bold')
    resources_end = block.find('</ul>', resources_start) + len('</ul>')
    resources = block[resources_start:resources_end]
    
    # We want resources first then buttons
    # Also adjust spacing classes
    new_resources = resources.replace('mb-3 mt-6', 'mb-3') # remove top margin if it's first
    new_buttons = buttons.replace('mb-4', 'mt-6 mb-4') # add top margin to buttons
    
    new_block = start_str + "\n        " + new_resources + "\n        " + new_buttons + "\n      </div>"
    
    content = content[:idx] + new_block + content[end_idx:]
    with open('src/App.vue', 'w', encoding='utf-8') as f:
        f.write(content)
