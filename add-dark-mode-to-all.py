"""
Script to add dark mode to all HTML pages
Adds CSS link, toggle button, and JavaScript to each page
"""

import os
import re

# Pages to update (excluding home.html and index.html which are already done)
PAGES = [
    'simpledashboard.html',
    'advanced-stats.html',
    'environmental-monitoring.html',
    'report-generator.html',
    'feedback.html',
    'about-green-spaces.html',
    'documentation.html',
    'bibliography.html',
    'admin-portal.html',
    'admindashboard.html',
]

FRONTEND_DIR = 'frontend'

# CSS link to add in <head>
CSS_LINK = '''    
    <!-- Dark Mode CSS -->
    <link rel="stylesheet" href="dark-mode.css">'''

# Toggle button HTML
TOGGLE_BUTTON = '''                    <li class="nav-item">
                        <button id="darkModeToggle" class="btn btn-link nav-link" aria-label="Toggle dark mode">
                            <i class="fas fa-moon"></i>
                            <i class="fas fa-sun hidden"></i>
                        </button>
                    </li>'''

# JavaScript to add before </body>
JS_SCRIPT = '''    
    <!-- Dark Mode Script -->
    <script src="dark-mode.js"></script>'''

def add_dark_mode_to_page(filepath):
    """Add dark mode to a single page"""
    print(f"\n📄 Processing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # 1. Add CSS link in <head> if not already present
        if 'dark-mode.css' not in content:
            # Find a good place to insert (after other CSS links)
            if '<link rel="stylesheet"' in content:
                # Insert after the last stylesheet link
                pattern = r'(<link rel="stylesheet"[^>]*>)(?!.*<link rel="stylesheet")'
                content = re.sub(pattern, r'\1' + CSS_LINK, content, count=1)
                changes_made.append('✅ Added CSS link')
            elif '</head>' in content:
                # Fallback: insert before </head>
                content = content.replace('</head>', CSS_LINK + '\n</head>')
                changes_made.append('✅ Added CSS link (before </head>)')
        else:
            print('   ⏭️  CSS already present')
        
        # 2. Add toggle button if not already present
        if 'darkModeToggle' not in content:
            # Try to find navigation list
            if '</ul>' in content and '<nav' in content:
                # Find the last </ul> in navigation
                nav_match = re.search(r'<nav[^>]*>.*?</nav>', content, re.DOTALL)
                if nav_match:
                    nav_content = nav_match.group(0)
                    # Find last </ul> in nav
                    last_ul_pos = nav_content.rfind('</ul>')
                    if last_ul_pos != -1:
                        # Insert button before </ul>
                        new_nav = nav_content[:last_ul_pos] + TOGGLE_BUTTON + '\n' + nav_content[last_ul_pos:]
                        content = content.replace(nav_match.group(0), new_nav)
                        changes_made.append('✅ Added toggle button')
        else:
            print('   ⏭️  Toggle button already present')
        
        # 3. Add JavaScript before </body> if not already present
        if 'dark-mode.js' not in content:
            if '</body>' in content:
                content = content.replace('</body>', JS_SCRIPT + '\n</body>')
                changes_made.append('✅ Added JavaScript')
        else:
            print('   ⏭️  JavaScript already present')
        
        # Write back if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'   {" | ".join(changes_made)}')
            return True
        else:
            print('   ℹ️  No changes needed')
            return False
            
    except Exception as e:
        print(f'   ❌ Error: {e}')
        return False

def main():
    print("=" * 70)
    print("🌙 Adding Dark Mode to All Pages")
    print("=" * 70)
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for page in PAGES:
        filepath = os.path.join(FRONTEND_DIR, page)
        
        if not os.path.exists(filepath):
            print(f"\n📄 {page}")
            print(f'   ⚠️  File not found, skipping')
            skipped_count += 1
            continue
        
        if add_dark_mode_to_page(filepath):
            updated_count += 1
        else:
            skipped_count += 1
    
    print("\n" + "=" * 70)
    print("📊 Summary")
    print("=" * 70)
    print(f"✅ Updated: {updated_count} pages")
    print(f"⏭️  Skipped: {skipped_count} pages")
    print(f"❌ Errors: {error_count} pages")
    print("\n🎉 Dark mode implementation complete!")
    print("\n💡 Next steps:")
    print("   1. Refresh any open pages")
    print("   2. Click the moon/sun icon to toggle dark mode")
    print("   3. Preference will be saved across all pages")

if __name__ == '__main__':
    main()
