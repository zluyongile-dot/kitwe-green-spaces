from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Static green spaces data for Vercel deployment
GREEN_SPACES_DATA = [
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
    },
    {
        "id": 4,
        "name": "Kitwe Golf Club",
        "type": "golf_course",
        "area_hectares": 38.0,
        "ward": "Ndeke",
        "latitude": -12.800000,
        "longitude": 28.240000,
        "description": "18-hole golf course with maintained green spaces",
        "facilities": "Golf course, clubhouse, parking",
        "accessibility": "Members only",
        "environmental_impact": "Moderate - large green area but limited public access"
    },
    {
        "id": 5,
        "name": "Parklands Community Park",
        "type": "park",
        "area_hectares": 2.2,
        "ward": "Parklands",
        "latitude": -12.827778,
        "longitude": 28.208333,
        "description": "Community park serving Parklands residential area",
        "facilities": "Children's playground, sports field, picnic area",
        "accessibility": "Fully accessible",
        "environmental_impact": "High - community recreation and air quality improvement"
    },
    {
        "id": 6,
        "name": "Riverside Gardens",
        "type": "garden",
        "area_hectares": 1.5,
        "ward": "Parklands",
        "latitude": -12.831111,
        "longitude": 28.206667,
        "description": "Botanical gardens along the riverside",
        "facilities": "Walking paths, flower beds, seating areas",
        "accessibility": "Wheelchair accessible",
        "environmental_impact": "High - biodiversity, water management"
    },
    {
        "id": 7,
        "name": "Mukuba Park",
        "type": "park",
        "area_hectares": 2.8,
        "ward": "Parklands",
        "latitude": -12.829167,
        "longitude": 28.204444,
        "description": "Large recreational park with multiple facilities",
        "facilities": "Sports courts, playground, amphitheater",
        "accessibility": "Fully accessible",
        "environmental_impact": "High - recreation, air purification, urban cooling"
    },
    {
        "id": 8,
        "name": "Nkana Sports Complex",
        "type": "sports_field",
        "area_hectares": 5.5,
        "ward": "Nkana",
        "latitude": -12.810833,
        "longitude": 28.218056,
        "description": "Multi-sport complex with grass fields",
        "facilities": "Football fields, athletics track, changing rooms",
        "accessibility": "Public access during events",
        "environmental_impact": "Moderate - large grass areas, limited trees"
    },
    {
        "id": 9,
        "name": "Nkana Dam Recreation Area",
        "type": "park",
        "area_hectares": 9.5,
        "ward": "Nkana",
        "latitude": -12.808333,
        "longitude": 28.221111,
        "description": "Recreational area around Nkana Dam",
        "facilities": "Fishing spots, picnic areas, walking trails",
        "accessibility": "Partially accessible",
        "environmental_impact": "Very high - water ecosystem, wildlife habitat"
    },
    {
        "id": 10,
        "name": "Wusakile Community Garden",
        "type": "garden",
        "area_hectares": 1.2,
        "ward": "Wusakile",
        "latitude": -12.805000,
        "longitude": 28.231944,
        "description": "Community-managed vegetable and flower garden",
        "facilities": "Garden plots, tool shed, water access",
        "accessibility": "Community members",
        "environmental_impact": "High - food security, community engagement"
    }
]

