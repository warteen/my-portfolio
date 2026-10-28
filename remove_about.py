import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove About card
start = html.find('<!-- 🧑‍💻 About Card -->')
if start != -1:
    end_card = html.find('      </div>\n\n    </div>\n\n    <!-- Title and Subtitle -->', start)
    if end_card != -1:
        html = html[:start] + html[end_card:]
        print('Removed About card')

# Remove About from navbar
nav_about = '<li><a href="#about">About</a></li>'
if nav_about in html:
    html = html.replace(nav_about, '')
    print('Removed About from navbar')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
