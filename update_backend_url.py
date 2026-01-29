#!/usr/bin/env python3
"""
Quick script to update backend URL in config files
Usage: python update_backend_url.py https://your-railway-url.railway.app
"""
import sys
import os

def update_backend_url(new_url):
    if not new_url.startswith('https://'):
        print("❌ Error: URL must start with https://")
        return False
    
    files_to_update = [
        ('frontend/config.js', 'YOUR_ACTUAL_RAILWAY_URL_HERE'),
        ('index.html', 'YOUR_ACTUAL_RAILWAY_URL_HERE')
    ]
    
    updated_files = []
    
    for file_path, placeholder in files_to_update:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if placeholder in content:
                    updated_content = content.replace(placeholder, new_url)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    
                    updated_files.append(file_path)
                    print(f"✅ Updated {file_path}")
                else:
                    print(f"⚠️  Placeholder not found in {file_path}")
            except Exception as e:
                print(f"❌ Error updating {file_path}: {e}")
        else:
            print(f"❌ File not found: {file_path}")
    
    if updated_files:
        print(f"\n🎉 Successfully updated {len(updated_files)} files!")
        print("📝 Next steps:")
        print("   1. git add .")
        print("   2. git commit -m 'Updated backend URL'")
        print("   3. git push origin main")
        return True
    else:
        print("❌ No files were updated")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_backend_url.py https://your-railway-url.railway.app")
        print("Example: python update_backend_url.py https://kitwe-green-spaces-production-abc123.railway.app")
        sys.exit(1)
    
    railway_url = sys.argv[1].rstrip('/')  # Remove trailing slash
    update_backend_url(railway_url)