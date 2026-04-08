// Global variables
let map;
let allMarkers = [];
let allGreenSpaces = [];

// Initialize the map
function initializeMap() {
    // Initialize the map centered on Kitwe
    map = L.map('map').setView([-12.8130, 28.2200], 13);

    // Add OpenStreetMap tiles with multiple options
    const osmStandard = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    });
    
    const osmHot = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors, Tiles style by Humanitarian OpenStreetMap Team'
    });
    
    const cartoDB = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors © CARTO'
    });
    
    // Add default layer
    osmStandard.addTo(map);
    
    // Layer control for switching between map styles
    const baseMaps = {
        "Standard": osmStandard,
        "Humanitarian": osmHot,
        "Light Theme": cartoDB
    };

    // Add layer groups to map
    Object.values(layerGroups).forEach(layer => layer.addTo(map));
    
    // Add layer control for switching map styles and toggling green space types
    const overlayMaps = {
        "Parks": layerGroups.park,
        "Gardens": layerGroups.garden,
        "Forests": layerGroups.forest,
        "Recreational": layerGroups.recreational,
        "Other": layerGroups.other
    };
    
    L.control.layers(baseMaps, overlayMaps, {
        position: 'topright',
        collapsed: false
    }).addTo(map);
    
    console.log('Map initialized successfully');
}

// Layer groups for different types
const layerGroups = {
    park: L.layerGroup(),
    garden: L.layerGroup(),
    forest: L.layerGroup(),
    recreational: L.layerGroup(),
    other: L.layerGroup()
};

// Add layer groups to map
Object.values(layerGroups).forEach(layer => layer.addTo(map));

// Store all markers for filtering
let allMarkers = [];
let allGreenSpaces = [];

// Color scheme for different types
const typeColors = {
    park: '#4CAF50',
    garden: '#2196F3',
    forest: '#9C27B0',
    recreational: '#FF9800',
    'golf course': '#795548',
    other: '#607D8B'
};

// Fetch green spaces from your Flask API
async function loadGreenSpaces() {
    console.log('Loading green spaces from API...');
    try {
        // Add cache-busting parameter to ensure fresh data
        const timestamp = new Date().getTime();
        const response = await fetch(`http://127.0.0.1:5000/api/green-spaces?t=${timestamp}`, {
            cache: 'no-cache',
            headers: {
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache'
            }
        });
        console.log('API response status:', response.status);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Received data:', data);
        console.log('Number of features:', data.features ? data.features.length : 'No features array');
        
        allGreenSpaces = data.features;
        console.log(`Loaded ${allGreenSpaces.length} green spaces`);
        
        // Log first few spaces to verify data
        if (allGreenSpaces.length > 0) {
            console.log('First 3 spaces:', allGreenSpaces.slice(0, 3).map(s => s.properties.name));
        }
        
        displayGreenSpaces(allGreenSpaces);
        updateStatistics(allGreenSpaces);
        populateWardFilter(allGreenSpaces);
        
        // Notify that search is now ready
        console.log('✅ Search is ready! You can now search through', allGreenSpaces.length, 'green spaces');
        
        // Hide loading overlay if it exists
        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.style.display = 'none';
        }
        
    } catch (error) {
        console.error('Error loading green spaces:', error);
        showNotification('Error loading green spaces. Please try again.', 'error');
        
        // Show error in loading overlay if it exists
        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.innerHTML = `
                <div class="alert alert-danger">
                    <h4>Loading Error</h4>
                    <p>Failed to load green spaces: ${error.message}</p>
                    <button onclick="location.reload()" class="btn btn-primary mt-2">Retry</button>
                </div>
            `;
        }
    }
}

