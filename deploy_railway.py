#!/usr/bin/env python3
"""
Railway Deployment Helper Script
Much simpler than AWS!
"""

import os
import subprocess
import webbrowser

def deploy_to_railway():
    print("🚂 Railway Deployment - Super Simple!")
    print("=" * 40)
    
    print("\n📋 Pre-deployment checklist:")
    
    # Check if files exist
    required_files = [
        'railway.json',
        'requirements.txt', 
        'backend/app.py',
        'gunicorn.conf.py'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {', '.join(missing_files)}")
        print("Please ensure all required files are present.")
        return False
    
    print("\n🎯 Deployment Steps:")
    print("1. Go to: https://railway.app")
    print("2. Sign up with GitHub")
    print("3. Click 'Deploy from GitHub repo'")
    print("4. Select your 'kitwe-green-spaces' repository")
    print("5. Add PostgreSQL database service")
    print("6. Your app will be live in 2-3 minutes!")
    
    # Open Railway in browser
    open_browser = input("\n🌐 Open Railway.app in browser? (y/n): ").lower().strip()
    if open_browser == 'y':
        webbrowser.open('https://railway.app')
    
    print("\n📱 After deployment:")
    print("1. Copy your Railway app URL")
    print("2. Run: python update_backend_url.py https://your-app.up.railway.app")
    print("3. git add . && git commit -m 'Connected to Railway' && git push")
    
    print("\n🎉 Your app will be live with:")
    print("- Frontend: GitHub Pages")
    print("- Backend: Railway")
    print("- Database: PostgreSQL")
    print("- Cost: FREE for academic use!")
    
    return True

def check_git_status():
    """Check if changes need to be committed"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        if result.stdout.strip():
            print("\n📝 You have uncommitted changes:")
            print("Run these commands first:")
            print("git add .")
            print("git commit -m 'Prepare for Railway deployment'")
            print("git push origin main")
            return False
        return True
    except subprocess.CalledProcessError:
        print("⚠️  Not a git repository or git not available")
        return True

if __name__ == "__main__":
    print("🌳 Kitwe Green Spaces - Railway Deployment")
    
    if not check_git_status():
        print("\n💡 Commit your changes first, then run this script again.")
    else:
        deploy_to_railway()
        
    print("\n📚 Need help? Check RAILWAY_DEPLOYMENT.md")