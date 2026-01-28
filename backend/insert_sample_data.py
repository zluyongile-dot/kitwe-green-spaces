import psycopg2

# Use the same connection settings as in app.py
DB_CONFIG = {
    "dbname": "kitwe_green_spaces",
    "user": "postgres",
    "password": "hapiness",  # 🔴 CHANGE THIS!
    "host": "localhost",
    "port": "5432"
}

# Extended list of green spaces in Kitwe
sample_spaces = [
    # Parks
    ("Kitwe City Park", "park", 85000, "City Centre", 28.2200, -12.8130),
    ("Chimwemwe Park", "park", 45000, "Chimwemwe", 28.2150, -12.8402),
    ("Wusakile Park", "park", 32000, "Wusakile", 28.2001, -12.8055),
    ("Riverside Park", "park", 68000, "Parklands", 28.2305, -12.8251),
    ("Nkana East Park", "park", 28000, "Nkana East", 28.2403, -12.7908),
    
    # Gardens
    ("Botanical Garden", "garden", 15000, "City Centre", 28.2185, -12.8102),
    ("Rose Garden", "garden", 8000, "Parklands", 28.2280, -12.8220),
    ("Community Garden", "garden", 12000, "Chimwemwe", 28.2100, -12.8380),
    ("Medicinal Garden", "garden", 6000, "Nkana", 28.2350, -12.7950),
    
    # Forests/Natural Areas
    ("Chimwemwe Forest Reserve", "forest", 185000, "Chimwemwe", 28.2050, -12.8450),
    ("Kafue River Forest", "forest", 225000, "Riverside", 28.2250, -12.8300),
    ("Mwekera Forest", "forest", 320000, "Mwekera", 28.2500, -12.7800),
    ("Kalulushi Forest Patch", "forest", 95000, "Kalulushi", 28.0900, -12.8500),
    
    # Recreational Areas
    ("Kitwe Golf Club", "golf course", 380000, "Nkana", 28.2380, -12.7880),
    ("Olympic Youth Centre", "recreational", 125000, "City Centre", 28.2220, -12.8080),
    ("Sports Complex Field", "recreational", 65000, "Wusakile", 28.1980, -12.8020),
    ("Community Playground", "recreational", 18000, "Chimwemwe", 28.2120, -12.8360),
    
    # Open Spaces
    ("Central Market Green", "other", 12000, "City Centre", 28.2170, -12.8150),
    ("University Open Space", "other", 35000, "Mulungushi", 28.2450, -12.7750),
    ("Hospital Gardens", "garden", 9000, "Ndeke", 28.1900, -12.8200),
    ("School Playing Field", "recreational", 22000, "Parklands", 28.2320, -12.8180),
    ("Church Grounds", "other", 7000, "Chimwemwe", 28.2080, -12.8420),
    
    # Future Proposed Spaces
    ("Riverside Walkway", "park", 0, "Riverside", 28.2285, -12.8280),
    ("Urban Farm Site", "garden", 0, "Nkana East", 28.2420, -12.7850)
]

def insert_samples():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # Clear existing data (optional)
        cur.execute("DELETE FROM green_spaces;")
        
        # Insert each sample
        for name, gtype, area, ward, lon, lat in sample_spaces:
            cur.execute("""
                INSERT INTO green_spaces (name, type, area_sq_m, ward, geom)
                VALUES (%s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
            """, (name, gtype, area, ward, lon, lat))
        
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ {len(sample_spaces)} green spaces inserted successfully!")
        
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    insert_samples()