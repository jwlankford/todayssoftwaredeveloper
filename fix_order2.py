import re

with open('src/App.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Grab the whole div after <!-- Social Buttons & Resources -->
start_str = "      <!-- Social Buttons & Resources -->\n      <div class=\"mt-6 mb-2\">"

idx = content.find(start_str)

if idx != -1:
    end_idx = content.find("      </div>\n    </aside>", idx) + len("      </div>")
    block = content[idx:end_idx]
    
    # We want to extract buttons div and resources separately
    # Assuming <div class="grid grid-cols-2 gap-2 mb-4"> is the buttons
    
    buttons_match = re.search(r'(<div class="grid grid-cols-2.*?</div>\n        </div>)', block, re.DOTALL)
    if buttons_match:
        buttons = buttons_match.group(1)
        
        # Now find the resources
        res_match = re.search(r'(<h3 class="text-xs font-bold uppercase.*?</ul>)', block, re.DOTALL)
        if res_match:
            resources = res_match.group(1)
            
            # Reconstruct
            new_block = start_str + "\n        " + resources.replace('mb-3 mt-6', 'mb-3') + "\n\n        " + buttons.replace('mb-4', 'mt-6 mb-4') + "\n      </div>"
            
            content = content[:idx] + new_block + content[end_idx:]
            with open('src/App.vue', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully swapped")
        else:
            print("res_match not found")
    else:
        print("buttons_match not found")
