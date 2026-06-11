# UI Enhancement - Design Document

## Architecture Overview

### Component Structure
```
┌─────────────────────────────────────────────────────┐
│  Top Navigation Bar                                  │
│  [Logo] [Map] [Events] [Analytics] [Planner] [User] │
└─────────────────────────────────────────────────────┘
┌──────────────────────┬──────────────────────────────┐
│                      │                              │
│   Main Content       │   Right Sidebar Panel        │
│   (Tab-based)        │   - Coverage Metrics         │
│                      │   - Quick Stats              │
│   - Map View         │   - Filters                  │
│   - Events List      │   - Legend                   │
│   - Analytics Charts │                              │
│   - Planner Tools    │                              │
│                      │                              │
└──────────────────────┴──────────────────────────────┘
```

## 1. Visual Design System

### Color Palette
```css
/* Primary - Green Forward */
--primary-green: #2E7D32;
--primary-light: #4CAF50;
--primary-dark: #1B5E20;

/* Gap Analysis Colors */
--critical-gap: #D32F2F;      /* Red - Critical */
--low-coverage: #F57C00;      /* Amber - Low */
--healthy-coverage: #388E3C;  /* Green - Healthy */

/* UI Elements */
--background: #FAFAFA;
--surface: #FFFFFF;
--text-primary: #212121;
--text-secondary: #757575;
--border: #E0E0E0;
```

### Typography
- **Headings**: Inter, 600-700 weight
- **Body**: Inter, 400 weight
- **Monospace** (API/Code): JetBrains Mono

### Spacing System
- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px

## 2. Navigation Bar Design

### Structure
```html
<nav class="top-nav">
  <div class="nav-left">
    <img src="logo.svg" class="logo" />
    <span class="app-name">Kitwe Green Spaces</span>
  </div>
  
  <div class="nav-center">
    <button class="nav-tab active">Map</button>
    <button class="nav-tab">Events</button>
    <button class="nav-tab">Analytics</button>
    <button class="nav-tab" data-role="planner">Planner</button>
  </div>
  
  <div class="nav-right">
    <input type="search" placeholder="Search locations..." />
    <div class="user-avatar">
      <img src="avatar.jpg" />
      <span class="user-name">John Doe</span>
    </div>
  </div>
</nav>
```

### Behavior
- Active tab highlighted with green underline
- Planner tab only visible for city_council/admin users
- Search bar expands on focus
- User avatar shows dropdown menu on click

## 3. Map View Enhancements

### Gap Analysis Layer
```javascript
// Color zones based on coverage
function getZoneColor(coverage) {
  if (coverage < 0.3) return '#D32F2F';  // Critical
  if (coverage < 0.6) return '#F57C00';  // Low
  return '#388E3C';                       // Healthy
}

// Coverage calculation
coverage = green_space_area / total_ward_area
```

### Map Legend
```
Legend:
🟢 Healthy Coverage (>60%)
🟠 Low Coverage (30-60%)
🔴 Critical Gap (<30%)
📍 Green Space Marker
```

### Map Controls
- Zoom in/out buttons
- Reset view button
- Layer toggle (satellite/street)
- Fullscreen button
- Current location button

## 4. Right Sidebar Panel

### Coverage Metrics Section
```html
<div class="coverage-panel">
  <h3>Ward Coverage</h3>
  
  <div class="ward-metric">
    <span class="ward-name">City Centre</span>
    <div class="progress-bar">
      <div class="progress-fill" style="width: 75%; background: #388E3C"></div>
    </div>
    <span class="coverage-value">75%</span>
  </div>
  
  <!-- Repeat for each ward -->
</div>
```

### Quick Stats
- Total Green Spaces: 27
- Total Area: 1.2M m²
- Average Coverage: 58%
- Critical Zones: 3

## 5. Events Tab

### Event Card Design
```html
<div class="event-card">
  <div class="event-header">
    <span class="event-badge filling">Filling Fast</span>
    <span class="event-date">Dec 15, 2024</span>
  </div>
  
  <h3 class="event-title">Tree Planting at Parklands</h3>
  
  <div class="event-details">
    <p>📍 Parklands Community Park</p>
    <p>⏰ 9:00 AM - 12:00 PM</p>
    <p>👥 45/50 registered</p>
  </div>
  
  <div class="event-actions">
    <button class="btn-primary">RSVP Now</button>
    <button class="btn-secondary">Details</button>
  </div>
</div>
```

### RSVP Status Badges
- **Open**: Green badge, plenty of spots
- **Filling**: Amber badge, <20% spots left
- **Full**: Red badge, waitlist available
- **Upcoming**: Blue badge, starts soon
- **Completed**: Gray badge, past event

### Event Filters
- Date range picker
- Ward filter
- Event type (planting, cleanup, workshop)
- RSVP status filter

## 6. Analytics Tab

### Dual-Axis Chart
```javascript
// Chart.js configuration
{
  type: 'bar',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [
      {
        label: 'Trees Planted',
        data: [120, 150, 180, 200, 220, 250],
        backgroundColor: '#4CAF50',
        yAxisID: 'y'
      },
      {
        label: 'Events Held',
        data: [3, 4, 5, 6, 5, 7],
        backgroundColor: '#2196F3',
        yAxisID: 'y1'
      }
    ]
  }
}
```

