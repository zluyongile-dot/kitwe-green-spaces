# 🔧 Spatial Analysis Troubleshooting Guide

## Problem: Spatial Analysis Buttons Not Working

### Step 1: Run Diagnostic Test

1. Open `test-spatial-analysis.html` in your browser
2. It will automatically check if all libraries are loading
3. Look for ✅ (success) or ❌ (error) messages

### Step 2: Check Browser Console

1. Open your browser console:
   - **Windows/Linux**: Press `F12` or `Ctrl+Shift+I`
   - **Mac**: Press `Cmd+Option+I`
2. Click the **"Console"** tab
3. Look for **red error messages**

### Common Errors and Solutions:

---

## Error 1: "turf is not defined"

**Problem:** Turf.js library not loading

**Solutions:**
1. Check internet connection
2. Hard refresh: `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)
3. Try different browser
4. Check if firewall/antivirus is blocking CDN

**Quick Fix:**
```html
<!-- Make sure this line is in index.html before the main script -->
<script src="https://unpkg.com/@turf/turf@6.5.0/turf.min.js"></script>
```

---

## Error 2: "L.heatLayer is not a function"

**Problem:** Leaflet.heat library not loading

**Solutions:**
1. Check internet connection
2. Verify this line exists in index.html:
```html
<script src="https://unpkg.com/leaflet.heat@0.2.0/dist/leaflet-heat.js"></script>
```

---

## Error 3: "Cannot read property 'addEventListener' of null"

**Problem:** Button elements not found (wrong IDs or timing issue)

**Solutions:**
1. Check that button IDs match:
   - `toggleHeatMap`
   - `toggleBufferZones`
   - `toggleClustering`
   - `toggleCoverage`
   - `toggleDistanceAnalysis`
   - `clearAllAnalysis`

2. Verify buttons exist in HTML

---

## Error 4: Buttons Don't Change State (Stay [OFF])

**Problem:** Event listeners not attached or JavaScript error

**Check:**
1. Open console and look for: `"🗺️ Setting up spatial analysis controls..."`
2. If you don't see this, `setupSpatialAnalysis()` isn't running

**Solutions:**
1. Check if `setupSpatialAnalysis()` is called in initialization
2. Look for JavaScript errors that stop execution
3. Verify all functions are defined before being called

---

## Error 5: "allGreenSpaces is not defined"

**Problem:** Green space data not loaded yet

**Solutions:**
1. Wait for map to fully load (see green space markers)
2. Check backend is running: `http://localhost:5000/api/green-spaces`
3. Check browser console for API errors

---

## Error 6: Buttons Click But Nothing Happens

**Problem:** Functions defined but not working correctly

**Debug Steps:**
1. Open console
2. Click a button
3. Look for notification messages
4. Check for error messages

**Manual Test:**
```javascript
// Type this in console:
console.log('Heat map layer:', heatMapLayer);
console.log('All green spaces:', allGreenSpaces);
console.log('Map object:', map);
```

---

## Error 7: "Failed to load resource" (CDN errors)

**Problem:** CDN blocked or unavailable

**Solutions:**
1. Check internet connection
2. Try different network (mobile hotspot)
3. Check if corporate firewall is blocking CDN
4. Use VPN if CDN is geo-blocked

**Alternative:** Download libraries locally
```bash
# Download libraries to local folder
mkdir frontend/libs
# Then update script tags to use local files
```

---

## Error 8: Works on Desktop but Not Mobile

**Problem:** Mobile browser compatibility

**Solutions:**
1. Update mobile browser to latest version
2. Try different mobile browser (Chrome, Firefox, Safari)
3. Check if JavaScript is enabled on mobile
4. Clear mobile browser cache

---

## Quick Diagnostic Checklist

Run through this checklist:

- [ ] Internet connection working
- [ ] Browser console open (F12)
- [ ] No red errors in console
- [ ] Green space markers visible on map
- [ ] Sidebar visible (click ☰ if not)
- [ ] Scrolled down to "Spatial Analysis" section
- [ ] Buttons visible with [OFF] toggles
- [ ] Clicked button and it turned green
- [ ] Notification appeared
- [ ] Analysis appeared on map

**If any step fails, that's where the problem is!**

---

## Manual Test in Console

Copy and paste this into browser console:

```javascript
// Test 1: Check libraries
console.log('Leaflet:', typeof L !== 'undefined' ? '✅' : '❌');
console.log('Leaflet.heat:', typeof L.heatLayer !== 'undefined' ? '✅' : '❌');
console.log('Turf.js:', typeof turf !== 'undefined' ? '✅' : '❌');
console.log('Markercluster:', typeof L.markerClusterGroup !== 'undefined' ? '✅' : '❌');

// Test 2: Check data
console.log('Green spaces loaded:', allGreenSpaces ? allGreenSpaces.length : 'NONE');
console.log('Map initialized:', map ? '✅' : '❌');

// Test 3: Check buttons
console.log('Heat map button:', document.getElementById('toggleHeatMap') ? '✅' : '❌');
console.log('Buffer button:', document.getElementById('toggleBufferZones') ? '✅' : '❌');
console.log('Cluster button:', document.getElementById('toggleClustering') ? '✅' : '❌');
console.log('Coverage button:', document.getElementById('toggleCoverage') ? '✅' : '❌');
console.log('Distance button:', document.getElementById('toggleDistanceAnalysis') ? '✅' : '❌');

// Test 4: Manually trigger heat map
if (typeof showHeatMap === 'function') {
    console.log('Manually triggering heat map...');
    showHeatMap();
} else {
    console.log('❌ showHeatMap function not found!');
}
```

---

## Still Not Working?

### Collect This Information:

1. **Browser and version:**
   - Chrome 120? Firefox 115? Safari 17?

2. **Console errors:**
   - Copy all red error messages

3. **What happens when you click:**
   - Does button turn green?
   - Do you see a notification?
   - Any console messages?

4. **Test results:**
   - Run `test-spatial-analysis.html`
   - Share the results

5. **Network tab:**
   - Open F12 → Network tab
   - Refresh page
   - Look for failed requests (red)
   - Share which files failed to load

---

## Emergency Fallback: Simplified Version

If nothing works, try this simplified heat map only:

```html
<!-- Add after map initialization -->
<script>
// Simple heat map test
function testHeatMap() {
    if (typeof L === 'undefined' || typeof L.heatLayer === 'undefined') {
        alert('Leaflet.heat not loaded!');
        return;
    }
    
    if (!allGreenSpaces || allGreenSpaces.length === 0) {
        alert('No green space data!');
        return;
    }
    
    const heatData = allGreenSpaces.map(space => {
        const coords = space.geometry.coordinates;
        return [coords[1], coords[0], 0.5];
    });
    
    const heat = L.heatLayer(heatData, {radius: 25}).addTo(map);
    alert('Heat map added! Check the map.');
}

// Add button to test
console.log('Type testHeatMap() in console to test');
</script>
```

---

## Contact Support

If you've tried everything above and it still doesn't work:

1. Share the console errors
2. Share test-spatial-analysis.html results
3. Share your browser/OS info
4. Share a screenshot of what you see

**Student:** Mukendwa Luyongile (202201912)  
**Supervisor:** Mr. Nyirenda

---

## Most Common Solution

**90% of the time, the issue is:**
1. ❌ Libraries not loading (internet/CDN issue)
2. ❌ Browser cache (need hard refresh: Ctrl+F5)
3. ❌ JavaScript error earlier in code (check console)

**Try these first:**
1. Hard refresh: `Ctrl+F5`
2. Open console: `F12`
3. Run diagnostic: `test-spatial-analysis.html`
