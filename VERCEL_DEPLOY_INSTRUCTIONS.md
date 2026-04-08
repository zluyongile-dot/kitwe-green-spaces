# Deploy to Vercel - Quick Guide

## Current Status
- ✅ Code pushed to GitHub (commit: 0854a20)
- ✅ Vercel configuration file exists (vercel.json)
- ⏳ Waiting for Vercel deployment

## Option 1: Auto-Deployment (Recommended)

If your GitHub repo is connected to Vercel:

1. **Check Deployment Status**
   - Visit: https://vercel.com/dashboard
   - Find your project: `kitwe-green-spaces`
   - Look for latest deployment with commit `0854a20`
   - Status should change from "Building" → "Ready" (1-3 minutes)

2. **View Live Site**
   - Once "Ready", click the deployment URL
   - Your "Find Parks Near Me" feature will be live!

## Option 2: Manual Deployment via CLI

If auto-deployment isn't set up:

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy
```bash
# From project root directory
vercel --prod
```

### Step 4: Follow Prompts
- Set up and deploy: Yes
- Which scope: Select your account
- Link to existing project: Yes (if exists) or No (create new)
- Project name: kitwe-green-spaces
- Directory: ./
- Override settings: No

## Option 3: Connect GitHub to Vercel (First Time Setup)

If you haven't connected GitHub yet:

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/new

2. **Import Git Repository**
   - Click "Add New..." → "Project"
   - Select "Import Git Repository"
   - Choose: `zluyongile-dot/kitwe-green-spaces`

3. **Configure Project**
   - Framework Preset: Other
   - Root Directory: ./
   - Build Command: (leave empty)
   - Output Directory: frontend
   - Install Command: pip install -r requirements.txt

4. **Environment Variables**
   Add these if using Supabase:
   - `SUPABASE_URL`: Your Supabase project URL
   - `SUPABASE_KEY`: Your Supabase anon key
   - `DATABASE_URL`: Your Supabase connection string

5. **Deploy**
   - Click "Deploy"
   - Wait 1-3 minutes
   - Get your live URL!

6. **Enable Auto-Deployment**
   - Go to Project Settings → Git
   - Enable "Production Branch": main
   - Now every push to main auto-deploys!

## Verify Deployment

Once deployed, test the new feature:

1. **Visit your Vercel URL**
   - Example: https://kitwe-green-spaces.vercel.app

2. **Test "Find Parks Near Me"**
   - Click the button in the sidebar
   - Allow location permission
   - Verify nearest parks appear
   - Check distance calculations
   - Test zoom to park functionality

## Troubleshooting

### Deployment Failed
- Check build logs in Vercel dashboard
- Verify vercel.json is correct
- Ensure all files are committed to GitHub

### Feature Not Showing
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache
- Check if correct branch deployed
- Verify commit hash matches latest

### Geolocation Not Working
- Ensure site uses HTTPS (Vercel provides this automatically)
- Check browser permissions
- Test on different browsers

## Current Deployment Info

- **Latest Commit**: 0854a20
- **Branch**: main
- **Files Changed**: 3 (index.html files)
- **New Feature**: Find Parks Near Me with geolocation
- **Status**: ✅ Pushed to GitHub, waiting for Vercel

## Next Steps

1. Check Vercel dashboard for deployment status
2. Once "Ready", visit your live site
3. Test the new geolocation feature
4. Share the URL to see it in action!

---

**Need Help?**
- Vercel Docs: https://vercel.com/docs
- Vercel Support: https://vercel.com/support
