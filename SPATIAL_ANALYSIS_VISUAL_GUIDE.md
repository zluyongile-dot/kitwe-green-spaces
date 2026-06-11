# Spatial Analysis - Visual Guide

## What You'll See

### Spatial Analysis Panel Location
```
┌─────────────────────────────────────┐
│  SIDEBAR                            │
│                                     │
│  🔍 Search Bar                      │
│  📊 Statistics (3 cards)            │
│  🎯 Find Parks Near Me Button       │
│  🔧 Filters Section                 │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 📊 SPATIAL ANALYSIS           │ │ ← NEW!
│  │                               │ │
│  │ Visualize patterns, density,  │ │
│  │ and accessibility...          │ │
│  │                               │ │
│  │ [🔥 Heat Map]         [OFF]   │ │
│  │ [⭕ Buffer Zones]     [OFF]   │ │
│  │ [🔗 Clustering]       [OFF]   │ │
│  │ [📊 Coverage]         [OFF]   │ │
│  │ [📏 Distance]         [OFF]   │ │
│  │                               │ │
│  │ [Clear All Analysis]          │ │
│  └───────────────────────────────┘ │
│                                     │
│  🗺️ Map Legend                     │
└─────────────────────────────────────┘
```

---

## Analysis Button Design

Each button looks like this:

```
┌────────────────────────────────────────┐
│ [🔥]  Heat Map                  [OFF] │
│       Show density of green spaces     │
└────────────────────────────────────────┘
 ↑      ↑                           ↑
Icon   Title                     Toggle
       Description
```

**When Active:**
```
┌────────────────────────────────────────┐
│ [🔥]  Heat Map                  [ON]  │ ← Green border
│       Show density of green spaces     │
└────────────────────────────────────────┘
```

---

## Visual Examples

### 1. Heat Map View
```
MAP VIEW:
┌─────────────────────────────────────────┐
│                                         │
│     🔴🔴🔴                              │ ← Red = High density
│     🔴🔴🔴                              │
│                                         │
│           🟡🟡                          │ ← Yellow = Medium
│           🟡🟡                          │
│                                         │
│                    🔵🔵                 │ ← Blue = Low density
│                    🔵🔵                 │
│                                         │
└─────────────────────────────────────────┘

LEGEND:
🔵 Low Density
🟢 Medium-Low
🟡 Medium-High
🔴 High Density
```

---

### 2. Buffer Zones View
```
MAP VIEW:
┌─────────────────────────────────────────┐
│                                         │
│        ⭕⭕⭕                            │ ← Red circle (2km)
│       ⭕🟡🟡⭕                           │ ← Yellow circle (1km)
│      ⭕🟡🟢🟡⭕                          │ ← Green circle (500m)
│       ⭕🟡🟡⭕                           │ ← 📍 Green space
│        ⭕⭕⭕                            │
│                                         │
└─────────────────────────────────────────┘

LEGEND:
🟢 500m (~6 min walk)
🟡 1km (~12 min walk)
🔴 2km (~25 min walk)
```

---

### 3. Clustering View
```
MAP VIEW (Zoomed Out):
┌─────────────────────────────────────────┐
│                                         │
│     (15)                                │ ← Cluster with 15 spaces
│                                         │
│              (8)                        │ ← Cluster with 8 spaces
│                                         │
│                        (23)             │ ← Cluster with 23 spaces
│                                         │
│  (3)                                    │ ← Cluster with 3 spaces
│                                         │
└─────────────────────────────────────────┘

COLORS:
🟢 Small (2-10 spaces)
🟠 Medium (11-20 spaces)
🔴 Large (20+ spaces)

Click cluster to zoom in and see individual markers!
```

---

### 4. Coverage Analysis View
```
MAP VIEW:
┌─────────────────────────────────────────┐
│                                         │
│  🟢🟢🟢🟢                               │ ← Green = Well-served
│  🟢🟢🟢🟢                               │   (<1km to park)
│  🟢🟢🟢🟢                               │
│                                         │
│           🔴🔴🔴                        │ ← Red = Underserved
│           🔴🔴🔴                        │   (>1km to park)
│           🔴🔴🔴                        │
│                                         │
└─────────────────────────────────────────┘

INTERPRETATION:
🟢 Residents have easy access to green spaces
🔴 Residents must walk far to reach green spaces
```

---

### 5. Distance Analysis View
```
MAP VIEW (After Clicking):
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│         🟠 ← You clicked here           │
│          ┊                              │
│          ┊ (dashed line)                │
│          ┊                              │
│          📍 ← Nearest green space       │
│                                         │
│  POPUP:                                 │
│  ┌─────────────────────┐                │
│  │ 📏 Nearest Space    │                │
│  │ Central Park        │                │
│  │ Distance: 850m      │                │
│  └─────────────────────┘                │
│                                         │
└─────────────────────────────────────────┘
```

---

## Button States

