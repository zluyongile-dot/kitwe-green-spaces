#!/usr/bin/env python3
"""
Complete Vercel + Supabase Deployment Script
This will set up everything for you!
"""

import webbrowser
import os

def deploy_to_vercel_supabase():
    print("🚀 Vercel + Supabase Deployment - Real Database!")
    print("=" * 50)
    
    print("\n📋 What we've set up for you:")
    print("✅ Vercel-compatible Flask API (api/index.py)")
    print("✅ PostgreSQL driver that works with Vercel (pg8000)")
    print("✅ Supabase database setup script (supabase_setup.sql)")
    print("✅ Updated vercel.json configuration")
    print("✅ Requirements.txt without problematic dependencies")
    
    print("\n🎯 Step 1: Set up Supabase Database")
    print("1. Go to: https://supabase.com")
    print("2. Sign up with GitHub")
    print("3. Create new project: 'kitwe-green-spaces'")
    print("4. Choose region: 'East US' (closest to Vercel)")
    print("5. Wait 2 minutes for database setup")
    
    open_supabase = input("\n🌐 Open Supabase in browser? (y/n): ").lower().strip()
    if open_supabase == 'y':
        webbrowser.open('https://supabase.com')
    
    print("\n🎯 Step 2: Run Database Setup")
    print("1. In Supabase, go to 'SQL Editor'")
    print("2. Copy and paste the contents of 'supabase_setup.sql'")
    print("3. Click 'Run' - this will create your table and insert all 51 green spaces")
    
    print("\n🎯 Step 3: Get Database Connection String")
    print("1. In Supabase, go to Settings → Database")
    print("2. Copy the 'Connection string' (URI format)")
    print("3. It looks like: postgresql://postgres:[password]@[host]:5432/postgres")
    
    print("\n🎯 Step 4: Deploy to Vercel")
    print("1. Go to: https://vercel.com")
    print("2. Sign up with GitHub")
    print("3. Import your 'kitwe-green-spaces' repository")
    print("4. In Environment Variables, add:")
    print("   - DATABASE_URL = [your Supabase connection string]")
    print("   - FLASK_ENV = production")
    print("5. Deploy!")
    
    open_vercel = input("\n🌐 Open Vercel in browser? (y/n): ").lower().strip()
    if open_vercel == 'y':
        webbrowser.open('https://vercel.com')
    
    print("\n🎉 After Deployment:")
    print("- Frontend: https://your-project.vercel.app")
    print("- API: https://your-project.vercel.app/api/green-spaces")
    print("- Test: https://your-project.vercel.app/test-db")
    
    print("\n💡 Why This Setup is Perfect:")
    print("✅ Real PostgreSQL database (not static!)")
    print("✅ Serverless - scales automatically")
    print("✅ Free - both platforms have generous free tiers")
    print("✅ Fast - global CDN and edge functions")
    print("✅ Professional - production-ready architecture")
    print("✅ Easy - auto-deploy from GitHub")
    
    print("\n📊 Your Database Will Have:")
    print("- 51 green spaces across Kitwe")
    print("- 261.5 hectares total area")
    print("- 16 different wards")
    print("- 7 different green space types")
    print("- Real environmental calculations")
    
    print("\n🔧 Troubleshooting:")
    print("- If deployment fails, check Vercel logs")
    print("- Ensure DATABASE_URL is correctly set")
    print("- Test database connection with /test-db endpoint")
    
    return True

def commit_and_push():
    """Commit changes and push to GitHub"""
    print("\n📝 Committing changes to GitHub...")
    
    try:
        import subprocess
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit
        subprocess.run(['git', 'commit', '-m', 'Add Vercel + Supabase deployment setup'], check=True)
        
        # Push
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        
        print("✅ Changes pushed to GitHub successfully!")
        print("🚀 Now you can deploy on Vercel!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")
        print("💡 Please commit and push manually:")
        print("   git add .")
        print("   git commit -m 'Add Vercel + Supabase setup'")
        print("   git push origin main")

if __name__ == "__main__":
    print("🌳 Kitwe Green Spaces - Vercel + Supabase Deployment")
    
    deploy_to_vercel_supabase()
    
    push_changes = input("\n📤 Push changes to GitHub now? (y/n): ").lower().strip()
    if push_changes == 'y':
        commit_and_push()
    
    print("\n📚 For detailed instructions, check: VERCEL_SUPABASE_SETUP.md")
    print("🎊 Your project will have a real database and professional hosting!")