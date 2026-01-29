# Kitwe Green Space Mapping System - Version Information

## 📁 **File Structure:**

### **Static Demo Version (Current GitHub Pages):**
- `index.html` - Landing page with static statistics
- `frontend/index.html` - Main map application (STATIC VERSION for demo)
- All other pages work normally

### **Backend-Enabled Version (For Cloud Hosting):**
- `frontend/index-with-backend.html` - Original map application with full backend integration
- Contains API calls, real-time data loading, and dynamic features

## 🚀 **Deployment Instructions:**

### **For GitHub Pages (Current Setup):**
- Uses static fallback data (51 green spaces)
- No backend required
- Perfect for demonstration and portfolio
- Live at: https://zluyongile-dot.github.io/kitwe-green-spaces/

### **For Cloud Hosting (Railway, Heroku, etc.):**
1. Deploy backend using `backend/app.py`
2. Replace `frontend/index.html` with `frontend/index-with-backend.html`
3. Update API URLs in `frontend/config.js`
4. Full dynamic functionality with real database

## 🔄 **Switching Between Versions:**

### **To Enable Backend (when you get cloud hosting):**
```bash
# Backup current static version
copy frontend\index.html frontend\index-static-demo.html

# Restore backend version
copy frontend\index-with-backend.html frontend\index.html

# Update config.js with your cloud backend URL
# Deploy backend to your cloud platform
```

### **To Return to Static Demo:**
```bash
# Restore static demo version
copy frontend\index-static-demo.html frontend\index.html
```

## ✨ **Current Features (Static Demo):**
- ✅ Interactive map with 51 green spaces
- ✅ All filtering and search functionality
- ✅ Professional UI with iOS fonts
- ✅ Responsive design
- ✅ All documentation pages
- ✅ Environmental monitoring dashboard
- ✅ Advanced statistics
- ✅ Perfect for academic presentation

## 🔮 **Future Features (With Backend):**
- 🔄 Real-time data updates
- 📊 Dynamic statistics calculation
- 💾 Database integration
- 🔄 Live data refresh
- 📈 Real-time environmental monitoring
- 👥 User feedback system

---
**Note:** The static demo version is fully functional and perfect for showcasing your academic project. When you're ready for production with a backend, simply follow the cloud hosting instructions above.