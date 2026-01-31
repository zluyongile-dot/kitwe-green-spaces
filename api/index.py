from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
import random
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Supabase configuration
SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://your-project.supabase.co')
SUPABASE_ANON_KEY = os.environ.get('SUPABASE_ANON_KEY', 'your-anon-key')

def get_supabase_headers():
    """Get headers for Supabase API requests"""
    return {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
        'Content-Type': 'application/json'
    }

@app.route('/')
def home():
    return jsonify({
        "message": "Kitwe Green Spaces API - Vercel + Supabase REST API",
        "status": "running",
        "endpoints": [
            "/api/green-spaces",
            "/api/environmental-data",
            "/test-db"
        ]
    })

@app.route('/test-db')
def test_db():
    """Test Supabase connection via REST API"""
    try:
        # Test connection by getting count of green spaces
        url = f"{SUPABASE_URL}/rest/v1/green_spaces?select=count"
        headers = get_supabase_headers()
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "status": "success",
                "message": "Supabase connection successful!",
                "platform": "Vercel + Supabase REST API",
                "response_code": response.status_code
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Supabase connection failed: {response.status_code}",
                "details": response.text
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": f"Connection test failed: {str(e)}"
        }), 500

@app.route('/api/green-spaces')
def get_green_spaces():
    """Get all green spaces as GeoJSON using Supabase REST API"""
    try:
        # Get all green spaces from Supabase
        url = f"{SUPABASE_URL}/rest/v1/green_spaces?select=*&order=name"
        headers = get_supabase_headers()
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            # Fallback to static data if Supabase fails
            return get_fallback_green_spaces()
        
        spaces = response.json()
        
        # Convert to GeoJSON
        features = []
        for space in spaces:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(space['longitude']), float(space['latitude'])]
                },
                "properties": {
                    "id": space['id'],
                    "name": space['name'],
                    "type": space['type'],
                    "area_hectares": float(space['area_hectares']) if space['area_hectares'] else 0,
                    "ward": space['ward'],
                    "description": space['description'],
                    "facilities": space['facilities'],
                    "accessibility": space['accessibility'],
                    "environmental_impact": space['environmental_impact']
                }
            }
            features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        
        return jsonify(geojson)
        
    except Exception as e:
        # Fallback to static data
        return get_fallback_green_spaces()

def get_fallback_green_spaces():
    """Fallback green spaces data if Supabase is not available"""
    # Static data for demonstration
    fallback_spaces = [
        {
            "id": 1,
            "name": "Kitwe City Square",
            "type": "public_square",
            "area_hectares": 1.8,
            "ward": "City Centre",
            "latitude": -12.817778,
            "longitude": 28.213611,
            "description": "Central public square in the heart of Kitwe",
            "facilities": "Benches, fountains, walkways",
            "accessibility": "Fully accessible",
            "environmental_impact": "Urban cooling, air purification"
        },
        {
            "id": 2,
            "name": "Central Park Kitwe",
            "type": "park",
            "area_hectares": 3.5,
            "ward": "City Centre",
            "latitude": -12.815000,
            "longitude": 28.210000,
            "description": "Main recreational park in Kitwe city center",
            "facilities": "Playground, walking paths, benches, sports area",
            "accessibility": "Wheelchair accessible",
            "environmental_impact": "High - provides urban cooling and biodiversity"
        },
        {
            "id": 3,
            "name": "Copperbelt University Arboretum",
            "type": "forest",
            "area_hectares": 4.2,
            "ward": "Riverside",
            "latitude": -12.825556,
            "longitude": 28.226389,
            "description": "Educational forest area with diverse tree species",
            "facilities": "Nature trails, research areas, educational signage",
            "accessibility": "Partially accessible",
            "environmental_impact": "Very high - carbon sequestration, biodiversity conservation"
        }
        # Add more fallback data as needed
    ]
    
    features = []
    for space in fallback_spaces:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [space['longitude'], space['latitude']]
            },
            "properties": space
        }
        features.append(feature)
    
    return jsonify({
        "type": "FeatureCollection",
        "features": features,
        "fallback": True,
        "message": "Using fallback data - configure Supabase for full dataset"
    })