// Display green spaces on map
function displayGreenSpaces(greenSpaces) {
    // Clear existing markers
    allMarkers.forEach(marker => marker.remove());
    allMarkers = [];
    Object.values(layerGroups).forEach(layer => layer.clearLayers());
    
    // Add new markers
    greenSpaces.forEach(feature => {
        const props = feature.properties;
        const coords = feature.geometry.coordinates;
        
        // Determine color based on type
        const color = typeColors[props.type] || typeColors.other;
        
        // Create custom icon
        const icon = L.divIcon({
            html: `<div style="
                width: 24px;
                height: 24px;
                background-color: ${color};
                border: 2px solid white;
                border-radius: 50%;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
                font-size: 12px;
            ">${props.type.charAt(0).toUpperCase()}</div>`,
            iconSize: [24, 24],
            className: 'custom-marker'
        });
        
        // Create marker
        const marker = L.marker([coords[1], coords[0]], { icon: icon })
            .addTo(layerGroups[props.type] || layerGroups.other);
        
        // Create popup content
        const popupContent = `
            <div class="popup-content" style="min-width: 250px;">
                <h6 style="color: ${color}; margin-bottom: 10px;">
                    <i class="fas fa-tree me-2"></i>${props.name}
                </h6>
                <table class="table table-sm">
                    <tr>
                        <td><strong>Type:</strong></td>
                        <td>${props.type}</td>
                    </tr>
                    <tr>
                        <td><strong>Area:</strong></td>
                        <td>${props.area_sq_m ? props.area_sq_m.toLocaleString() + ' m²' : 'N/A'}</td>
                    </tr>
                    <tr>
                        <td><strong>Ward:</strong></td>
                        <td>${props.ward || 'N/A'}</td>
                    </tr>
                </table>
                <div class="d-grid gap-2">
                    <button class="btn btn-sm btn-primary-custom" onclick="zoomToLocation(${coords[1]}, ${coords[0]})">
                        <i class="fas fa-search-location me-1"></i>Zoom In
                    </button>
                    <a href="feedback.html?space=${props.id}" class="btn btn-sm btn-outline-danger">
                        <i class="fas fa-flag me-1"></i>Report Issue
                    </a>
                </div>
            </div>
        `;
        
        marker.bindPopup(popupContent);
        allMarkers.push(marker);
    });
    
    // Update layer controls
    updateLayerControls();
}

// Update statistics
function updateStatistics(greenSpaces) {
    const totalSpaces = greenSpaces.length;
    const totalAreaSqM = greenSpaces.reduce((sum, space) => sum + (space.properties.area_sq_m || 0), 0);
    const totalAreaHa = Math.round(totalAreaSqM / 10000); // Convert to hectares
    const wards = [...new Set(greenSpaces.map(space => space.properties.ward).filter(Boolean))];
    
    // Update sidebar stats
    const statSpaces = document.getElementById('statSpaces');
    const statArea = document.getElementById('statArea');
    const statWards = document.getElementById('statWards');
    
    if (statSpaces) statSpaces.textContent = totalSpaces;
    if (statArea) statArea.textContent = totalAreaHa;
    if (statWards) statWards.textContent = wards.length;
    
    // Also update any other stat elements that might exist
    const totalSpacesEl = document.getElementById('totalSpaces');
    const totalAreaEl = document.getElementById('totalArea');
    const wardsCoveredEl = document.getElementById('wardsCovered');
    
    if (totalSpacesEl) totalSpacesEl.textContent = totalSpaces;
    if (totalAreaEl) totalAreaEl.textContent = totalAreaSqM.toLocaleString() + ' m²';
    if (wardsCoveredEl) wardsCoveredEl.textContent = wards.length;
    
    console.log(`📊 Stats updated: ${totalSpaces} spaces, ${totalAreaHa} ha, ${wards.length} wards`);
}

// Populate ward filter
function populateWardFilter(greenSpaces) {
    const wardSelect = document.getElementById('filterWard');
    const wards = [...new Set(greenSpaces.map(space => space.properties.ward).filter(Boolean))].sort();
    
    // Clear existing options (keep "All Wards")
    while (wardSelect.options.length > 1) {
        wardSelect.remove(1);
    }
    
    // Add ward options
    wards.forEach(ward => {
        const option = document.createElement('option');
        option.value = ward;
        option.textContent = ward;
        wardSelect.appendChild(option);
    });
}

// Update layer controls
function updateLayerControls() {
    // This function can be expanded to add layer control toggles
}

// Filter green spaces
function filterGreenSpaces() {
    const typeFilter = document.getElementById('filterType').value;
    const wardFilter = document.getElementById('filterWard').value;
    const minArea = parseInt(document.getElementById('areaRange').value);
    
    let filtered = allGreenSpaces;
    
    // Filter by type
    if (typeFilter !== 'all') {
        filtered = filtered.filter(space => space.properties.type === typeFilter);
    }
    
    // Filter by ward
    if (wardFilter !== 'all') {
        filtered = filtered.filter(space => space.properties.ward === wardFilter);
    }
    
    // Filter by area
    filtered = filtered.filter(space => (space.properties.area_sq_m || 0) >= minArea);
    
    displayGreenSpaces(filtered);
    updateStatistics(filtered);
}

