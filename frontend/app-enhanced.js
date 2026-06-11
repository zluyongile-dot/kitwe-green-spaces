// ========================================
// PHASE 2: EVENTS SYSTEM
// ========================================

async function loadEvents() {
    try {
        const response = await fetch('http://localhost:5000/api/events');
        const data = await response.json();
        
        if (data.status === 'success') {
            displayEvents(data.events);
        }
    } catch (error) {
        console.error('Error loading events:', error);
    }
}

function displayEvents(events) {
    const grid = document.getElementById('eventsGrid');
    grid.innerHTML = '';
    
    if (events.length === 0) {
        grid.innerHTML = '<p style="text-align: center; color: var(--text-secondary); grid-column: 1/-1;">No upcoming events</p>';
        return;
    }
    
    events.forEach(event => {
        const fillPercentage = (event.rsvp_count / event.max_participants) * 100;
        let badgeClass = 'open';
        let badgeText = 'Open';
        
        if (fillPercentage >= 100) {
            badgeClass = 'full';
            badgeText = 'Full';
        } else if (fillPercentage >= 80) {
            badgeClass = 'filling';
            badgeText = 'Filling Fast';
        }
        
        const eventDate = new Date(event.event_date);
        const formattedDate = eventDate.toLocaleDateString('en-US', { 
            month: 'short', 
            day: 'numeric', 
            year: 'numeric' 
        });
        
        const card = document.createElement('div');
        card.className = 'event-card';
        card.innerHTML = `
            <div class="event-card-header">
                <span class="event-badge ${badgeClass}">${badgeText}</span>
                <span class="event-date">${formattedDate}</span>
            </div>
            
            <h3 class="event-title">${event.title}</h3>
            <p class="event-description">${event.description || 'Join us for this community event!'}</p>
            
            <div class="event-details">
                <div class="event-detail-item">
                    <i class="fas fa-map-marker-alt"></i>
                    <span>${event.location_name || 'TBA'}</span>
                </div>
                <div class="event-detail-item">
                    <i class="fas fa-clock"></i>
                    <span>${event.start_time || '9:00 AM'} - ${event.end_time || '12:00 PM'}</span>
                </div>
                <div class="event-detail-item">
                    <i class="fas fa-users"></i>
                    <span>${event.rsvp_count}/${event.max_participants} registered</span>
                </div>
            </div>
            
            <div class="event-actions">
                <button class="btn-primary" onclick="openRSVPModal(${event.id})" ${fillPercentage >= 100 ? 'disabled' : ''}>
                    <i class="fas fa-check"></i> RSVP
                </button>
                <button class="btn-secondary">
                    <i class="fas fa-info-circle"></i> Details
                </button>
            </div>
        `;
        
        grid.appendChild(card);
    });
}

function openRSVPModal(eventId) {
    document.getElementById('rsvpEventId').value = eventId;
    document.getElementById('rsvpModal').classList.add('active');
}

function closeRSVPModal() {
    document.getElementById('rsvpModal').classList.remove('active');
    document.getElementById('rsvpForm').reset();
}

async function submitRSVP(e) {
    e.preventDefault();
    
    const eventId = document.getElementById('rsvpEventId').value;
    const name = document.getElementById('rsvpName').value;
    const email = document.getElementById('rsvpEmail').value;
    const phone = document.getElementById('rsvpPhone').value;
    
    try {
        const response = await fetch(`http://localhost:5000/api/events/${eventId}/rsvp`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, phone })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            alert('RSVP confirmed! See you at the event.');
            closeRSVPModal();
            loadEvents(); // Reload to update counts
        } else {
            alert(data.message || 'RSVP failed');
        }
    } catch (error) {
        console.error('Error submitting RSVP:', error);
        alert('Failed to submit RSVP. Please try again.');
    }
}

// ========================================
// PHASE 3: ANALYTICS
// ========================================

let trendsChart = null;
let coverageChart = null;

