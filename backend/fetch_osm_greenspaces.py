"""
Fetch real green spaces from OpenStreetMap for Kitwe, Zambia
Uses Overpass API to get accurate park and green space data
"""

import requests
import json
import psycopg2
from psycopg2.extras import execute_values
import time

# Kitwe bounding box (approximate)
# Format: [south, west, north, east]
KITWE_BBOX = [-12.9, 28.1, -12.7, 28.3]

# Overpass API endpoint
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# Query for green spaces in Kitwe
OVERPASS_QUERY = f"""
[out:json][timeout:60];
(
  // Parks
  way["leisure"="park"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  relation["leisure"="park"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Gardens
  way["leisure"="garden"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  relation["leisure"="garden"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Recreation grounds
  way["leisure"="recreation_ground"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Sports pitches
  way["leisure"="pitch"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Golf courses
  way["leisure"="golf_course"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Forests
  way["landuse"="forest"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Green spaces
  way["landuse"="grass"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  way["landuse"="meadow"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
  
  // Nature reserves
  way["leisure"="nature_reserve"]({KITWE_BBOX[0]},{KITWE_BBOX[1]},{KITWE_BBOX[2]},{KITWE_BBOX[3]});
);
out body;
>;
out skel qt;
"""

def fetch_osm_data():
    """Fetch green space data from OpenStreetMap"""
    print("🌍 Fetching green spaces from OpenStreetMap...")
    print(f"📍 Area: Kitwe, Zambia (bbox: {KITWE_BBOX})")
    
    try:
        response = requests.post(OVERPASS_URL, data={'data': OVERPASS_QUERY}, timeout=60)
        response.raise_for_status()
        data = response.json()
        
        print(f"✅ Received {len(data.get('elements', []))} elements from OSM")
        return data
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching OSM data: {e}")
        return None

def calculate_center(nodes):
    """Calculate center point of a way"""
    if not nodes:
        return None, None
    
    lats = [node['lat'] for node in nodes if 'lat' in node]
    lons = [node['lon'] for node in nodes if 'lon' in node]
    
    if not lats or not lons:
        return None, None
    
    return sum(lats) / len(lats), sum(lons) / len(lons)

def calculate_area(nodes):
    """Calculate approximate area in square meters using Shoelace formula"""
    if len(nodes) < 3:
        return 0
    
    # Convert to radians and calculate area
    import math
    
    def to_radians(deg):
        return deg * math.pi / 180
    
    # Earth radius in meters
    R = 6371000
    
    # Simple approximation for small areas
    lats = [node['lat'] for node in nodes if 'lat' in node]
    lons = [node['lon'] for node in nodes if 'lon' in node]
    
    if len(lats) < 3:
        return 0
    
    # Convert to meters (approximate)
    avg_lat = sum(lats) / len(lats)
    lat_to_m = 111320  # meters per degree latitude
    lon_to_m = 111320 * math.cos(to_radians(avg_lat))  # meters per degree longitude
    
    # Calculate area using Shoelace formula
    area = 0
    for i in range(len(lats)):
        j = (i + 1) % len(lats)
        area += (lons[i] * lon_to_m) * (lats[j] * lat_to_m)
        area -= (lons[j] * lon_to_m) * (lats[i] * lat_to_m)
    
    return abs(area) / 2

def process_osm_data(osm_data):
    """Process OSM data into green spaces"""
    if not osm_data or 'elements' not in osm_data:
        return []
    
    elements = osm_data['elements']
    
    # Create a lookup for nodes
    nodes_lookup = {}
    for element in elements:
        if element['type'] == 'node':
            nodes_lookup[element['id']] = element
    
    green_spaces = []
    
    for element in elements:
        if element['type'] not in ['way', 'relation']:
            continue
        
        tags = element.get('tags', {})
        
        # Skip if no name
        name = tags.get('name', tags.get('name:en', ''))
        if not name:
            # Generate a name based on type
            leisure = tags.get('leisure', '')
            landuse = tags.get('landuse', '')
            if leisure:
                name = f"{leisure.replace('_', ' ').title()} Area"
            elif landuse:
                name = f"{landuse.replace('_', ' ').title()} Area"
            else:
                continue
        
        # Determine type
        green_type = 'other'
        if tags.get('leisure') == 'park':
            green_type = 'park'
        elif tags.get('leisure') == 'garden':
            green_type = 'garden'
        elif tags.get('landuse') == 'forest':
            green_type = 'forest'
        elif tags.get('leisure') in ['recreation_ground', 'pitch']:
            green_type = 'recreational'
        elif tags.get('leisure') == 'golf_course':
            green_type = 'golf course'
        
        # Get nodes for this way
        if element['type'] == 'way':
            way_nodes = []
            for node_id in element.get('nodes', []):
                if node_id in nodes_lookup:
                    way_nodes.append(nodes_lookup[node_id])
            
            if not way_nodes:
                continue
            
            # Calculate center and area
            lat, lon = calculate_center(way_nodes)
            if lat is None or lon is None:
                continue
            
            area_sq_m = calculate_area(way_nodes)
            
            # Skip very small areas (< 100 sq m)
            if area_sq_m < 100:
                continue
            
            green_space = {
                'name': name,
                'type': green_type,
                'latitude': lat,
                'longitude': lon,
                'area_sq_m': area_sq_m,
                'area_hectares': area_sq_m / 10000,
                'description': tags.get('description', f"Green space in Kitwe"),
                'ward': tags.get('addr:suburb', tags.get('addr:district', 'Kitwe')),
                'osm_id': element['id'],
                'osm_type': element['type']
            }
            
            green_spaces.append(green_space)
    
    return green_spaces

