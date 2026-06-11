# 🌍 Import Real Green Spaces from OpenStreetMap

## What This Does

This script fetches **real, verified green space data** from OpenStreetMap for Kitwe, Zambia. It will replace your fake/inaccurate data with actual parks, gardens, and green spaces that exist in the real world.

## How to Use

### **Step 1: Install Required Package**

The script needs the `requests` library. Install it:

```bash
pip install requests
```

### **Step 2: Run the Script**

```bash
cd backend
python fetch_osm_greenspaces.py
```

### **Step 3: Review the Results**

The script will:
1. ✅ Fetch data from OpenStreetMap
2. ✅ Process and clean the data
3. ✅ Show you what it found
4. ✅ Save a backup JSON file
5. ❓ Ask if you want to update the database

### **Step 4: Confirm Database Update**

When prompted:
```
💾 Save to database? This will REPLACE existing data (y/n):
```

Type `y` and press Enter to update your database with real data.

### **Step 5: Refresh Your Map**

1. Go back to your browser
2. Refresh the page (Ctrl+F5)
3. Switch to satellite view
4. Verify the green spaces now match reality!

## What Data Gets Imported

The script fetches:

### **Types of Green Spaces:**
- 🌳 **Parks** - Public parks and recreational areas
- 🌺 **Gardens** - Public and community gardens
- 🌲 **Forests** - Forested areas
- ⚽ **Recreation Grounds** - Sports fields and pitches
- 🏌️ **Golf Courses** - Golf facilities
- 🌿 **Nature Reserves** - Protected natural areas
- 🌾 **Meadows & Grasslands** - Open green spaces

### **Data Included:**
- ✅ Accurate GPS coordinates (latitude/longitude)
- ✅ Real names from OpenStreetMap
- ✅ Calculated area (square meters and hectares)
- ✅ Type classification
- ✅ Ward/district information (if available)
- ✅ Descriptions

## Expected Results

### **If Kitwe Has OSM Data:**
```
✅ Found 15 green spaces!

📋 Sample green spaces:
   1. Mindolo Dam Park (park) - 12.50 ha
   2. Kitwe Golf Club (golf course) - 45.30 ha
   3. Nkana Recreation Ground (recreational) - 8.20 ha
   ... and 12 more

💾 Save to database? This will REPLACE existing data (y/n):
```

### **If No OSM Data Available:**
```
⚠️ No green spaces found in the data

💡 This might mean:
   - Kitwe doesn't have mapped green spaces in OSM yet
   - The bounding box needs adjustment
   - You may need to add data to OpenStreetMap first
```

## If No Data Is Found

### **Option A: Adjust the Bounding Box**

Edit `fetch_osm_greenspaces.py` and modify the coordinates:

```python
# Current bounding box
KITWE_BBOX = [-12.9, 28.1, -12.7, 28.3]

# Try expanding it
KITWE_BBOX = [-13.0, 28.0, -12.6, 28.4]
```

### **Option B: Add Data to OpenStreetMap**

1. Go to https://www.openstreetmap.org
2. Create a free account
3. Use the "Edit" button to add green spaces
4. Wait 24 hours for data to sync
5. Run the script again

### **Option C: Use Sample Data**

If OSM has no data for Kitwe, I can create realistic sample data based on:
- Typical Zambian city layout
- Common park sizes
- Realistic coordinates within Kitwe

## Backup & Safety

### **Automatic Backup:**
The script saves a JSON backup file before updating the database:
- File: `osm_greenspaces.json`
- Location: `backend/` folder
- Contains all fetched data

### **Restore from Backup:**
If you need to restore old data, you can:
1. Keep a backup of your current database
2. Use pgAdmin to export data before running script
3. The JSON file can be used to restore OSM data

## Troubleshooting

### **Error: "Connection refused"**
- Make sure PostgreSQL is running
- Check database credentials in the script
- Verify database name is correct

### **Error: "requests module not found"**
```bash
pip install requests
```

### **Error: "Timeout"**
- OpenStreetMap Overpass API might be busy
- Wait a few minutes and try again
- The script has a 60-second timeout

### **No green spaces found**
- Kitwe might not have OSM data yet
- Try adjusting the bounding box
- Consider adding data to OSM first

### **Coordinates seem wrong**
- Check the bounding box coordinates
- Verify they cover Kitwe area
- Use https://boundingbox.klokantech.com/ to get correct bbox

## Verifying the Data

### **After Import:**

1. **Check Database:**
```sql
SELECT COUNT(*) FROM green_spaces;
SELECT type, COUNT(*) FROM green_spaces GROUP BY type;
```

2. **Check Map:**
- Refresh your browser
- Switch to satellite view
- Zoom in on markers
- Verify they match real locations

3. **Check JSON Backup:**
- Open `osm_greenspaces.json`
- Review the data
- Verify coordinates look reasonable

## Advanced: Customizing the Query

You can modify what types of green spaces to fetch by editing the Overpass query in the script:

```python
OVERPASS_QUERY = f"""
[out:json][timeout:60];
(
  // Add more types here
  way["leisure"="park"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Example: Add playgrounds
  way["leisure"="playground"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
);
out body;
>;
out skel qt;
"""
```

## Benefits of Real OSM Data

### **Accuracy:**
- ✅ Real GPS coordinates
- ✅ Verified by OSM community
- ✅ Matches satellite imagery
- ✅ Up-to-date information

### **Credibility:**
- ✅ Data from reputable source
- ✅ Can cite OpenStreetMap
- ✅ Verifiable by examiners
- ✅ Professional standard

### **Completeness:**
- ✅ Includes all mapped green spaces
- ✅ Proper classifications
- ✅ Real area calculations
- ✅ Actual names

## For Your Project Report

You can now write:

> "Green space data was obtained from OpenStreetMap, a collaborative mapping project with verified, crowd-sourced geographic data. The data was fetched using the Overpass API and includes accurate GPS coordinates, area measurements, and classifications for all public green spaces in Kitwe."

This is much more credible than fake sample data!

## Summary

**Before:** Fake coordinates that don't match satellite imagery  
**After:** Real, verified green spaces from OpenStreetMap

**Steps:**
1. Install requests: `pip install requests`
2. Run script: `python backend/fetch_osm_greenspaces.py`
3. Review results
4. Confirm database update
5. Refresh map and verify!

---

**Note:** If Kitwe has limited OSM data, you might get fewer green spaces than the fake data. This is actually better - it's real data you can verify and defend in your project!

**Ready to get real data? Run the script now!** 🌍✨
