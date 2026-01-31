// Appwrite Integration for Kitwe Green Spaces
// Replace your Flask API calls with these functions

// Initialize Appwrite
const { Client, Databases, Query } = Appwrite;

const client = new Client()
    .setEndpoint('https://cloud.appwrite.io/v1')
    .setProject('YOUR_PROJECT_ID'); // Replace with your project ID

const databases = new Databases(client);

// Configuration
const DATABASE_ID = 'kitwe_green_spaces';
const COLLECTION_ID = 'green_spaces';

// Replace your existing loadGreenSpaces function
async function loadGreenSpaces() {
    try {
        console.log('Loading green spaces from Appwrite...');
        
        const response = await databases.listDocuments(
            DATABASE_ID,
            COLLECTION_ID,
            [
                Query.limit(100), // Get all green spaces
                Query.orderAsc('name')
            ]
        );
        
        console.log(`Loaded ${response.documents.length} green spaces`);
        return response.documents;
        
    } catch (error) {
        console.error('Error loading green spaces:', error);
        
        // Fallback to static data if Appwrite fails
        console.log('Falling back to static data...');
        return window.fallbackGreenSpaces || [];
    }
}

// Replace your environmental data function
async function getEnvironmentalData() {
    try {
        const greenSpaces = await loadGreenSpaces();
        
        if (!greenSpaces.length) {
            return null;
        }
        
        // Calculate statistics
        const totalSpaces = greenSpaces.length;
        const totalArea = greenSpaces.reduce((sum, space) => 
            sum + (space.area_hectares || 0), 0);
        
        const wardCounts = {};
        const typeCounts = {};
        
        greenSpaces.forEach(space => {
            // Count by ward
            wardCounts[space.ward] = (wardCounts[space.ward] || 0) + 1;
            
            // Count by type
            typeCounts[space.type] = (typeCounts[space.type] || 0) + 1;
        });
        
        return {
            totalSpaces,
            totalArea: Math.round(totalArea * 100) / 100,
            averageSize: Math.round((totalArea / totalSpaces) * 100) / 100,
            wardCount: Object.keys(wardCounts).length,
            wardDistribution: wardCounts,
            typeDistribution: typeCounts,
            // Environmental calculations
            co2Absorbed: Math.round(totalArea * 22 * 100) / 100, // 22 tons CO2/hectare/year
            oxygenProduced: Math.round(totalArea * 16 * 100) / 100, // 16 tons O2/hectare/year
            airPurified: Math.round(totalArea * 27000 * 100) / 100, // 27,000 m³/hectare/year
            temperatureReduction: Math.round(totalArea * 0.5 * 100) / 100 // 0.5°C per hectare
        };
        
    } catch (error) {
        console.error('Error calculating environmental data:', error);
        return null;
    }
}

// Search function with Appwrite queries
async function searchGreenSpaces(searchTerm) {
    try {
        if (!searchTerm) {
            return await loadGreenSpaces();
        }
        
        const response = await databases.listDocuments(
            DATABASE_ID,
            COLLECTION_ID,
            [
                Query.search('name', searchTerm),
                Query.limit(50)
            ]
        );
        
        return response.documents;
        
    } catch (error) {
        console.error('Error searching green spaces:', error);
        return [];
    }
}

// Filter by ward
async function getGreenSpacesByWard(ward) {
    try {
        const response = await databases.listDocuments(
            DATABASE_ID,
            COLLECTION_ID,
            [
                Query.equal('ward', ward),
                Query.limit(50)
            ]
        );
        
        return response.documents;
        
    } catch (error) {
        console.error('Error filtering by ward:', error);
        return [];
    }
}

// Real-time updates (bonus feature!)
function subscribeToUpdates(callback) {
    try {
        client.subscribe(`databases.${DATABASE_ID}.collections.${COLLECTION_ID}.documents`, response => {
            console.log('Real-time update received:', response);
            callback(response);
        });
        
        console.log('Subscribed to real-time updates');
        
    } catch (error) {
        console.error('Error subscribing to updates:', error);
    }
}

// Export functions for use in your existing code
window.AppwriteAPI = {
    loadGreenSpaces,
    getEnvironmentalData,
    searchGreenSpaces,
    getGreenSpacesByWard,
    subscribeToUpdates
};

console.log('Appwrite integration loaded successfully!');