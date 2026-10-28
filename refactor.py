import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the workspace section
start_workspace = html.find('<!-- Interactive Digital Workspace About Me Section -->')
end_workspace = html.find('</div> <!-- end world-container -->')

if start_workspace == -1 or end_workspace == -1:
    print('Could not find workspace section boundaries')
    sys.exit(1)

workspace_html = html[start_workspace:end_workspace]

# Extract just the .workspace-desk
desk_start = workspace_html.find('<div class="workspace-desk">')
desk_end = workspace_html.rfind('</div>\n  </section>')

if desk_start == -1 or desk_end == -1:
    print('Could not find workspace-desk boundaries')
    sys.exit(1)

desk_content = workspace_html[desk_start:desk_end + 6] # including closing </div> of desk

# Remove the whole workspace section
new_html = html[:start_workspace] + '\n' + html[end_workspace:]

# Create the about card html
about_card = f'''
        <!-- 🧑‍💻 About Card -->
        <div class="floating-card about-card" data-card="about" style="--card-index: 7;" id="about-card-element">
          <div class="card-bobber">
            <div class="card-glow" style="background: radial-gradient(circle, rgba(135, 206, 235, 0.4) 0%, transparent 70%);"></div>
            <div class="card-inner">
              <div class="icon-wrapper">
                <svg class="icon-svg 3d-object" viewBox="0 0 24 24" fill="none" stroke="#2d3748" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <div class="card-info">
                <h3>About Me</h3>
                <p>Digital Workspace</p>
              </div>
            </div>
            <div class="card-detail-content">
              <div style="transform: scale(0.4); transform-origin: center center; position: absolute; width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center;">
                {desk_content}
              </div>
            </div>
          </div>
        </div>
'''

# Insert it right before the end of floating-icons-container
# The end of floating-icons-container is just before <div class="hero-titles">
insert_pos = new_html.find('      </div>\n\n    </div>\n\n    <!-- Title and Subtitle -->')

final_html = new_html[:insert_pos] + about_card + new_html[insert_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Updated index.html successfully')
