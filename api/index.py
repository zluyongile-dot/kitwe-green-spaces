from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import random
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Kitwe Green Spaces API - Vercel Deployment",
        "status": "running",
        "endpoints": [
            "/api/green-spaces",
            "/api/environmental-data",
            "/test-db"
        ]
    })

@app.route('/test-db')
def test_db():
    """Test API connection"""
    return jsonify({
        "status": "success",
        "message": "API is working! Using enhanced fallback data.",
        "platform": "Vercel + Enhanced Fallback Data",
        "note": "Ready for production use"
    })

@app.route('/api/green-spaces')
def get_green_spaces():
    """Get all green spaces as GeoJSON"""
    # Enhanced fallback data
    fallback_spaces = [
        {
            "id": 1,
            "name": "Kitwe City Square",
            "type": "park",
            "area_hectares": 1.8,
            "area_sq_m": 18000,
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
            "area_sq_m": 35000,
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
            "area_sq_m": 42000,
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
            "name": "Mindolo Dam Recreation Area",
            "type": "recreational",
            "area_hectares": 12.5,
            "area_sq_m": 125000,
            "ward": "Mindolo",
            "latitude": -12.835000,
            "longitude": 28.240000,
            "description": "Large recreational area around Mindolo Dam",
            "facilities": "Fishing spots, picnic areas, boat launch",
            "accessibility": "Limited accessibility",
            "environmental_impact": "Water conservation, wildlife habitat"
        },
        {
            "id": 5,
            "name": "Nkana Golf Course",
            "type": "golf course",
            "area_hectares": 45.0,
            "area_sq_m": 450000,
            "ward": "Nkana East",
            "latitude": -12.820000,
            "longitude": 28.200000,
            "description": "18-hole championship golf course",
            "facilities": "Golf course, clubhouse, pro shop, restaurant",
            "accessibility": "Members and guests only",
            "environmental_impact": "Large green space, water management"
        },
        {
            "id": 6,
            "name": "Chimwemwe Township Park",
            "type": "park",
            "area_hectares": 2.1,
            "area_sq_m": 21000,
            "ward": "Chimwemwe",
            "latitude": -12.840000,
            "longitude": 28.220000,
            "description": "Community park serving Chimwemwe township",
            "facilities": "Playground, community center, sports field",
            "accessibility": "Fully accessible",
            "environmental_impact": "Community green space, air quality improvement"
        },
        {
            "id": 7,
            "name": "Wusakile Community Garden",
            "type": "garden",
            "area_hectares": 0.8,
            "area_sq_m": 8000,
            "ward": "Wusakile",
            "latitude": -12.830000,
            "longitude": 28.190000,
            "description": "Community vegetable garden and green space",
            "facilities": "Garden plots, tool shed, water access",
            "accessibility": "Community members",
            "environmental_impact": "Food security, soil conservation"
        },
        {
            "id": 8,
            "name": "Buchi Township Green Belt",
            "type": "forest",
            "area_hectares": 8.3,
            "area_sq_m": 83000,
            "ward": "Buchi",
            "latitude": -12.845000,
            "longitude": 28.235000,
            "description": "Protected green belt area in Buchi township",
            "facilities": "Walking trails, bird watching areas",
            "accessibility": "Public access during daylight",
            "environmental_impact": "Biodiversity conservation, erosion control"
        },
        {
            "id": 9,
            "name": "Ndeke Township Park",
            "type": "park",
            "area_hectares": 1.5,
            "area_sq_m": 15000,
            "ward": "Ndeke",
            "latitude": -12.850000,
            "longitude": 28.215000,
            "description": "Small community park in Ndeke township",
            "facilities": "Playground, benches, small sports area",
            "accessibility": "Fully accessible",
            "environmental_impact": "Local air quality improvement"
        },
        {
            "id": 10,
            "name": "Garneton Sports Complex",
            "type": "recreational",
            "area_hectares": 6.8,
            "area_sq_m": 68000,
            "ward": "Garneton",
            "latitude": -12.825000,
            "longitude": 28.205000,
            "description": "Multi-sport recreational facility",
            "facilities": "Football pitch, basketball court, athletics track",
            "accessibility": "Public access with fees",
            "environmental_impact": "Community recreation, green space preservation"
        },
        {
            "id": 11,
            "name": "Kwacha Township Garden",
            "type": "garden",
            "area_hectares": 1.2,
            "area_sq_m": 12000,
            "ward": "Kwacha",
            "latitude": -12.855000,
            "longitude": 28.225000,
            "description": "Community botanical garden",
            "facilities": "Flower beds, medicinal plants, seating areas",
            "accessibility": "Public access",
            "environmental_impact": "Biodiversity, educational value"
        },
        {
            "id": 12,
            "name": "Parklands Residential Green",
            "type": "park",
            "area_hectares": 2.8,
            "area_sq_m": 28000,
            "ward": "Parklands",
            "latitude": -12.810000,
            "longitude": 28.195000,
            "description": "Residential area green space",
            "facilities": "Walking paths, children's play area, dog park",
            "accessibility": "Residents and visitors",
            "environmental_impact": "Residential air quality, property values"
        }
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
        "features": features
    })

@app.route('/api/environmental-data')
def get_environmental_data():
    """Get environmental monitoring data"""
    # Calculate from our fallback data
    total_area = 90.6  # Sum of all areas above
    ward_count = 10
    type_count = 5
    total_spaces = 12
    
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
            'average_size': round(total_area / total_spaces, 1)
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

@app.route('/api/add-green-space', methods=['POST'])
def add_green_space():
    """Add a new green space (demo endpoint)"""
    return jsonify({
        "status": "success",
        "message": "Demo mode - green space would be added to database",
        "note": "Connect to Supabase for full functionality"
    })

# For Vercel
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)