### Summary Metrics
- Trees planted this year: 1,320
- Events held: 35
- Volunteers engaged: 450
- Area improved: 15,000 m²

### Additional Charts
- Coverage by ward (horizontal bar)
- Green space types (pie chart)
- Monthly growth trend (line chart)

## 7. Planner Tab

### Tool Cards
```html
<div class="planner-tools">
  <div class="tool-card">
    <div class="tool-icon">📦</div>
    <h3>GIS Export</h3>
    <p>Download shapefiles for QGIS/ArcGIS</p>
    <button class="btn-primary">Export Shapefile</button>
  </div>
  
  <div class="tool-card">
    <div class="tool-icon">📊</div>
    <h3>Gap Analysis Report</h3>
    <p>Generate PDF with coverage analysis</p>
    <button class="btn-primary">Generate Report</button>
  </div>
  
  <div class="tool-card">
    <div class="tool-icon">🌡️</div>
    <h3>Heat Island Risk</h3>
    <p>Overlay temperature risk zones</p>
    <button class="btn-primary">Show Overlay</button>
  </div>
  
  <div class="tool-card">
    <div class="tool-icon">📅</div>
    <h3>Development Timeline</h3>
    <p>Track project progress over time</p>
    <button class="btn-primary">View Timeline</button>
  </div>
  
  <div class="tool-card">
    <div class="tool-icon">🔌</div>
    <h3>API Documentation</h3>
    <p>REST API for data integration</p>
    <button class="btn-primary">View Docs</button>
  </div>
</div>
```

### Export Flow
1. User clicks "Export Shapefile"
2. Modal opens with format options (SHP, GeoJSON, KML)
3. User selects layers to include
4. User clicks "Download"
5. Backend generates file and returns download link

### Report Generation
1. User clicks "Generate Report"
2. Modal shows report options (date range, wards, metrics)
3. User configures and clicks "Generate"
4. Backend creates PDF with:
   - Executive summary
   - Coverage maps
   - Ward-by-ward analysis
   - Recommendations
5. PDF downloads automatically

## 8. Database Schema Extensions

### Events Table
```sql
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    event_type VARCHAR(50),
    location_id INTEGER REFERENCES green_spaces(id),
    event_date TIMESTAMP NOT NULL,
    start_time TIME,
    end_time TIME,
    max_participants INTEGER,
    current_participants INTEGER DEFAULT 0,
    status VARCHAR(20) DEFAULT 'open',
    created_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### RSVPs Table
```sql
CREATE TABLE rsvps (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(id),
    user_id INTEGER REFERENCES users(id),
    status VARCHAR(20) DEFAULT 'confirmed',
    rsvp_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(event_id, user_id)
);
```

### Coverage Metrics Table
```sql
CREATE TABLE ward_coverage (
    id SERIAL PRIMARY KEY,
    ward VARCHAR(100) NOT NULL,
    total_area_m2 FLOAT,
    green_space_area_m2 FLOAT,
    coverage_percentage FLOAT,
    status VARCHAR(20),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Heat Island Data Table
```sql
CREATE TABLE heat_island_zones (
    id SERIAL PRIMARY KEY,
    zone_name VARCHAR(100),
    risk_level VARCHAR(20),
    avg_temperature FLOAT,
    geom GEOMETRY(Polygon, 4326),
    last_measured TIMESTAMP
);
```

## 9. API Endpoints

### Events
- `GET /api/events` - List all events
- `GET /api/events/:id` - Get event details
- `POST /api/events` - Create event (admin/council)
- `PUT /api/events/:id` - Update event
- `DELETE /api/events/:id` - Delete event

### RSVPs
- `POST /api/events/:id/rsvp` - RSVP to event
- `DELETE /api/events/:id/rsvp` - Cancel RSVP
- `GET /api/events/:id/participants` - List participants

### Analytics
- `GET /api/analytics/summary` - Overall metrics
- `GET /api/analytics/coverage` - Ward coverage data
- `GET /api/analytics/trends` - Time-series data

### Planner Tools
- `GET /api/export/shapefile` - Generate shapefile
- `GET /api/export/geojson` - Export as GeoJSON
- `POST /api/reports/gap-analysis` - Generate PDF report
- `GET /api/heat-island/zones` - Get heat risk data
- `GET /api/timeline` - Development timeline data

## 10. Implementation Phases

### Phase 1: Visual Polish (Week 1)
- New navigation bar
- Color system implementation
- Map legend and controls
- Right sidebar panel

### Phase 2: Events System (Week 2)
- Events database tables
- Event CRUD endpoints
- RSVP functionality
- Event cards UI

### Phase 3: Analytics (Week 3)
- Coverage calculation
- Chart implementation
- Summary metrics
- Gap analysis visualization

### Phase 4: Planner Tools (Week 4)
- Shapefile export
- PDF report generation
- Heat island overlay
- Timeline view
- API documentation

## 11. Responsive Design

### Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

### Mobile Adaptations
- Navigation becomes hamburger menu
- Sidebar becomes bottom sheet
- Map takes full width
- Tool cards stack vertically
- Charts resize responsively

## 12. Performance Considerations

- Lazy load event images
- Paginate events list (20 per page)
- Cache coverage calculations
- Debounce search input
- Use map clustering for many markers
- Optimize shapefile generation
- Generate reports asynchronously
