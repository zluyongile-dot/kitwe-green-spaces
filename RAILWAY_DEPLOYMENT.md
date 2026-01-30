# 🚂 Railway Deployment Guide - Super Simple!

## 🎯 **Why Railway?**
- ✅ **$5 free credit** for new users (lasts months for academic projects)
- ✅ **500 hours/month** execution time
- ✅ **Free PostgreSQL database** included
- ✅ **Auto-deploy** from GitHub
- ✅ **No credit card required** for trial
- ✅ **Much easier than AWS!**

---

## 🚀 **5-Minute Deployment**

### **Step 1: Go to Railway**
1. Visit: https://railway.app
2. Click "Start a New Project"
3. Sign up with your GitHub account

### **Step 2: Deploy from GitHub**
1. Click "Deploy from GitHub repo"
2. Select your `kitwe-green-spaces` repository
3. Railway will automatically detect it's a Python Flask app

### **Step 3: Add PostgreSQL Database**
1. In your project dashboard, click "New Service"
2. Select "Database" → "PostgreSQL"
3. Railway will create and connect the database automatically

### **Step 4: Configure Environment Variables**
Railway will auto-set most variables, but you can add:
- `FLASK_ENV=production`
- `SECRET_KEY=your-secret-key`

### **Step 5: Deploy!**
- Railway automatically builds and deploys your app
- You'll get a URL like: `https://kitwe-green-spaces.up.railway.app`

---

## 🔧 **Project Configuration**

Your project already has the right files:
- ✅ `railway.json` - Railway configuration
- ✅ `requirements.txt` - Python dependencies  
- ✅ `gunicorn.conf.py` - Production server config
- ✅ `application.py` - Entry point

---

## 📱 **After Deployment**

### **Update Frontend Config**
Once deployed, update your frontend to use the Railway URL:

```bash
python update_backend_url.py https://your-app-name.up.railway.app
```

### **Push to GitHub**
```bash
git add .
git commit -m "Connected to Railway backend"
git push origin main
```

Your GitHub Pages site will automatically use the live Railway backend!

---

## 💰 **Cost Breakdown**
- **First 30 days**: Completely FREE with $5 credit
- **After trial**: ~$0.50-2.00/month for academic projects
- **Database**: FREE PostgreSQL included
- **Perfect for**: Student portfolios and academic projects

---

## 🎉 **Final Result**
- **Frontend**: `https://zluyongile-dot.github.io/kitwe-green-spaces/`
- **Backend**: `https://your-app.up.railway.app`
- **Database**: PostgreSQL with your 51 green spaces
- **Total setup time**: 5-10 minutes!

Much easier than AWS! 🎊