# Add more green spaces to reach 51 total
ADDITIONAL_SPACES = [
    {
        "id": 11,
        "name": "Chimwemwe Children's Park",
        "type": "park",
        "area_hectares": 1.8,
        "ward": "Chimwemwe",
        "latitude": -12.834722,
        "longitude": 28.195833,
        "description": "Dedicated children's recreational park",
        "facilities": "Playground equipment, sandbox, seating",
        "accessibility": "Fully accessible",
        "environmental_impact": "Moderate - child development, limited green coverage"
    },
    {
        "id": 12,
        "name": "Mindolo Dam Park",
        "type": "park",
        "area_hectares": 12.0,
        "ward": "Mindolo",
        "latitude": -12.832778,
        "longitude": 28.234722,
        "description": "Large park surrounding Mindolo Dam",
        "facilities": "Walking trails, fishing areas, picnic spots",
        "accessibility": "Public access with some restrictions",
        "environmental_impact": "Very high - water ecosystem, large green area"
    },
    {
        "id": 13,
        "name": "Buchi Community Forest",
        "type": "forest",
        "area_hectares": 6.5,
        "ward": "Buchi",
        "latitude": -12.845833,
        "longitude": 28.183333,
        "description": "Community-managed forest area",
        "facilities": "Nature trails, picnic areas, forest education",
        "accessibility": "Public access with guides",
        "environmental_impact": "Very high - carbon sequestration, biodiversity"
    },
    {
        "id": 14,
        "name": "Itimpi Nature Reserve",
        "type": "forest",
        "area_hectares": 18.0,
        "ward": "Itimpi",
        "latitude": -12.775000,
        "longitude": 28.266667,
        "description": "Protected nature reserve with indigenous species",
        "facilities": "Nature trails, bird watching areas, research station",
        "accessibility": "Guided tours only",
        "environmental_impact": "Very high - conservation, research, biodiversity"
    },
    {
        "id": 15,
        "name": "Riverside Nature Trail",
        "type": "forest",
        "area_hectares": 8.8,
        "ward": "Riverside",
        "latitude": -12.822222,
        "longitude": 28.229167,
        "description": "Nature trail along the river with forest cover",
        "facilities": "Walking trails, bird watching points, rest areas",
        "accessibility": "Hiking trails, moderate difficulty",
        "environmental_impact": "Very high - riparian ecosystem, wildlife corridor"
    }
]

# Combine all green spaces (truncated for brevity - you can add all 51)
ALL_GREEN_SPACES = GREEN_SPACES_DATA + ADDITIONAL_SPACES

@app.route('/api/green-spaces')
def get_green_spaces():
    """Returns all green spaces as GeoJSON."""
    try:
        features = []
        for space in ALL_GREEN_SPACES:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [space["longitude"], space["latitude"]]
                },
                "properties": {
                    "id": space["id"],
                    "name": space["name"],
                    "type": space["type"],
                    "area_hectares": space["area_hectares"],
                    "ward": space["ward"],
                    "description": space["description"],
                    "facilities": space["facilities"],
                    "accessibility": space["accessibility"],
                    "environmental_impact": space["environmental_impact"]
                }
            }
            features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        
        return jsonify(geojson)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/environmental-data')
def get_environmental_data():
    """Returns simulated environmental monitoring data."""
    try:
        import random
        from datetime import datetime, timedelta
        
        # Calculate total area
        total_area = sum(space["area_hectares"] for space in ALL_GREEN_SPACES)
        
        # Simulate environmental data
        base_aqi = 45
        base_temp = 28 + random.uniform(-2, 3)
        humidity = 65 + random.uniform(-10, 15)
        
        # Generate 7 days of historical data
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
                'biodiversity_index': 85
            },
            'historical_data': historical_data,
            'total_green_spaces': len(ALL_GREEN_SPACES),
            'total_area_hectares': round(total_area, 1),
            'wards_covered': len(set(space["ward"] for space in ALL_GREEN_SPACES)),
            'last_updated': datetime.now().isoformat()
        }
        
        return jsonify(environmental_data)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/test-db')
def test_db():
    """Test endpoint for Vercel deployment."""
    return jsonify({
        "status": "success", 
        "message": "Vercel deployment working!",
        "green_spaces_count": len(ALL_GREEN_SPACES),
        "platform": "Vercel Serverless"
    })

@app.route('/')
def home():
    return jsonify({
        "message": "Kitwe Green Spaces API - Vercel Deployment",
        "endpoints": [
            "/api/green-spaces",
            "/api/environmental-data", 
            "/test-db"
        ]
    })

# Vercel serverless function handler
def handler(request):
    return app(request.environ, lambda status, headers: None)