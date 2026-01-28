# 🆓 Open Source Hosting Guide - Kitwe Green Space Mapping System

## 🌟 **Best Free Hosting Combinations**

### **Option 1: GitHub Pages + Railway (100% Free)**

#### **Frontend: GitHub Pages (Free Forever)**
1. **Create GitHub Repository:**
   ```bash
   # Create new repo on GitHub: kitwe-green-spaces
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/kitwe-green-spaces.git
   git push -u origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repo → Settings → Pages
   - Source: Deploy from a branch
   - Branch: main → /frontend folder
   - Your site will be at: `https://yourusername.github.io/kitwe-green-spaces`

#### **Backend: Railway.app (Free Tier)**
- 500 hours/month free (enough for academic projects)
- Free PostgreSQL database
- Auto-deployment from GitHub

---

### **Option 2: Netlify + Supabase (100% Free)**

#### **Frontend: Netlify (Free)**
- Unlimited static sites
- Custom domains
- Automatic deployments

#### **Backend: Supabase (Free)**
- PostgreSQL database with 500MB storage
- Built-in API
- Real-time features

---

### **Option 3: Vercel + PlanetScale (Free)**

#### **Frontend: Vercel (Free)**
- Unlimited static deployments
- Edge network
- Custom domains

#### **Backend: PlanetScale (Free)**
- MySQL database (5GB storage)
- Serverless architecture

---

## 🚀 **Quick Setup: GitHub Pages + Railway**

### **Step 1: Prepare Your Repository**

1. **Create .github/workflows/deploy.yml:**
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '16'
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./frontend
```

2. **Update package.json (optional):**
```json
{
  "name": "kitwe-green-spaces",
  "version": "1.0.0",
  "description": "Interactive GIS mapping system for Kitwe green spaces",
  "scripts": {
    "start": "python backend/app.py",
    "deploy": "echo 'Deploying to GitHub Pages'"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/yourusername/kitwe-green-spaces.git"
  },
  "author": "Mukendwa Luyongile",
  "license": "MIT"
}
```

### **Step 2: Deploy Backend to Railway**

1. **Go to [railway.app](https://railway.app)**
2. **Connect GitHub repository**
3. **Add PostgreSQL service**
4. **Environment variables will be auto-configured**

### **Step 3: Update Frontend Configuration**

Update `frontend/config.js`:
```javascript
const CONFIG = {
    production: {
        API_BASE_URL: 'https://your-project-name.up.railway.app'
    },
    local: {
        API_BASE_URL: 'http://127.0.0.1:5000'
    }
};

// Auto-detect environment
const isLocal = window.location.hostname === 'localhost' || 
                window.location.hostname === '127.0.0.1';

window.APP_CONFIG = isLocal ? CONFIG.local : CONFIG.production;
```

---

## 🌐 **Alternative: Completely Free Stack**

### **Frontend: GitHub Pages**
- **Cost**: $0 forever
- **Features**: Custom domains, HTTPS, CDN
- **Limitations**: Static sites only

### **Backend: Render.com (Free Tier)**
- **Cost**: $0 for 750 hours/month
- **Features**: PostgreSQL included, auto-deploy
- **Limitations**: Sleeps after 15 minutes of inactivity

### **Database: ElephantSQL (Free)**
- **Cost**: $0 for 20MB PostgreSQL
- **Features**: Managed PostgreSQL
- **Perfect for**: Academic projects

---

## 📊 **Free Hosting Comparison**

| Platform | Frontend | Backend | Database | Custom Domain | SSL |
|----------|----------|---------|----------|---------------|-----|
| **GitHub Pages + Railway** | ✅ Free | ✅ 500h/month | ✅ PostgreSQL | ✅ Yes | ✅ Yes |
| **Netlify + Supabase** | ✅ Free | ✅ Free | ✅ 500MB | ✅ Yes | ✅ Yes |
| **Vercel + PlanetScale** | ✅ Free | ✅ Serverless | ✅ 5GB MySQL | ✅ Yes | ✅ Yes |
| **Render + ElephantSQL** | ✅ Free | ✅ 750h/month | ✅ 20MB | ✅ Yes | ✅ Yes |

---

## 🛠️ **Setup Commands**

### **Initialize Git Repository:**
```bash
git init
git add .
git commit -m "Kitwe Green Spaces - Academic Project"
git branch -M main
git remote add origin https://github.com/yourusername/kitwe-green-spaces.git
git push -u origin main
```

### **Create GitHub Pages:**
```bash
# Create gh-pages branch for deployment
git checkout -b gh-pages
git push origin gh-pages
```

---

## 🔧 **Configuration Files for Open Source Hosting**

### **1. GitHub Actions Workflow (.github/workflows/pages.yml):**
```yaml
name: Deploy GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Pages
        uses: actions/configure-pages@v2
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: './frontend'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```

### **2. Netlify Configuration (_redirects in frontend/):**
```
/*    /index.html   200
```

### **3. Vercel Configuration (vercel.json):**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "frontend/**/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/frontend/$1"
    }
  ]
}
```

---

## 🎯 **Recommended Setup for Academic Projects**

### **Best Choice: GitHub Pages + Railway**

**Why this combination:**
- ✅ **100% Free** for academic use
- ✅ **Professional URLs** (github.io domain)
- ✅ **Full PostgreSQL database**
- ✅ **Automatic deployments**
- ✅ **No credit card required**
- ✅ **Perfect for portfolios**

**Your final URLs:**
- **Website**: `https://yourusername.github.io/kitwe-green-spaces`
- **API**: `https://kitwe-backend.up.railway.app`
- **Documentation**: `https://yourusername.github.io/kitwe-green-spaces/documentation.html`

---

## 🚀 **Quick Start (5 Minutes)**

1. **Create GitHub repo** with your project files
2. **Enable GitHub Pages** in repo settings
3. **Deploy backend** to Railway.app
4. **Update API URL** in config.js
5. **Push changes** to GitHub

**Result**: Your academic project is live and accessible worldwide!

---

## 💡 **Pro Tips for Academic Projects**

1. **Use descriptive repository names**: `kitwe-green-spaces-gis`
2. **Add comprehensive README.md**
3. **Include your student details** in documentation
4. **Use semantic versioning** for releases
5. **Document your deployment process**

---

## 🆘 **Troubleshooting**

### **GitHub Pages not updating:**
- Check Actions tab for deployment status
- Ensure frontend folder structure is correct
- Clear browser cache

### **API CORS errors:**
- Add your GitHub Pages URL to Flask-CORS
- Update allowed origins in backend

### **Database connection issues:**
- Check Railway environment variables
- Verify PostgreSQL service is running
- Test API endpoints directly

---

**🎉 Your academic project will be live at zero cost and accessible from anywhere!**