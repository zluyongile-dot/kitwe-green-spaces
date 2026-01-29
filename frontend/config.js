// Configuration for different environments
const CONFIG = {
    // Local development
    local: {
        API_BASE_URL: 'http://127.0.0.1:5000'
    },
    
    // Production deployment
    production: {
        API_BASE_URL: 'https://YOUR_ACTUAL_RAILWAY_URL_HERE' // Replace with your Railway URL
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