# Backend Issues and Fixes

## Issues Found:

1. **Duplicate API Routes** - `/api/feedback` is defined twice in app.py (lines 409 and 1388)
2. **Missing API Endpoints** - Admin portal expects endpoints that don't exist:
   - `/api/dashboard/recent-activity`
   - `/api/environmental-data`
3. **Database Table Issues** - Some tables may not be created:
   - `public_feedback` table
   - `environmental_data` table

## Solutions:

### 1. Fix Duplicate Routes
Remove duplicate `/api/feedback` definition

### 2. Add Missing Endpoints
Create the following endpoints:
- `/api/dashboard/recent-activity` - Returns recent system activity
- `/api/environmental-data` - Returns environmental monitoring data
- `/create-environmental-table` - Creates environmental_data table

### 3. Ensure Tables Exist
Run these endpoints to create tables:
- http://127.0.0.1:5000/create-feedback-table
- http://127.0.0.1:5000/create-environmental-table (new)

## Quick Fix Steps:

1. Stop the Flask backend (Ctrl+C)
2. Apply the fixes to backend/app.py
3. Restart the backend: `python backend/app.py`
4. Visit setup endpoints to create missing tables
5. Test the frontend pages

## API Endpoints Status:

✅ Working:
- `/api/green-spaces` - Returns 35 green spaces
- `/api/dashboard/simple-stats` - Returns statistics

❌ Broken:
- `/api/feedback` - 500 Internal Server Error (duplicate routes)
- `/api/dashboard/recent-activity` - 404 Not Found
- `/api/environmental-data` - 404 Not Found