def save_to_database(green_spaces):
    """Save green spaces to PostgreSQL database"""
    if not green_spaces:
        print("⚠️ No green spaces to save")
        return
    
    print(f"\n💾 Saving {len(green_spaces)} green spaces to database...")
    
    try:
        # Connect to database
        conn = psycopg2.connect(
            dbname="kitwe_green_spaces",
            user="postgres",
            password="hapiness",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        
        # Clear existing data (optional - comment out if you want to keep old data)
        print("🗑️ Clearing old data...")
        cur.execute("DELETE FROM green_spaces")
        
        # Prepare data for insertion
        values = [
            (
                gs['name'],
                gs['type'],
                gs['latitude'],
                gs['longitude'],
                gs['area_sq_m'],
                gs['area_hectares'],
                gs['description'],
                gs['ward'],
                f"POINT({gs['longitude']} {gs['latitude']})"
            )
            for gs in green_spaces
        ]
        
        # Insert data
        insert_query = """
            INSERT INTO green_spaces 
            (name, type, latitude, longitude, area_sq_m, area_hectares, description, ward, geom)
            VALUES %s
        """
        
        execute_values(cur, insert_query, values)
        
        conn.commit()
        print(f"✅ Successfully saved {len(green_spaces)} green spaces!")
        
        # Show summary
        cur.execute("SELECT type, COUNT(*) FROM green_spaces GROUP BY type ORDER BY COUNT(*) DESC")
        print("\n📊 Summary by type:")
        for row in cur.fetchall():
            print(f"   {row[0]}: {row[1]}")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        if conn:
            conn.rollback()

def save_to_json(green_spaces, filename='osm_greenspaces.json'):
    """Save green spaces to JSON file for backup"""
    print(f"\n💾 Saving to {filename}...")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(green_spaces, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved to {filename}")

def main():
    print("=" * 60)
    print("🌳 Kitwe Green Spaces - OpenStreetMap Data Fetcher")
    print("=" * 60)
    
    # Fetch data from OSM
    osm_data = fetch_osm_data()
    
    if not osm_data:
        print("❌ Failed to fetch data from OpenStreetMap")
        return
    
    # Process the data
    print("\n🔄 Processing OSM data...")
    green_spaces = process_osm_data(osm_data)
    
    if not green_spaces:
        print("⚠️ No green spaces found in the data")
        print("💡 This might mean:")
        print("   - Kitwe doesn't have mapped green spaces in OSM yet")
        print("   - The bounding box needs adjustment")
        print("   - You may need to add data to OpenStreetMap first")
        return
    
    print(f"\n✅ Found {len(green_spaces)} green spaces!")
    
    # Show sample
    print("\n📋 Sample green spaces:")
    for i, gs in enumerate(green_spaces[:5], 1):
        print(f"   {i}. {gs['name']} ({gs['type']}) - {gs['area_hectares']:.2f} ha")
    
    if len(green_spaces) > 5:
        print(f"   ... and {len(green_spaces) - 5} more")
    
    # Save to JSON backup
    save_to_json(green_spaces)
    
    # Ask user before saving to database
    print("\n" + "=" * 60)
    response = input("💾 Save to database? This will REPLACE existing data (y/n): ")
    
    if response.lower() == 'y':
        save_to_database(green_spaces)
        print("\n✅ Done! Refresh your map to see the real green spaces!")
    else:
        print("\n⏭️ Skipped database update. Data saved to JSON file only.")
    
    print("\n" + "=" * 60)
    print("🎉 Process complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
