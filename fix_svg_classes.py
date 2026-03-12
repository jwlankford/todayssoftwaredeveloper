import re

with open('src/App.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <svg class="..." ... class="..."> with single class
def merge_classes(match):
    class1 = match.group(1)
    # The rest of attributes until the second class
    middle = match.group(2)
    class2 = match.group(3)
    
    return f'<svg class="{class1} {class2}" {middle}'

pattern = r'<svg class="([^"]+)" (xmlns="[^"]+") class="([^"]+)"'
new_content = re.sub(pattern, merge_classes, content)

with open('src/App.vue', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Fixed SVG classes")
