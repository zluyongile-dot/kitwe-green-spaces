// Static green spaces data for Kitwe & Ndola Green Spaces GIS Map - 26 Kitwe + 12 Ndola Locations with NDVI and City properties
const STATIC_GREEN_SPACES_DATA = {
    "type": "FeatureCollection",
    "features": [
        // ================= KITWE STUDY AREA (26 spaces) =================
        // PARKS & RECREATION (8 spaces)
        {
            "type": "Feature",
            "properties": { 
                "id": 1, 
                "name": "Freedom Park", 
                "type": "municipal_park", 
                "ward": "City Centre", 
                "city": "Kitwe",
                "ndvi_value": 0.62,
                "area_sq_m": 45000,
                "image_url": "https://images.unsplash.com/photo-1625244724107-a73d34d69344?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.21551, -12.80693] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 2, 
                "name": "Kitwe Playing Fields", 
                "type": "sports_recreation", 
                "ward": "City Centre", 
                "city": "Kitwe",
                "ndvi_value": 0.35,
                "area_sq_m": 65000,
                "image_url": "https://images.unsplash.com/photo-1589487391730-58f20eb2c308?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.21822, -12.79229] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 3, 
                "name": "Zambezi Way Park", 
                "type": "neighborhood_park", 
                "ward": "Riverside", 
                "city": "Kitwe",
                "ndvi_value": 0.55,
                "area_sq_m": 28000,
                "image_url": "https://images.unsplash.com/photo-1519331379826-f10be5486c6f?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.23229, -12.79260] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 4, 
                "name": "Fyapakale Park", 
                "type": "neighborhood_park", 
                "ward": "Riverside", 
                "city": "Kitwe",
                "ndvi_value": 0.58,
                "area_sq_m": 32000,
                "image_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.23458, -12.79800] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 5, 
                "name": "Burrum Park", 
                "type": "neighborhood_park", 
                "ward": "Parklands", 
                "city": "Kitwe",
                "ndvi_value": 0.51,
                "area_sq_m": 22000,
                "image_url": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.243056, -12.802083] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 6, 
                "name": "Kew Gardens Park", 
                "type": "neighborhood_park", 
                "ward": "Parklands", 
                "city": "Kitwe",
                "ndvi_value": 0.56,
                "area_sq_m": 19000,
                "image_url": "https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.232778, -12.803889] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 7, 
                "name": "Garden Park Stadium", 
                "type": "sports_recreation", 
                "ward": "City Centre", 
                "city": "Kitwe",
                "ndvi_value": 0.32,
                "area_sq_m": 28000,
                "image_url": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.219722, -12.791389] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 8, 
                "name": "Cheswa Park", 
                "type": "neighborhood_park", 
                "ward": "Parklands", 
                "city": "Kitwe",
                "ndvi_value": 0.53,
                "area_sq_m": 15000,
                "image_url": "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.2250, -12.8080] }
        },

        // WATER BODIES (9 spaces)
        {
            "type": "Feature",
            "properties": { 
                "id": 9, 
                "name": "Kitwe Stream", 
                "type": "tributary_stream", 
                "ward": "Riverside", 
                "city": "Kitwe",
                "ndvi_value": 0.22,
                "area_sq_m": 15000,
                "image_url": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.25811, -12.80936] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 10, 
                "name": "Kafue River", 
                "type": "major_river", 
                "ward": "Riverside", 
                "city": "Kitwe",
                "ndvi_value": 0.10,
                "area_sq_m": 185000,
                "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.250756572152678, -12.825001678275749] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 11, 
                "name": "Mindolo Dam", 
                "type": "dam_lake", 
                "ward": "Mindolo", 
                "city": "Kitwe",
                "ndvi_value": 0.08,
                "area_sq_m": 425000,
                "image_url": "https://images.unsplash.com/photo-1439066615861-d1af74d74000?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.14111998142754, -12.790960190352685] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 12, 
                "name": "Mwekwera Falls", 
                "type": "waterfall_lake", 
                "ward": "Mwekwera", 
                "city": "Kitwe",
                "ndvi_value": 0.18,
                "area_sq_m": 95000,
                "image_url": "https://images.unsplash.com/photo-1482862549707-f63cb32c5fd9?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.358938982476428, -12.828180654957118] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 13, 
                "name": "Chembe Bird Sanctuary Lake", 
                "type": "lake_wetland", 
                "ward": "Chembe", 
                "city": "Kitwe",
                "ndvi_value": 0.25,
                "area_sq_m": 285000,
                "image_url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [27.993929731853243, -12.832010423511084] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 14, 
                "name": "Kumasamba Lodge Water", 
                "type": "lake_fishing", 
                "ward": "Kumasamba", 
                "city": "Kitwe",
                "ndvi_value": 0.15,
                "area_sq_m": 125000,
                "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.23994476728268, -12.905264693431171] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 15, 
                "name": "Ngoma Lake", 
                "type": "lake", 
                "ward": "Ngoma", 
                "city": "Kitwe",
                "ndvi_value": 0.05,
                "area_sq_m": 165000,
                "image_url": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.24254722, -12.79860833] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 16, 
                "name": "Country Side Dam", 
                "type": "dam_lake", 
                "ward": "Mindolo", 
                "city": "Kitwe",
                "ndvi_value": 0.09,
                "area_sq_m": 95000,
                "image_url": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.1600, -12.7950] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 17, 
                "name": "Chandamali Lake", 
                "type": "lake", 
                "ward": "Garneton", 
                "city": "Kitwe",
                "ndvi_value": 0.07,
                "area_sq_m": 110000,
                "image_url": "https://images.unsplash.com/photo-1494783367193-149034c05e8f?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.2550, -12.7850] }
        },

        // GARDENS (4 spaces)
        {
            "type": "Feature",
            "properties": { 
                "id": 18, 
                "name": "Serene Gardens", 
                "type": "commercial_garden", 
                "ward": "City Centre", 
                "city": "Kitwe",
                "ndvi_value": 0.60,
                "area_sq_m": 12000,
                "image_url": "https://images.unsplash.com/photo-1558905617-1538b4512e80?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.223056, -12.810278] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 19, 
                "name": "Mist Gardens", 
                "type": "commercial_garden", 
                "ward": "Riverside", 
                "city": "Kitwe",
                "ndvi_value": 0.64,
                "area_sq_m": 15000,
                "image_url": "https://images.unsplash.com/photo-1533038590840-1cde6b66b706?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.236111, -12.813889] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 20, 
                "name": "Sunset Gardens Kitwe", 
                "type": "commercial_event_garden", 
                "ward": "City Centre", 
                "city": "Kitwe",
                "ndvi_value": 0.61,
                "area_sq_m": 18500,
                "image_url": "https://images.unsplash.com/photo-1472214222541-d510753a49fa?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.217778, -12.813056] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 21, 
                "name": "Casablanca Gardens", 
                "type": "commercial_garden", 
                "ward": "Nkana", 
                "city": "Kitwe",
                "ndvi_value": 0.59,
                "area_sq_m": 14000,
                "image_url": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.205556, -12.831944] }
        },

        // GOLF COURSES (1 space)
        {
            "type": "Feature",
            "properties": { 
                "id": 22, 
                "name": "Nkana Golf Club", 
                "type": "golf_course_18hole", 
                "ward": "Nkana West", 
                "city": "Kitwe",
                "ndvi_value": 0.42,
                "area_sq_m": 485000,
                "image_url": "https://images.unsplash.com/photo-1587174486073-ae5e5cff23aa?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.17966, -12.82881] }
        },

        // CRICKET GROUNDS (1 space)
        {
            "type": "Feature",
            "properties": { 
                "id": 23, 
                "name": "Nkana Cricket Club", 
                "type": "cricket_ground", 
                "ward": "Nkana", 
                "city": "Kitwe",
                "ndvi_value": 0.38,
                "area_sq_m": 35000,
                "image_url": "https://images.unsplash.com/photo-1530541930197-ff16ac917b0e?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.20839907714752, -12.830287133445191] }
        },

        // FORESTS & WOODLANDS (2 spaces)
        {
            "type": "Feature",
            "properties": { 
                "id": 24, 
                "name": "Savanna Woodlands", 
                "type": "miombo_woodland", 
                "ward": "Surrounding Area", 
                "city": "Kitwe",
                "ndvi_value": 0.82,
                "area_sq_m": 1250000,
                "image_url": "https://images.unsplash.com/photo-1475113548554-5a36f1f523d6?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.25, -12.85] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 25, 
                "name": "Dambos Seasonal Wetlands", 
                "type": "grassland_wetland", 
                "ward": "Surrounding Area", 
                "city": "Kitwe",
                "ndvi_value": 0.48,
                "area_sq_m": 385000,
                "image_url": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.28, -12.82] }
        },

        // WILDLIFE RESERVES (1 space)
        {
            "type": "Feature",
            "properties": { 
                "id": 26, 
                "name": "CBU Nature Park", 
                "type": "university_nature_park", 
                "ward": "Riverside", 
                "city": "Kitwe",
                "ndvi_value": 0.74,
                "area_sq_m": 125000,
                "image_url": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.239010623101414, -12.80234209672651] }
        },

        // ================= NDOLA BENCHMARK REFERENCE AREA (12 spaces) =================
        {
            "type": "Feature",
            "properties": { 
                "id": 101, 
                "name": "Ndola Golf Club", 
                "type": "golf_course_18hole", 
                "ward": "Ndola Central", 
                "city": "Ndola",
                "ndvi_value": 0.38,
                "area_sq_m": 350000,
                "image_url": "https://images.unsplash.com/photo-1587174486073-ae5e5cff23aa?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6400, -12.9750] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 102, 
                "name": "Kanini Community Park", 
                "type": "neighborhood_park", 
                "ward": "Kanini", 
                "city": "Ndola",
                "ndvi_value": 0.52,
                "area_sq_m": 22000,
                "image_url": "https://images.unsplash.com/photo-1519331379826-f10be5486c6f?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6480, -12.9800] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 103, 
                "name": "Itawa Springs Reserve", 
                "type": "forest", 
                "ward": "Itawa", 
                "city": "Ndola",
                "ndvi_value": 0.75,
                "area_sq_m": 120000,
                "image_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6650, -13.0100] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 104, 
                "name": "Hillcrest Public Gardens", 
                "type": "commercial_garden", 
                "ward": "Hillcrest", 
                "city": "Ndola",
                "ndvi_value": 0.58,
                "area_sq_m": 14000,
                "image_url": "https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6380, -12.9650] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 105, 
                "name": "Kavu Forest Reserve", 
                "type": "forest", 
                "ward": "Kavu", 
                "city": "Ndola",
                "ndvi_value": 0.81,
                "area_sq_m": 450000,
                "image_url": "https://images.unsplash.com/photo-1475113548554-5a36f1f523d6?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6900, -12.9500] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 106, 
                "name": "Dag Hammarskjöld Memorial Site", 
                "type": "municipal_park", 
                "ward": "Hammarskjöld", 
                "city": "Ndola",
                "ndvi_value": 0.72,
                "area_sq_m": 90000,
                "image_url": "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.5200, -12.9780] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 107, 
                "name": "Ndola Boating Club Lake", 
                "type": "dam_lake", 
                "ward": "Itawa", 
                "city": "Ndola",
                "ndvi_value": 0.12,
                "area_sq_m": 150000,
                "image_url": "https://images.unsplash.com/photo-1439066615861-d1af74d74000?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6550, -13.0200] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 108, 
                "name": "Chifubu Sports Ground", 
                "type": "sports_recreation", 
                "ward": "Chifubu", 
                "city": "Ndola",
                "ndvi_value": 0.32,
                "area_sq_m": 45000,
                "image_url": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6600, -12.9450] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 109, 
                "name": "Kansenji Linear Park", 
                "type": "neighborhood_park", 
                "ward": "Kansenji", 
                "city": "Ndola",
                "ndvi_value": 0.55,
                "area_sq_m": 18000,
                "image_url": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6250, -12.9700] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 110, 
                "name": "Jubilee Park Ndola", 
                "type": "municipal_park", 
                "ward": "City Centre", 
                "city": "Ndola",
                "ndvi_value": 0.61,
                "area_sq_m": 25000,
                "image_url": "https://images.unsplash.com/photo-1625244724107-a73d34d69344?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6420, -12.9820] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 111, 
                "name": "Masala Community Garden", 
                "type": "commercial_garden", 
                "ward": "Masala", 
                "city": "Ndola",
                "ndvi_value": 0.48,
                "area_sq_m": 8500,
                "image_url": "https://images.unsplash.com/photo-1558905617-1538b4512e80?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6300, -13.0150] }
        },
        {
            "type": "Feature",
            "properties": { 
                "id": 112, 
                "name": "Mapepe Woodland", 
                "type": "forest", 
                "ward": "Kavu", 
                "city": "Ndola",
                "ndvi_value": 0.78,
                "area_sq_m": 280000,
                "image_url": "https://images.unsplash.com/photo-1482862549707-f63cb32c5fd9?q=80&w=600&auto=format&fit=crop"
            },
            "geometry": { "type": "Point", "coordinates": [28.6950, -12.9900] }
        }
    ]
};

// Function to simulate API call for static deployment
window.getStaticGreenSpaces = function() {
    return Promise.resolve(STATIC_GREEN_SPACES_DATA);
};