@app.route('/api/environmental-data')
def get_environmental_data():
    """Get environmental monitoring data"""
    try:
        # Try to get real data from Supabase
        url = f"{SUPABASE_URL}/rest/v1/green_spaces?select=area_hectares,ward,type"
        headers = get_supabase_headers()
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            spaces = response.json()
            total_area = sum(float(space.get('area_hectares', 0)) for space in spaces)
            ward_count = len(set(space.get('ward') for space in spaces if space.get('ward')))
            type_count = len(set(space.get('type') for space in spaces if space.get('type')))
            total_spaces = len(spaces)
        else:
            # Fallback values
            total_area = 261.5
            ward_count = 16
            type_count = 7
            total_spaces = 51
        
        # Calculate environmental metrics
        base_aqi = max(20, 50 - (total_area / 100) * 5)
        base_temp = 28 + random.uniform(-2, 3)
        humidity = 65 + random.uniform(-10, 15)
        
        # Generate historical data
        historical_data = []
        for i in range(7):
            date = datetime.now() - timedelta(days=6-i)
            historical_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'aqi': max(20, base_aqi + random.uniform(-5, 5)),
                'temperature': base_temp + random.uniform(-3, 3),
                'humidity': max(40, min(80, humidity + random.uniform(-5, 5)))
            })
        
        environmental_data = {
            'current_readings': {
                'aqi': round(base_aqi),
                'temperature': round(base_temp, 1),
                'humidity': round(humidity),
                'green_impact': round((total_area / 500) * 100, 1)
            },
            'green_space_impact': {
                'co2_absorbed': round(total_area * 22),
                'rainwater_capacity': round(total_area * 1000),
                'cooling_effect': round(total_area * 0.1, 1),
                'biodiversity_index': min(100, 60 + (total_area / 10))
            },
            'statistics': {
                'total_spaces': total_spaces,
                'total_area_hectares': round(total_area, 1),
                'ward_count': ward_count,
                'type_count': type_count,
                'average_size': round(total_area / total_spaces, 1) if total_spaces > 0 else 0
            },
            'historical_data': historical_data,
            'alerts': [
                {
                    'type': 'info',
                    'title': 'Air Quality Improving',
                    'message': f'Green spaces contributing to {round((total_area/500)*100)}% improvement in air quality'
                },
                {
                    'type': 'success',
                    'title': 'CO₂ Reduction',
                    'message': f'{round(total_area * 22)}kg CO₂ absorbed annually by green spaces'
                }
            ],
            'last_updated': datetime.now().isoformat()
        }
        
        return jsonify(environmental_data)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/add-green-space', methods=['POST'])
def add_green_space():
    """Add a new green space via Supabase REST API"""
    try:
        data = request.json
        
        # Prepare data for Supabase
        green_space_data = {
            "name": data.get('name'),
            "type": data.get('type'),
            "area_hectares": data.get('area_hectares'),
            "ward": data.get('ward'),
            "latitude": data.get('latitude'),
            "longitude": data.get('longitude'),
            "description": data.get('description'),
            "facilities": data.get('facilities'),
            "accessibility": data.get('accessibility'),
            "environmental_impact": data.get('environmental_impact')
        }
        
        # Insert into Supabase
        url = f"{SUPABASE_URL}/rest/v1/green_spaces"
        headers = get_supabase_headers()
        
        response = requests.post(url, json=green_space_data, headers=headers)
        
        if response.status_code in [200, 201]:
            return jsonify({
                "status": "success",
                "message": "Green space added successfully",
                "data": response.json()
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Failed to add green space: {response.status_code}",
                "details": response.text
            }), 500
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Vercel serverless function handler
def handler(event, context):
    return app(event, context)