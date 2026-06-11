# 🗺️ How to Use the Built-in Routing Feature

## Quick Start Guide

### Step 1: Find a Green Space
- Browse the map or use the search bar to find a green space
- Click on any green space marker to open its popup

### Step 2: Get Directions
- In the popup, click the **"Get Directions"** button (blue button with directions icon)
- Your browser will ask for location permission - click **"Allow"**

### Step 3: View Your Route
- A blue route line will appear on the map
- You'll see two markers:
  - 🔵 **Blue marker** = Your current location
  - 🏁 **Green checkered flag** = Your destination
- A notification will show: **"🚗 Route found: X.XX km, ~XX minutes"**

### Step 4: Clear Directions (Optional)
- A red **"Clear Directions"** button will appear in the sidebar
- Click it to remove the route from the map

---

## 🎯 What You'll See

### Before Clicking "Get Directions"
```
┌─────────────────────────────────────┐
│  🌳 Central Park Kitwe              │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  📍 City Centre                     │
│  📏 3.5 hectares                    │
│  🌲 Type: Park                      │
│                                     │
│  [🧭 Get Directions] [ℹ️ Details]   │
│  [🚩 Report Issue]                  │
└─────────────────────────────────────┘
```

### After Route is Calculated
```
Map View:
┌─────────────────────────────────────┐
│                                     │
│     🔵 (You)                        │
│      │                              │
│      │ ← Blue route line            │
│      │                              │
│      └──────────→ 🏁 (Park)         │
│                                     │
└─────────────────────────────────────┘

Sidebar:
┌─────────────────────────────────────┐
│  🔍 Search green spaces...          │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                     │
│  [📍 Find Parks Near Me]            │
│  [❌ Clear Directions] ← NEW!       │
│                                     │
└─────────────────────────────────────┘

Notification:
┌─────────────────────────────────────┐
│ ✅ Route found: 3.45 km, ~12 min    │
└─────────────────────────────────────┘
```

---

## 🚨 Troubleshooting

### "Could not get your location"
**Cause:** Location permission denied or unavailable

**Solutions:**
1. Check browser location settings
2. Make sure you're using HTTPS (or localhost)
3. Click "Allow" when browser asks for permission
4. Use the Google Maps fallback option

### "Could not find route"
**Cause:** No road connection between locations

**Solutions:**
1. The app will automatically offer Google Maps
2. Click "OK" to open Google Maps
3. Google Maps has more routing options

### Route looks wrong
**Cause:** OSRM routing data may be outdated

**Solutions:**
1. Use Google Maps fallback for more accurate routes
2. Report the issue if it's a consistent problem

---

## 💡 Tips & Tricks

### 1. **Allow Location Permission**
- Always allow location permission for best experience
- You can revoke it later in browser settings

### 2. **Clear Old Routes**
- Always clear old routes before getting new directions
- Click the red "Clear Directions" button

### 3. **Mobile Usage**
- Works great on mobile devices
- Make sure location services are enabled
- Use in landscape mode for better view

### 4. **Offline Mode**
- Routing requires internet connection
- Download offline maps for future enhancement

### 5. **Battery Saving**
- Clear directions when done to save battery
- Disable location services when not needed

---

## 🌟 Feature Highlights

### ✅ What Works
- ✅ Automatic location detection
- ✅ Visual route display on map
- ✅ Distance and time estimates
- ✅ Custom markers for start/end
- ✅ One-click route clearing
- ✅ Fallback to Google Maps
- ✅ Mobile-friendly interface
- ✅ No API keys needed

### ⏳ Coming Soon (Optional)
- ⏳ Walking vs driving routes
- ⏳ Alternative route options
- ⏳ Turn-by-turn instructions
- ⏳ Save favorite routes
- ⏳ Share routes with friends

---

## 🎨 Visual Elements

### Route Line
- **Color:** Blue (#4285F4)
- **Width:** 6 pixels
- **Opacity:** 80%
- **Style:** Solid line

### Your Location Marker
- **Color:** Blue
- **Icon:** User icon (👤)
- **Size:** 32x32 pixels
- **Border:** White, 3px

### Destination Marker
- **Color:** Green
- **Icon:** Checkered flag (🏁)
- **Size:** 32x32 pixels
- **Border:** White, 3px

### Clear Directions Button
- **Color:** Red gradient
- **Icon:** Times circle (❌)
- **Position:** Sidebar, below "Find Parks Near Me"
- **Visibility:** Hidden until route is shown

---

## 📱 Mobile Experience

### Portrait Mode
```
┌─────────────┐
│   Sidebar   │
│ ┌─────────┐ │
│ │ Search  │ │
│ └─────────┘ │
│             │
│ [Find Near] │
│ [Clear Dir] │
├─────────────┤
│             │
│     Map     │
│   🔵───🏁   │
│             │
└─────────────┘
```

### Landscape Mode
```
┌──────────┬────────────────────┐
│ Sidebar  │                    │
│ Search   │       Map          │
│ [Find]   │     🔵───🏁        │
│ [Clear]  │                    │
└──────────┴────────────────────┘
```

---

## 🔒 Privacy & Security

### Location Data
- ✅ Only used for routing
- ✅ Not stored on server
- ✅ Not shared with third parties
- ✅ Cleared when route is removed

### Permissions
- 📍 Location permission required
- 🌐 Internet connection required
- 🔒 HTTPS recommended (required for production)

### Data Usage
- Minimal data usage (~50-100 KB per route)
- Route data cached temporarily
- No tracking or analytics

---

## 🎓 For Developers

### Key Functions
```javascript
// Show directions to a location
showDirections(latitude, longitude, name)

// Clear directions from map
clearDirections()

// Check if routing is active
if (routingControl) {
    // Route is displayed
}
```

### Event Listeners
```javascript
// Listen for route found
routingControl.on('routesfound', function(e) {
    const distance = e.routes[0].summary.totalDistance;
    const time = e.routes[0].summary.totalTime;
});

// Listen for routing errors
routingControl.on('routingerror', function(e) {
    // Handle error
});
```

### Customization
```javascript
// Change route color
lineOptions: {
    styles: [{
        color: '#FF0000',  // Red route
        opacity: 0.8,
        weight: 6
    }]
}

// Change routing profile
router: L.Routing.osrmv1({
    profile: 'foot'  // walking, car, bike
})
```

---

## 📞 Support

### Need Help?
- Check browser console for errors (F12)
- Verify location permission is granted
- Try refreshing the page
- Use Google Maps fallback if routing fails

### Report Issues
- Use the "Report Issue" button on green space popups
- Include browser and device information
- Describe what you were trying to do

---

## 🎉 Enjoy Your Routes!

The built-in routing feature makes it easy to navigate to any green space in Kitwe. No more switching between apps - everything you need is right here!

**Happy exploring! 🌳🗺️**