// Search functionality
function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchClear = document.getElementById('searchClear');
    const searchResults = document.getElementById('searchResults');
    
    if (!searchInput || !searchClear || !searchResults) {
        console.error('Search elements not found:', {
            searchInput: !!searchInput,
            searchClear: !!searchClear, 
            searchResults: !!searchResults
        });
        return;
    }
    
    console.log('Setting up search functionality...');
    
    // Search on input
    searchInput.addEventListener('input', performSearch);
    
    // Clear search
    searchClear.addEventListener('click', () => {
        searchInput.value = '';
        searchResults.innerHTML = '';
        searchResults.classList.add('d-none');
    });
    
    function performSearch() {
        const query = searchInput.value.toLowerCase().trim();
        searchResults.innerHTML = '';
        
        if (!query) {
            searchResults.classList.add('d-none');
            return;
        }
        
        if (!allGreenSpaces || allGreenSpaces.length === 0) {
            console.log('No green spaces data available for search');
            searchResults.innerHTML = '<div class="text-muted p-2">Loading data...</div>';
            searchResults.classList.remove('d-none');
            return;
        }
        
        console.log(`Searching for "${query}" in ${allGreenSpaces.length} spaces`);
        
        const results = allGreenSpaces.filter(space =>
            space.properties.name.toLowerCase().includes(query) ||
            space.properties.ward?.toLowerCase().includes(query) ||
            space.properties.type.toLowerCase().includes(query)
        );
        
        console.log(`Found ${results.length} search results`);
        
        if (results.length > 0) {
            searchResults.classList.remove('d-none');
            results.forEach(space => {
                const resultItem = document.createElement('div');
                resultItem.className = 'search-result-item p-2 border-bottom';
                resultItem.innerHTML = `
                    <strong>${space.properties.name}</strong>
                    <br>
                    <small>${space.properties.type} • ${space.properties.ward || 'N/A'}</small>
                `;
                resultItem.style.cursor = 'pointer';
                resultItem.addEventListener('click', () => {
                    const coords = space.geometry.coordinates;
                    zoomToLocation(coords[1], coords[0]);
                    searchResults.classList.add('d-none');
                    searchInput.value = space.properties.name;
                });
                searchResults.appendChild(resultItem);
            });
        } else {
            searchResults.innerHTML = '<div class="text-muted p-2">No results found</div>';
            searchResults.classList.remove('d-none');
        }
    }
}

// Utility functions
function zoomToLocation(lat, lng) {
    map.setView([lat, lng], 16);
    // Open popup for the marker at this location
    allMarkers.forEach(marker => {
        const markerLatLng = marker.getLatLng();
        if (markerLatLng.lat === lat && markerLatLng.lng === lng) {
            marker.openPopup();
        }
    });
}

function showNotification(message, type = 'info') {
    // Create and show a Bootstrap toast notification
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-bg-${type === 'error' ? 'danger' : 'success'} border-0`;
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                <i class="fas fa-${type === 'error' ? 'exclamation-circle' : 'check-circle'} me-2"></i>
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    const toastContainer = document.getElementById('toastContainer') || (() => {
        const container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        document.body.appendChild(container);
        return container;
    })();
    
    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Remove toast after it hides
    toast.addEventListener('hidden.bs.toast', () => {
        toast.remove();
    });
}

// Initialize application
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing application...');
    
    // Initialize map first
    initializeMap();
    
    // Set up search (before loading data so it's ready)
    setupSearch();
    
    // Then load data
    loadGreenSpaces();
    
    // Event listeners for filters
    document.getElementById('applyFilters').addEventListener('click', filterGreenSpaces);
    document.getElementById('resetFilters').addEventListener('click', () => {
        document.getElementById('filterType').value = 'all';
        document.getElementById('filterWard').value = 'all';
        document.getElementById('areaRange').value = 0;
        document.getElementById('areaValue').textContent = '0';
        displayGreenSpaces(allGreenSpaces);
        updateStatistics(allGreenSpaces);
    });
    
    // Update area range display
    document.getElementById('areaRange').addEventListener('input', (e) => {
        document.getElementById('areaValue').textContent = 
            parseInt(e.target.value).toLocaleString();
    });
});