// Configuration for different environments
const CONFIG = {
    // Local development
    local: {
        API_BASE_URL: 'http://127.0.0.1:5000'
    },
    
    // Production deployment
    production: {
        API_BASE_URL: 'https://kitwe-green-spaces-fze8.vercel.app', // Vercel deployment
        USE_FALLBACK: true // Use fallback data when backend is not available
    }
};

// Auto-detect environment
const isLocal = window.location.hostname === 'localhost' || 
                window.location.hostname === '127.0.0.1' ||
                window.location.hostname === '' ||
                window.location.port === '8000'; // Local HTTP server

// Export the appropriate config
window.APP_CONFIG = isLocal ? CONFIG.local : CONFIG.production;

console.log('🔧 Environment:', isLocal ? 'Local Development' : 'Production (GitHub Pages)');
console.log('🌐 API Base URL:', window.APP_CONFIG.API_BASE_URL);
console.log('📍 Current hostname:', window.location.hostname);

// Fallback data loader function
window.loadGreenSpacesWithFallback = async function() {
    try {
        // Try to load from API first
        const timestamp = new Date().getTime();
        const response = await fetch(`${window.APP_CONFIG.API_BASE_URL}/api/green-spaces?t=${timestamp}`, {
            cache: 'no-cache',
            headers: {
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache'
            }
        });
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        console.log('✅ Loaded data from API:', data.features?.length || 0, 'green spaces');
        return data;
        
    } catch (error) {
        console.log('⚠️ API not available, using fallback data:', error.message);
        
        // Use fallback data if available
        if (window.FALLBACK_GREEN_SPACES) {
            console.log('✅ Using fallback data:', window.FALLBACK_GREEN_SPACES.features.length, 'green spaces');
            return window.FALLBACK_GREEN_SPACES;
        } else {
            console.error('❌ No fallback data available');
            throw new Error('No data source available');
        }
    }
};