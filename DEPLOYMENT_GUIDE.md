# 🚀 Deployment Guide - Kitwe Green Space Mapping System

## 📋 Quick Deployment (Recommended for Academic Projects)

### **Step 1: Deploy Backend (Railway.app)**

1. **Create Railway Account:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy Backend:**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect Python and deploy
   - Add PostgreSQL database: "Add Service" → "Database" → "PostgreSQL"

3. **Configure Environment:**
   - In Railway dashboard, go to your app settings
   - Add environment variables:
     ```
     DATABASE_URL=postgresql://username:password@host:port/database
     PORT=8000
     ```
   - Railway will provide the DATABASE_URL automatically

4. **Get Your Backend URL:**
   - After deployment, you'll get a URL like: `https://your-app-name.railway.app`
   - Test it: `https://your-app-name.railway.app/test-db`

### **Step 2: Deploy Frontend (Netlify)**

1. **Update Configuration:**
   - Edit `frontend/config.js`
   - Replace `your-backend-url.railway.app` with your actual Railway URL

2. **Deploy to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Drag and drop your `frontend/` folder
   - Or connect GitHub for automatic deployments

3. **Get Your Website URL:**
   - Netlify gives you a URL like: `https://amazing-project-name.netlify.app`
   - You can customize the subdomain in settings

### **Step 3: Initialize Database**

1. **Visit your backend URL:**
   - `https://your-backend-url.railway.app/create-green-spaces-table`
   - `https://your-backend-url.railway.app/add-sample-green-spaces`
   - `https://your-backend-url.railway.app/create-feedback-table`

2. **Test the API:**
   - `https://your-backend-url.railway.app/api/green-spaces`

---

## 🌐 Alternative Deployment Options

### **Option 1: Vercel (Frontend) + Railway (Backend)**
- **Vercel**: Better for React/Next.js but works with static sites
- **Railway**: Same as above for backend

### **Option 2: Heroku (Full Stack)**
- **Pros**: Single platform for both frontend and backend
- **Cons**: No longer has free tier

### **Option 3: GitHub Pages (Frontend Only)**
- **Limitation**: Only static sites, need separate backend hosting
- **Good for**: Portfolio/demo purposes

---

## 🔧 Configuration Files Explained

### **requirements.txt**
```txt
Flask==2.3.3
psycopg2-binary==2.9.7
Flask-CORS==4.0.0
Werkzeug==2.3.7
gunicorn==21.2.0
```
- Lists all Python dependencies for deployment

### **Procfile**
```
web: gunicorn --chdir backend app:app
```
- Tells the hosting service how to start your app

### **railway.json**
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn --chdir backend app:app",
    "healthcheckPath": "/test-db"
  }
}
```
- Railway-specific configuration

### **netlify.toml**
```toml
[build]
  publish = "frontend"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```
- Netlify configuration for single-page applications

---

## 📱 Mobile-Friendly Features

Your app is already mobile-responsive with:
- ✅ Bootstrap 5 responsive design
- ✅ Touch-friendly controls
- ✅ Mobile-optimized sidebar
- ✅ Responsive charts and maps

---

## 🔒 Security Considerations

For production deployment:

1. **Environment Variables:**
   ```python
   import os
   DB_CONFIG = {
       "dbname": os.environ.get('DB_NAME', 'kitwe_green_spaces'),
       "user": os.environ.get('DB_USER', 'postgres'),
       "password": os.environ.get('DB_PASSWORD', 'your_password'),
       "host": os.environ.get('DB_HOST', 'localhost'),
       "port": os.environ.get('DB_PORT', '5432')
   }
   ```

2. **CORS Configuration:**
   - Update allowed origins in your Flask app
   - Restrict to your frontend domain

3. **HTTPS:**
   - Both Railway and Netlify provide HTTPS automatically

---

## 🎯 Final Steps

1. **Deploy Backend** → Get Railway URL
2. **Update Frontend Config** → Add Railway URL
3. **Deploy Frontend** → Get Netlify URL
4. **Initialize Database** → Run setup endpoints
5. **Test Everything** → Verify all features work
6. **Share Your URL** → `https://your-project.netlify.app`

---

## 💡 Pro Tips

1. **Custom Domain**: Both platforms support custom domains
2. **Environment Variables**: Use them for sensitive data
3. **Monitoring**: Railway provides logs and metrics
4. **Backups**: Export your data regularly
5. **Updates**: Connect GitHub for automatic deployments

---

## 🆘 Troubleshooting

### **Common Issues:**

1. **CORS Errors:**
   - Update Flask-CORS configuration
   - Add your frontend domain to allowed origins

2. **Database Connection:**
   - Check DATABASE_URL environment variable
   - Ensure PostgreSQL service is running

3. **API Not Loading:**
   - Verify backend URL in config.js
   - Check browser console for errors

4. **Charts Not Showing:**
   - Ensure Chart.js is loading
   - Check for JavaScript errors

---

**🎉 Once deployed, your academic project will be accessible worldwide at your custom URL!**

Example final URLs:
- **Frontend**: `https://kitwe-green-spaces.netlify.app`
- **Backend API**: `https://kitwe-backend.railway.app`
- **Documentation**: `https://kitwe-green-spaces.netlify.app/documentation.html`