async function loadAnalytics() {
    try {
        // Load summary metrics
        const summaryResponse = await fetch('http://localhost:5000/api/analytics/summary');
        const summaryData = await summaryResponse.json();
        
        if (summaryData.status === 'success') {
            displayAnalyticsMetrics(summaryData.summary);
        }
        
        // Load trends data
        const trendsResponse = await fetch('http://localhost:5000/api/analytics/trends');
        const trendsData = await trendsResponse.json();
        
        if (trendsData.status === 'success') {
            displayTrendsChart(trendsData.trends);
        }
        
        // Load coverage data
        const coverageResponse = await fetch('http://localhost:5000/api/analytics/coverage');
        const coverageData = await coverageResponse.json();
        
        if (coverageData.status === 'success') {
            displayCoverageChart(coverageData.coverage);
        }
    } catch (error) {
        console.error('Error loading analytics:', error);
    }
}

function displayAnalyticsMetrics(summary) {
    const metricsGrid = document.getElementById('analyticsMetrics');
    metricsGrid.innerHTML = `
        <div class="metric-card">
            <span class="metric-value">${summary.total_green_spaces}</span>
            <span class="metric-label">Green Spaces</span>
        </div>
        <div class="metric-card">
            <span class="metric-value">${summary.total_area_hectares}</span>
            <span class="metric-label">Hectares</span>
        </div>
        <div class="metric-card">
            <span class="metric-value">${summary.trees_planted_ytd}</span>
            <span class="metric-label">Trees Planted YTD</span>
        </div>
        <div class="metric-card">
            <span class="metric-value">${summary.volunteers_engaged}</span>
            <span class="metric-label">Volunteers</span>
        </div>
        <div class="metric-card">
            <span class="metric-value">${summary.upcoming_events}</span>
            <span class="metric-label">Upcoming Events</span>
        </div>
        <div class="metric-card">
            <span class="metric-value">${summary.total_wards}</span>
            <span class="metric-label">Wards Covered</span>
        </div>
    `;
}

function displayTrendsChart(trends) {
    const ctx = document.getElementById('trendsChart').getContext('2d');
    
    if (trendsChart) {
        trendsChart.destroy();
    }
    
    trendsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: trends.months,
            datasets: [
                {
                    label: 'Trees Planted',
                    data: trends.trees_planted,
                    backgroundColor: '#4CAF50',
                    yAxisID: 'y'
                },
                {
                    label: 'Events Held',
                    data: trends.events_held,
                    backgroundColor: '#2196F3',
                    yAxisID: 'y1',
                    type: 'line',
                    borderColor: '#2196F3',
                    borderWidth: 2,
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            interaction: {
                mode: 'index',
                intersect: false
            },
            scales: {
                y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    title: {
                        display: true,
                        text: 'Trees Planted'
                    }
                },
                y1: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    title: {
                        display: true,
                        text: 'Events Held'
                    },
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });
}

function displayCoverageChart(coverage) {
    const ctx = document.getElementById('coverageChart').getContext('2d');
    
    if (coverageChart) {
        coverageChart.destroy();
    }
    
    const sortedCoverage = coverage.sort((a, b) => a.coverage - b.coverage);
    
    coverageChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sortedCoverage.map(w => w.ward),
            datasets: [{
                label: 'Coverage %',
                data: sortedCoverage.map(w => w.coverage),
                backgroundColor: sortedCoverage.map(w => {
                    if (w.coverage < 30) return '#D32F2F';
                    if (w.coverage < 60) return '#F57C00';
                    return '#388E3C';
                })
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    max: 100,
                    title: {
                        display: true,
                        text: 'Coverage Percentage'
                    }
                }
            }
        }
    });
}

// ========================================
// PHASE 4: PLANNER TOOLS
// ========================================

async function exportGeoJSON() {
    try {
        const response = await fetch('http://localhost:5000/api/export/geojson');
        const data = await response.json();
        
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'kitwe_green_spaces.geojson';
        a.click();
        URL.revokeObjectURL(url);
        
        alert('GeoJSON file downloaded successfully!');
    } catch (error) {
        console.error('Error exporting GeoJSON:', error);
        alert('Failed to export GeoJSON');
    }
}

