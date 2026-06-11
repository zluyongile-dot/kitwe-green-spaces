# Spatial Analysis Features - User Guide

## Overview
The Kitwe Green Space Map now includes powerful spatial analysis tools to help you understand patterns, density, and accessibility of green spaces across the city.

## Features

### 1. 🔥 Heat Map
**What it does:** Shows the density and distribution of green spaces across Kitwe using color-coded intensity.

**How to use:**
1. Click the "Heat Map" button in the Spatial Analysis panel
2. The map will display colored overlays:
   - **Blue**: Low density (few green spaces)
   - **Cyan**: Medium-low density
   - **Yellow**: Medium-high density
   - **Red**: High density (many green spaces)

**Use cases:**
- Identify areas with abundant green spaces
- Find neighborhoods lacking green infrastructure
- Plan new green space development in underserved areas

---

### 2. ⭕ Buffer Zones (Accessibility Analysis)
**What it does:** Shows walking distance accessibility by drawing circles around each green space.

**How to use:**
1. Click the "Buffer Zones" button
2. Three colored circles appear around each green space:
   - **Green circle**: 500m radius (~6 minute walk)
   - **Yellow circle**: 1km radius (~12 minute walk)
   - **Red circle**: 2km radius (~25 minute walk)

**Use cases:**
- Determine if your neighborhood has accessible green spaces
- Identify coverage gaps where residents must walk far
- Plan locations for new parks to maximize accessibility

---

### 3. 🔗 Clustering
**What it does:** Groups nearby green spaces into clusters when zoomed out, making the map easier to read.

**How to use:**
1. Click the "Clustering" button
2. Markers will group together showing the number of spaces in each cluster
3. Click a cluster to zoom in and see individual spaces
4. Cluster colors indicate size:
   - **Green**: Small cluster (2-10 spaces)
   - **Orange**: Medium cluster (11-20 spaces)
   - **Red**: Large cluster (20+ spaces)

**Use cases:**
- Get an overview of green space distribution without clutter
- Quickly identify areas with many vs few green spaces
- Navigate large datasets more easily

---

### 4. 📊 Coverage Analysis
**What it does:** Highlights areas that are well-served or underserved by green spaces.

**How to use:**
1. Click the "Coverage Analysis" button
2. The map displays colored overlays:
   - **Green areas**: Well-served (within 1km of a green space)
   - **Red areas**: Underserved (more than 1km from nearest green space)

**Use cases:**
- Identify neighborhoods needing more green infrastructure
- Assess equity in green space distribution
- Support urban planning decisions with data

---

### 5. 📏 Distance Analysis
**What it does:** Click anywhere on the map to find the nearest green space and see the distance.

**How to use:**
1. Click the "Distance Analysis" button
2. Your cursor changes to a crosshair
3. Click any location on the map
4. An orange marker appears showing:
   - Name of nearest green space
   - Distance in meters or kilometers
   - A dashed line connecting your point to the space

**Use cases:**
- Find the nearest park from your home or workplace
- Calculate walking distances to green spaces
- Assess accessibility from specific locations

---

## Tips & Best Practices

### Combining Analyses
You can activate multiple analyses at once! Try these combinations:
- **Heat Map + Buffer Zones**: See density patterns and accessibility together
- **Coverage + Distance Analysis**: Identify underserved areas and measure distances
- **Clustering + Heat Map**: Get both overview and detailed density information

### Performance
- Coverage Analysis may take a few seconds to calculate for large areas
- Zoom in before activating Buffer Zones for better performance
- Use Clustering when viewing the entire city to improve map responsiveness

### Clearing Analysis
- Click individual analysis buttons again to toggle them off
- Use "Clear All Analysis" button to remove all visualizations at once
- Analysis layers are removed when you refresh the page

---

## Technical Details

### Libraries Used
- **Leaflet.heat**: Heat map visualization
- **Leaflet.markercluster**: Marker clustering
- **Turf.js**: Spatial calculations (buffers, distances, coverage)

### Calculations
- **Buffer zones**: Circular buffers using geodesic distance
- **Coverage**: Grid-based analysis with 1km resolution
- **Distance**: Haversine formula for accurate earth-surface distances
- **Heat map**: Weighted by green space area (larger = more intense)

### Data Sources
- Green space locations from PostgreSQL/PostGIS database
- Real-time calculations performed in browser
- No external API calls required

---

## Accessibility

All spatial analysis features are keyboard accessible:
- Use **Tab** to navigate between analysis buttons
- Press **Enter** or **Space** to toggle analyses
- Press **Escape** to close popups and dialogs
- Screen readers announce analysis activation/deactivation

---

## Troubleshooting

**Heat map not showing?**
- Ensure you have green space data loaded
- Try zooming out to see the full heat map extent
- Check that your browser supports Canvas rendering

**Buffer zones too cluttered?**
- Zoom in to see individual buffers more clearly
- Use clustering to reduce visual complexity
- Toggle buffer zones off when not needed

**Coverage analysis slow?**
- This is normal for large areas - it calculates thousands of points
- Zoom in to a smaller area for faster results
- Close other browser tabs to free up memory

**Distance analysis not working?**
- Ensure the analysis is activated (button shows toggle-on icon)
- Click directly on the map, not on markers
- Check that you have green space data loaded

---

## Future Enhancements

Planned features for future versions:
- **Isochrone Analysis**: Show actual walking/driving time zones
- **Population Density Overlay**: Combine with census data
- **Temporal Analysis**: Track changes in green space over time
- **Custom Buffer Distances**: User-defined accessibility radii
- **Export Analysis Results**: Download maps and statistics

---

## Support

For questions or issues with spatial analysis features:
1. Check this guide first
2. Review the help panel in the sidebar (? icon)
3. Contact: Mukendwa Luyongile (202201912)
4. Supervisor: Mr. Nyirenda, Mulungushi University

---

**Last Updated:** May 26, 2026  
**Version:** 1.0  
**Project:** Kitwe Green Space Mapping System  
**Institution:** Mulungushi University, BSc Computer Science
