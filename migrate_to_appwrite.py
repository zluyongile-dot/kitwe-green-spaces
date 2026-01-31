#!/usr/bin/env python3
"""
Migration script to move from Flask backend to Appwrite
This will help you export your data and create Appwrite integration
"""

import json
import os
from datetime import datetime

def export_green_spaces_data():
    """Export green spaces data for Appwrite import"""
    
    # Sample data structure (replace with your actual data)
    green_spaces = [
        {
            "name": "Kitwe Central Park",
            "ward": "Central Ward",
            "area_hectares": 15.5,
            "latitude": -12.8044,
            "longitude": 28.2136,
            "type": "Urban Park",
            "description": "Large central park with recreational facilities",
            "facilities": "Playground, Walking paths, Benches",
            "accessibility": "Wheelchair accessible",
            "environmental_impact": "High - provides urban cooling and air purification"
        },
        # Add your other 50 green spaces here...
    ]
    
    # Export to JSON for Appwrite import
    export_data = {
        "database_id": "kitwe_green_spaces",
        "collection_id": "green_spaces", 
        "documents": green_spaces,
        "exported_at": datetime.now().isoformat(),
        "total_documents": len(green_spaces)
    }
    
    with open('appwrite_import_data.json', 'w') as f:
        json.dump(export_data, f, indent=2)
    
    print(f"✅ Exported {len(green_spaces)} green spaces to appwrite_import_data.json")
    return export_data

def create_appwrite_config():
    """Create Appwrite configuration file"""
    
    config = {
        "project_id": "YOUR_APPWRITE_PROJECT_ID",
        "endpoint": "https://cloud.appwrite.io/v1",
        "database_id": "kitwe_green_spaces",
        "collection_id": "green_spaces",
        "api_key": "YOUR_API_KEY_HERE"
    }
    
    with open('appwrite_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ Created appwrite_config.json")
    print("📝 Update the project_id and api_key with your actual values")

def create_frontend_integration():
    """Create JavaScript file for Appwrite integration"""
    
    js_code = '''
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
        
        console.log('✅ Subscribed to real-time updates');
        
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

console.log('🚀 Appwrite integration loaded successfully!');
'''
    
    with open('frontend/appwrite-integration.js', 'w') as f:
        f.write(js_code)
    
    print("✅ Created frontend/appwrite-integration.js")

def create_html_integration():
    """Create HTML snippet for Appwrite integration"""
    
    html_snippet = '''
<!-- Add this to your HTML head section -->
<script src="https://cdn.jsdelivr.net/npm/appwrite@15.0.0"></script>
<script src="appwrite-integration.js"></script>

<!-- Update your existing JavaScript to use Appwrite -->
<script>
// Replace your existing API calls with Appwrite functions
document.addEventListener('DOMContentLoaded', async function() {
    try {
        // Load green spaces using Appwrite
        const greenSpaces = await window.AppwriteAPI.loadGreenSpaces();
        
        // Your existing map initialization code
        initializeMap(greenSpaces);
        
        // Load environmental data
        const envData = await window.AppwriteAPI.getEnvironmentalData();
        updateStatistics(envData);
        
        // Optional: Subscribe to real-time updates
        window.AppwriteAPI.subscribeToUpdates((update) => {
            console.log('Data updated in real-time!');
            // Refresh your map or statistics
        });
        
    } catch (error) {
        console.error('Error initializing Appwrite:', error);
        // Fallback to your existing static data
    }
});
</script>
'''
    
    with open('appwrite_html_integration.html', 'w') as f:
        f.write(html_snippet)
    
    print("✅ Created appwrite_html_integration.html")

def main():
    print("🚀 Migrating Kitwe Green Spaces to Appwrite")
    print("=" * 50)
    
    # Create necessary directories
    os.makedirs('frontend', exist_ok=True)
    
    # Export data
    export_green_spaces_data()
    
    # Create configuration
    create_appwrite_config()
    
    # Create frontend integration
    create_frontend_integration()
    create_html_integration()
    
    print("\n🎉 Migration files created successfully!")
    print("\n📋 Next Steps:")
    print("1. Go to https://cloud.appwrite.io and create a project")
    print("2. Create database 'kitwe_green_spaces' with collection 'green_spaces'")
    print("3. Import data from appwrite_import_data.json")
    print("4. Update appwrite_config.json with your project ID")
    print("5. Add appwrite-integration.js to your frontend")
    print("6. Update your HTML with the integration snippet")
    
    print("\n✨ Benefits of Appwrite:")
    print("- No server maintenance")
    print("- Real-time updates")
    print("- Built-in security")
    print("- Free hosting")
    print("- Professional architecture")
    
    print("\n📚 Check APPWRITE_DEPLOYMENT.md for detailed instructions")

if __name__ == "__main__":
    main()