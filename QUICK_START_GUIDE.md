# Quick Start Guide - Kitwe Green Spaces

## 🎉 Backend is Fixed and Running!

All backend database connection issues have been resolved. Your application is now fully functional.

---

## Current Status

### ✅ Backend Server
- **Status**: Running
- **URL**: http://127.0.0.1:5000
- **Database**: Connected to PostgreSQL (kitwe_green_spaces)
- **Green Spaces**: 35 locations loaded

### ✅ Fixed Issues
1. Removed duplicate API routes (was causing 500 errors)
2. Added missing `/api/dashboard/recent-activity` endpoint
3. Added `/create-environmental-table` endpoint
4. Updated dashboard stats to include all required fields
5. Improved error handling for all endpoints

---

## How to Access Your Application

### Option 1: Open HTML Files Directly
Simply open these files in your browser:

1. **Main Map** (with 35 green spaces)
   ```
   frontend/index.html
   ```

2. **Admin Portal** (comprehensive dashboard)
   ```
   frontend/admin-portal.html
   ```

3. **Feedback Form**
   ```
   frontend/feedback.html
   ```

4. **Other Dashboards**
   - `frontend/simpledashboard.html` - Simple statistics
   - `frontend/admindashboard-new.html` - Admin feedback management
   - `frontend/council-new.html` - Council dashboard
   - `frontend/environmental-monitoring-new.html` - Environmental data

### Option 2: Use a Local Web Server (Recommended)
For better CORS handling, serve the frontend through a web server:

```bash
# Using Python's built-in server
cd frontend
python -m http.server 8000
```

Then open: http://localhost:8000/index.html

---

## Testing the Application

### 1. Test the Map
Open `frontend/index.html` in your browser. You should see:
- ✅ Interactive map of Kitwe
- ✅ 35 green spaces displayed as markers
- ✅ Click markers to see details
- ✅ Search and filter functionality

### 2. Test the Admin Portal
Open `frontend/admin-portal.html` in your browser. You should see:
- ✅ Statistics cards showing:
  - Total Green Spaces: 35
  - Total Feedback: 0
  - Environmental Records: 0
  - Total Visitors: 0
- ✅ Recent Activity section
- ✅ Tabs for Feedback, Green Spaces, Environmental Data

### 3. Test Feedback Submission
Open `frontend/feedback.html` and submit test feedback:
- Fill out the form
- Submit
- Check `frontend/admindashboard-new.html` to see the feedback

---

## API Endpoints Reference

### Green Spaces
```
GET  /api/green-spaces              - Get all green spaces (GeoJSON)
POST /api/add-green-space           - Add new green space
```

### Feedback
```
GET  /api/feedback                  - Get all feedback
POST /api/submit-feedback           - Submit new feedback
```

### Dashboard
```
GET  /api/dashboard/simple-stats    - Get statistics
GET  /api/dashboard/recent-activity - Get recent activity
```

### Environmental Data
```
GET  /api/environmental-data        - Get environmental data
POST /api/submit-environmental-data - Submit environmental data
```

### Database Setup
```
GET  /create-green-spaces-table     - Create green_spaces table
GET  /create-feedback-table         - Create public_feedback table
GET  /create-environmental-table    - Create environmental_data table
GET  /create-users-table            - Create users table
```

---

## Troubleshooting

### Backend Not Running?
If you see connection errors, restart the backend:

```bash
cd backend
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

### Database Connection Error?
Check your database credentials in `backend/app.py`:
```python
DB_CONFIG = {
    "dbname": "kitwe_green_spaces",
    "user": "postgres",
    "password": "hapiness",
    "host": "localhost",
    "port": "5432"
}
```

### CORS Errors?
If you see CORS errors in the browser console:
1. Make sure the backend is running
2. Use a local web server instead of opening files directly
3. Check that `flask-cors` is installed: `pip install flask-cors`

### Map Not Loading?
1. Check browser console for errors
2. Verify backend is running: http://127.0.0.1:5000/api/green-spaces
3. Check that `frontend/config.js` has correct API URL

---

## What's Working Now

### ✅ Frontend Pages
- Main map with 35 green spaces
- Admin portal with statistics
- Feedback submission form
- Dashboard pages (simple, advanced, council)
- Environmental monitoring dashboard
- Report generator

### ✅ Backend API
- All endpoints responding correctly
- No more 500 errors
- No more 404 errors for missing endpoints
- Proper error handling
- Database tables created

### ✅ Database
- PostgreSQL connected
- 35 green spaces loaded
- Tables ready for feedback and environmental data
- User authentication system in place

---

## Next Steps

### 1. Add Sample Data
To test the full functionality:
- Submit feedback through the feedback form
- Add environmental data through the monitoring page
- Create test user accounts

### 2. Customize
- Update green space data in the database
- Customize colors and styling in CSS
- Add more features to the admin portal

### 3. Deploy to Production
When ready to go live:
- Set `debug=False` in `backend/app.py`
- Use a production WSGI server (gunicorn)
- Deploy to a cloud platform (Heroku, AWS, etc.)
- Update CORS settings for your domain

---

## Support

### Documentation Files
- `BACKEND_FIXES_COMPLETE.md` - Detailed list of all fixes
- `BACKEND_FIX_SUMMARY.md` - Original issue summary
- `DATABASE_CONNECTION_COMPLETE.md` - Database setup guide
- `COMPLETE_APP_SUMMARY.md` - Full application overview

### Test Accounts
If you created the users table, you can login with:
- **Admin**: username: `admin`, password: `admin123`
- **Council**: username: `council`, password: `council123`
- **Citizen**: username: `citizen`, password: `citizen123`

---

## Summary

🎉 **Everything is working!**

Your Kitwe Green Spaces application is now fully functional with:
- ✅ 35 green spaces on an interactive map
- ✅ Working admin portal with statistics
- ✅ Feedback submission system
- ✅ Environmental monitoring dashboard
- ✅ All backend API endpoints operational
- ✅ Database connected and ready

**Just open `frontend/index.html` or `frontend/admin-portal.html` in your browser to get started!**

---

*Last Updated: May 23, 2026*