### Inactive (Default)
```
┌────────────────────────────────────────┐
│ [🔥]  Heat Map                  [⚪]  │ ← Gray toggle
│       Show density of green spaces     │
└────────────────────────────────────────┘
```

### Hover
```
┌────────────────────────────────────────┐
│ [🔥]  Heat Map                  [⚪]  │ ← Slight lift effect
│       Show density of green spaces     │ ← Green border appears
└────────────────────────────────────────┘
```

### Active
```
┌────────────────────────────────────────┐
│ [🔥]  Heat Map                  [🟢]  │ ← Green toggle
│       Show density of green spaces     │ ← Green border
└────────────────────────────────────────┘
```

---

## Dynamic Legend

When analyses are active, a legend appears below the buttons:

```
┌───────────────────────────────────┐
│ Active Analysis                   │
│                                   │
│ Heat Map                          │
│ 🔵 Low Density                    │
│ 🟢 Medium-Low Density             │
│ 🟡 Medium-High Density            │
│ 🔴 High Density                   │
│                                   │
│ Buffer Zones                      │
│ 🟢 500m Walking Distance          │
│ 🟡 1km Walking Distance           │
│ 🔴 2km Walking Distance           │
└───────────────────────────────────┘
```

---

## Notifications

When you activate/deactivate analyses, you'll see notifications:

```
┌─────────────────────────────────┐
│ ✅ Heat map activated           │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ ℹ️ Heat map removed             │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ ⭕ Buffer zones activated        │
│    (500m, 1km, 2km)             │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ 📏 Click anywhere on the map    │
│    to find nearest green space  │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ 🗑️ All spatial analysis cleared │
└─────────────────────────────────┘
```

---

## Color Scheme

### Analysis Colors
- **Heat Map**: Blue → Cyan → Yellow → Red
- **Buffer Zones**: Green (500m), Yellow (1km), Red (2km)
- **Clustering**: Green (small), Orange (medium), Red (large)
- **Coverage**: Green (well-served), Red (underserved)
- **Distance**: Orange marker, orange dashed line

### UI Colors
- **Primary**: Green (#1B5E20, #4CAF50)
- **Icons**: Gradient backgrounds
- **Borders**: Light gray (inactive), Green (active)
- **Toggle**: Gray (off), Green (on)

---

## Responsive Design

### Desktop (>768px)
```
┌──────────────┬─────────────────────────┐
│              │                         │
│   SIDEBAR    │         MAP             │
│   (420px)    │      (Remaining)        │
│              │                         │
│  Spatial     │    Analysis layers      │
│  Analysis    │    displayed here       │
│  Panel       │                         │
│              │                         │
└──────────────┴─────────────────────────┘
```

### Mobile (<768px)
```
┌─────────────────────────────────┐
│          MAP (Full Width)       │
│                                 │
│  [☰] ← Hamburger menu           │
│                                 │
│  (Sidebar slides in from left)  │
│                                 │
└─────────────────────────────────┘

When menu opened:
┌─────────────────────────────────┐
│ SIDEBAR (Full Width)            │
│                                 │
│ Spatial Analysis Panel          │
│ (Scrollable)                    │
│                                 │
│ [×] Close                       │
└─────────────────────────────────┘
```

---

## Interaction Flow

### Example: Activating Heat Map

1. **Initial State**
   ```
   [🔥 Heat Map] [OFF]
   Map shows normal markers
   ```

2. **Click Button**
   ```
   [🔥 Heat Map] [ON] ← Button turns green
   ```

3. **Processing**
   ```
   Notification: "🔥 Heat map activated"
   ```

4. **Result**
   ```
   Map now shows colored heat overlay
   Legend appears showing color meanings
   ```

5. **Click Again to Deactivate**
   ```
   [🔥 Heat Map] [OFF] ← Button returns to gray
   Notification: "ℹ️ Heat map removed"
   Heat overlay disappears
   ```

---

## Tips for Best Viewing

### Heat Map
- Zoom out to see city-wide patterns
- Works best with 10+ green spaces visible

### Buffer Zones
- Zoom in to see individual circles clearly
- May be cluttered with many spaces - use selectively

### Clustering
- Zoom out to see clusters
- Zoom in to expand clusters into individual markers

### Coverage Analysis
- Zoom out to see overall coverage patterns
- Green = good, Red = needs improvement

### Distance Analysis
- Zoom to your area of interest first
- Click specific locations you care about
- Multiple clicks update the analysis

---

## Keyboard Shortcuts

- **Tab**: Navigate between analysis buttons
- **Enter/Space**: Toggle selected analysis
- **Escape**: Close popups and dialogs
- **Ctrl+B**: Toggle sidebar visibility

---

## Accessibility

All features are screen reader friendly:
- Buttons announce their state (on/off)
- Notifications are announced
- Keyboard navigation fully supported
- High contrast mode compatible

---

**This visual guide helps you understand what to expect when using the spatial analysis features!**