async function generateGapReport() {
    try {
        const response = await fetch('http://localhost:5000/api/reports/gap-analysis');
        const data = await response.json();
        
        if (data.status === 'success') {
            // In production, this would generate a PDF
            // For now, show the data
            const report = data.report;
            let reportText = `GAP ANALYSIS REPORT\n`;
            reportText += `Generated: ${new Date(report.generated_at).toLocaleString()}\n\n`;
            reportText += `SUMMARY:\n`;
            reportText += `- Critical Wards: ${report.summary.critical_wards}\n`;
            reportText += `- Low Coverage Wards: ${report.summary.low_wards}\n`;
            reportText += `- Healthy Wards: ${report.summary.healthy_wards}\n\n`;
            reportText += `WARD DETAILS:\n`;
            
            report.wards.forEach(ward => {
                reportText += `\n${ward.ward}:\n`;
                reportText += `  Coverage: ${ward.coverage_percent}% (${ward.status.toUpperCase()})\n`;
                reportText += `  Spaces: ${ward.spaces}\n`;
                reportText += `  Recommendation: ${ward.recommendation}\n`;
            });
            
            // Download as text file (in production, would be PDF)
            const blob = new Blob([reportText], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'gap_analysis_report.txt';
            a.click();
            URL.revokeObjectURL(url);
            
            alert('Gap analysis report downloaded!');
        }
    } catch (error) {
        console.error('Error generating report:', error);
        alert('Failed to generate report');
    }
}

async function showHeatIslandData() {
    try {
        const response = await fetch('http://localhost:5000/api/heat-island/zones');
        const data = await response.json();
        
        if (data.status === 'success') {
            let message = 'HEAT ISLAND RISK ZONES:\n\n';
            data.zones.forEach(zone => {
                message += `${zone.zone} (${zone.ward})\n`;
                message += `  Risk: ${zone.risk.toUpperCase()}\n`;
                message += `  Avg Temp: ${zone.avg_temp}°C\n\n`;
            });
            alert(message);
        }
    } catch (error) {
        console.error('Error loading heat island data:', error);
        alert('Failed to load heat island data');
    }
}

async function showTimeline() {
    try {
        const response = await fetch('http://localhost:5000/api/timeline');
        const data = await response.json();
        
        if (data.status === 'success') {
            let message = 'DEVELOPMENT TIMELINE:\n\n';
            data.timeline.forEach(item => {
                message += `${item.date} - ${item.title}\n`;
                message += `  Status: ${item.status.toUpperCase()}\n`;
                message += `  ${item.description}\n\n`;
            });
            alert(message);
        }
    } catch (error) {
        console.error('Error loading timeline:', error);
        alert('Failed to load timeline');
    }
}

function showAPIDoc() {
    const apiDoc = `
KITWE GREEN SPACES API DOCUMENTATION

Base URL: http://localhost:5000

ENDPOINTS:

1. GET /api/green-spaces
   Returns all green spaces as GeoJSON

2. GET /api/events
   Returns all events with RSVP counts

3. POST /api/events/:id/rsvp
   RSVP to an event
   Body: { name, email, phone }

4. GET /api/analytics/summary
   Get overall analytics summary

5. GET /api/analytics/coverage
   Get ward coverage data

6. GET /api/analytics/trends
   Get time-series trends data

7. GET /api/export/geojson
   Export green spaces as GeoJSON

8. GET /api/reports/gap-analysis
   Generate gap analysis report

9. GET /api/heat-island/zones
   Get heat island risk zones

10. GET /api/timeline
    Get development timeline

For full documentation, visit: https://github.com/your-repo/api-docs
    `;
    
    alert(apiDoc);
}

// ========================================
// INITIALIZE ON TAB CHANGE
// ========================================

// Override tab navigation to load data
const originalTabClick = navTabs.forEach;
navTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const tabName = tab.dataset.tab;
        
        // Load data when switching tabs
        if (tabName === 'events') {
            loadEvents();
        } else if (tabName === 'analytics') {
            loadAnalytics();
        }
    });
});
