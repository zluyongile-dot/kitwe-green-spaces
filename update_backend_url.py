#!/usr/bin/env python3
"""
Quick script to update backend URL in config files
Usage: python update_backend_url.py https://your-aws-url.elasticbeanstalk.com
"""
import sys
import os

def update_backend_url(new_url):
    if not new_url.startswith('https://') and not new_url.startswith('http://'):
        print("❌ Error: URL must start with https:// or http://")
        return False
    
    files_to_update = [
        ('frontend/config.js', 'YOUR_ACTUAL_RAILWAY_URL_HERE'),
        ('frontend/config.js', 'https://YOUR_ACTUAL_RAILWAY_URL_HERE'),
        ('index.html', 'YOUR_ACTUAL_RAILWAY_URL_HERE'),
        ('index.html', 'https://YOUR_ACTUAL_RAILWAY_URL_HERE')
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
                    
                    if file_path not in [f[0] for f in updated_files]:
                        updated_files.append((file_path, placeholder))
                    print(f"✅ Updated {file_path}")
                else:
                    print(f"⚠️  Placeholder '{placeholder}' not found in {file_path}")
            except Exception as e:
                print(f"❌ Error updating {file_path}: {e}")
        else:
            print(f"❌ File not found: {file_path}")
    
    if updated_files:
        print(f"\n🎉 Successfully updated {len(updated_files)} files!")
        print(f"� Backend URL set to: {new_url}")
        print("\n�📝 Next steps:")
        print("   1. Test your backend: curl " + new_url + "/test-db")
        print("   2. git add .")
        print("   3. git commit -m 'Connected to AWS backend'")
        print("   4. git push origin main")
        print("   5. Wait 2-3 minutes for GitHub Pages to update")
        print(f"   6. Visit: https://zluyongile-dot.github.io/kitwe-green-spaces/")
        return True
    else:
        print("❌ No files were updated")
        return False

def restore_backend_version():
    """Restore the backend-enabled version of index.html"""
    if os.path.exists('frontend/index-with-backend.html'):
        try:
            # Backup current static version
            if os.path.exists('frontend/index.html'):
                os.rename('frontend/index.html', 'frontend/index-static-demo.html')
                print("✅ Backed up static demo version to index-static-demo.html")
            
            # Restore backend version
            with open('frontend/index-with-backend.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            with open('frontend/index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Restored backend-enabled version of index.html")
            print("🔄 Now run: python update_backend_url.py https://your-aws-url")
            return True
        except Exception as e:
            print(f"❌ Error restoring backend version: {e}")
            return False
    else:
        print("❌ Backend version (index-with-backend.html) not found")
        return False

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '--restore-backend':
        restore_backend_version()
    elif len(sys.argv) != 2:
        print("Usage: python update_backend_url.py https://your-aws-url.elasticbeanstalk.com")
        print("   Or: python update_backend_url.py --restore-backend")
        print("\nExamples:")
        print("   python update_backend_url.py https://kitwe-production.us-east-1.elasticbeanstalk.com")
        print("   python update_backend_url.py https://your-railway-app.railway.app")
        print("   python update_backend_url.py --restore-backend")
        sys.exit(1)
    else:
        backend_url = sys.argv[1].rstrip('/')  # Remove trailing slash
        update_backend_url(backend_url)