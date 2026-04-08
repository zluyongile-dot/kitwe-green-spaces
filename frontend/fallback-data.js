// Fallback data for when backend is not available - All 51 Green Spaces
window.FALLBACK_GREEN_SPACES = {
    "type": "FeatureCollection",
    "features": [
        // Parks (15 spaces)
        {"type": "Feature", "properties": {"id": 1, "name": "Kitwe Central Park", "type": "park", "ward": "Kitwe Central", "area_sq_m": 25000}, "geometry": {"type": "Point", "coordinates": [28.2200, -12.8130]}},
        {"type": "Feature", "properties": {"id": 2, "name": "Parklands Community Park", "type": "park", "ward": "Parklands", "area_sq_m": 28000}, "geometry": {"type": "Point", "coordinates": [28.2080, -12.8120]}},
        {"type": "Feature", "properties": {"id": 3, "name": "Mukuba Park", "type": "park", "ward": "Mukuba", "area_sq_m": 22000}, "geometry": {"type": "Point", "coordinates": [28.2320, -12.8160]}},
        {"type": "Feature", "properties": {"id": 4, "name": "Ndeke Park", "type": "park", "ward": "Ndeke", "area_sq_m": 18000}, "geometry": {"type": "Point", "coordinates": [28.2050, -12.8200]}},
        {"type": "Feature", "properties": {"id": 5, "name": "Bulangililo Park", "type": "park", "ward": "Bulangililo", "area_sq_m": 20000}, "geometry": {"type": "Point", "coordinates": [28.2400, -12.8100]}},
        {"type": "Feature", "properties": {"id": 6, "name": "Chamboli Park", "type": "park", "ward": "Chamboli", "area_sq_m": 15000}, "geometry": {"type": "Point", "coordinates": [28.1950, -12.8250]}},
        {"type": "Feature", "properties": {"id": 7, "name": "Wusakile Park", "type": "park", "ward": "Wusakile", "area_sq_m": 17000}, "geometry": {"type": "Point", "coordinates": [28.2450, -12.8050]}},
        {"type": "Feature", "properties": {"id": 8, "name": "Kwacha Park", "type": "park", "ward": "Kwacha", "area_sq_m": 19000}, "geometry": {"type": "Point", "coordinates": [28.2150, -12.8300]}},
        {"type": "Feature", "properties": {"id": 9, "name": "Ipusukilo Park", "type": "park", "ward": "Ipusukilo", "area_sq_m": 16000}, "geometry": {"type": "Point", "coordinates": [28.2350, -12.8280]}},
        {"type": "Feature", "properties": {"id": 10, "name": "Nkana East Park", "type": "park", "ward": "Nkana East", "area_sq_m": 21000}, "geometry": {"type": "Point", "coordinates": [28.2100, -12.8050]}},
        {"type": "Feature", "properties": {"id": 11, "name": "Nkana West Park", "type": "park", "ward": "Nkana West", "area_sq_m": 23000}, "geometry": {"type": "Point", "coordinates": [28.2000, -12.8000]}},
        {"type": "Feature", "properties": {"id": 12, "name": "Chimwemwe Park", "type": "park", "ward": "Chimwemwe", "area_sq_m": 14000}, "geometry": {"type": "Point", "coordinates": [28.2300, -12.8200]}},
        {"type": "Feature", "properties": {"id": 13, "name": "Mindolo Park", "type": "park", "ward": "Mindolo", "area_sq_m": 26000}, "geometry": {"type": "Point", "coordinates": [28.2250, -12.8180]}},
        {"type": "Feature", "properties": {"id": 14, "name": "Buchi Park", "type": "park", "ward": "Buchi", "area_sq_m": 24000}, "geometry": {"type": "Point", "coordinates": [28.2350, -12.8250]}},
        {"type": "Feature", "properties": {"id": 15, "name": "Riverside Park", "type": "park", "ward": "Riverside", "area_sq_m": 30000}, "geometry": {"type": "Point", "coordinates": [28.2180, -12.8080]}},

        // Gardens (12 spaces)
        {"type": "Feature", "properties": {"id": 16, "name": "Riverside Gardens", "type": "garden", "ward": "Riverside", "area_sq_m": 15000}, "geometry": {"type": "Point", "coordinates": [28.2150, -12.8100]}},
        {"type": "Feature", "properties": {"id": 17, "name": "Mindolo Gardens", "type": "garden", "ward": "Mindolo", "area_sq_m": 18000}, "geometry": {"type": "Point", "coordinates": [28.2260, -12.8190]}},
        {"type": "Feature", "properties": {"id": 18, "name": "Botanical Gardens", "type": "garden", "ward": "Kitwe Central", "area_sq_m": 12000}, "geometry": {"type": "Point", "coordinates": [28.2220, -12.8140]}},
        {"type": "Feature", "properties": {"id": 19, "name": "Nkana Rose Garden", "type": "garden", "ward": "Nkana East", "area_sq_m": 8000}, "geometry": {"type": "Point", "coordinates": [28.2110, -12.8060]}},
        {"type": "Feature", "properties": {"id": 20, "name": "Parklands Flower Garden", "type": "garden", "ward": "Parklands", "area_sq_m": 10000}, "geometry": {"type": "Point", "coordinates": [28.2090, -12.8130]}},
        {"type": "Feature", "properties": {"id": 21, "name": "Chimwemwe Community Garden", "type": "garden", "ward": "Chimwemwe", "area_sq_m": 6000}, "geometry": {"type": "Point", "coordinates": [28.2310, -12.8210]}},
        {"type": "Feature", "properties": {"id": 22, "name": "Wusakile Herb Garden", "type": "garden", "ward": "Wusakile", "area_sq_m": 7000}, "geometry": {"type": "Point", "coordinates": [28.2460, -12.8060]}},
        {"type": "Feature", "properties": {"id": 23, "name": "Mukuba Medicinal Garden", "type": "garden", "ward": "Mukuba", "area_sq_m": 9000}, "geometry": {"type": "Point", "coordinates": [28.2330, -12.8170]}},
        {"type": "Feature", "properties": {"id": 24, "name": "Bulangililo Vegetable Garden", "type": "garden", "ward": "Bulangililo", "area_sq_m": 11000}, "geometry": {"type": "Point", "coordinates": [28.2410, -12.8110]}},
        {"type": "Feature", "properties": {"id": 25, "name": "Chamboli Flower Garden", "type": "garden", "ward": "Chamboli", "area_sq_m": 5000}, "geometry": {"type": "Point", "coordinates": [28.1960, -12.8260]}},
        {"type": "Feature", "properties": {"id": 26, "name": "Kwacha Community Garden", "type": "garden", "ward": "Kwacha", "area_sq_m": 8500}, "geometry": {"type": "Point", "coordinates": [28.2160, -12.8310]}},
        {"type": "Feature", "properties": {"id": 27, "name": "Ipusukilo Garden", "type": "garden", "ward": "Ipusukilo", "area_sq_m": 7500}, "geometry": {"type": "Point", "coordinates": [28.2360, -12.8290]}},

        // Forests (10 spaces)
        {"type": "Feature", "properties": {"id": 28, "name": "Chimwemwe Forest", "type": "forest", "ward": "Chimwemwe", "area_sq_m": 45000}, "geometry": {"type": "Point", "coordinates": [28.2300, -12.8200]}},
        {"type": "Feature", "properties": {"id": 29, "name": "Buchi Community Forest", "type": "forest", "ward": "Buchi", "area_sq_m": 52000}, "geometry": {"type": "Point", "coordinates": [28.2350, -12.8250]}},
        {"type": "Feature", "properties": {"id": 30, "name": "Copperbelt University Arboretum", "type": "forest", "ward": "Riverside", "area_sq_m": 38000}, "geometry": {"type": "Point", "coordinates": [28.2180, -12.8080]}},
        {"type": "Feature", "properties": {"id": 31, "name": "Mindolo Forest Reserve", "type": "forest", "ward": "Mindolo", "area_sq_m": 42000}, "geometry": {"type": "Point", "coordinates": [28.2270, -12.8200]}},
        {"type": "Feature", "properties": {"id": 32, "name": "Wusakile Woodland", "type": "forest", "ward": "Wusakile", "area_sq_m": 35000}, "geometry": {"type": "Point", "coordinates": [28.2470, -12.8070]}},
        {"type": "Feature", "properties": {"id": 33, "name": "Mukuba Forest", "type": "forest", "ward": "Mukuba", "area_sq_m": 40000}, "geometry": {"type": "Point", "coordinates": [28.2340, -12.8180]}},
        {"type": "Feature", "properties": {"id": 34, "name": "Bulangililo Forest", "type": "forest", "ward": "Bulangililo", "area_sq_m": 48000}, "geometry": {"type": "Point", "coordinates": [28.2420, -12.8120]}},
        {"type": "Feature", "properties": {"id": 35, "name": "Ndeke Woodland", "type": "forest", "ward": "Ndeke", "area_sq_m": 33000}, "geometry": {"type": "Point", "coordinates": [28.2060, -12.8210]}},
        {"type": "Feature", "properties": {"id": 36, "name": "Chamboli Forest", "type": "forest", "ward": "Chamboli", "area_sq_m": 36000}, "geometry": {"type": "Point", "coordinates": [28.1970, -12.8270]}},
        {"type": "Feature", "properties": {"id": 37, "name": "Kwacha Forest Reserve", "type": "forest", "ward": "Kwacha", "area_sq_m": 44000}, "geometry": {"type": "Point", "coordinates": [28.2170, -12.8320]}},

        // Recreational (8 spaces)
        {"type": "Feature", "properties": {"id": 38, "name": "Nkana Sports Complex", "type": "recreational", "ward": "Nkana East", "area_sq_m": 35000}, "geometry": {"type": "Point", "coordinates": [28.2100, -12.8050]}},
        {"type": "Feature", "properties": {"id": 39, "name": "Chimwemwe Football Ground", "type": "recreational", "ward": "Chimwemwe", "area_sq_m": 12000}, "geometry": {"type": "Point", "coordinates": [28.2320, -12.8220]}},
        {"type": "Feature", "properties": {"id": 40, "name": "Mindolo Recreation Center", "type": "recreational", "ward": "Mindolo", "area_sq_m": 18000}, "geometry": {"type": "Point", "coordinates": [28.2280, -12.8210]}},
        {"type": "Feature", "properties": {"id": 41, "name": "Riverside Sports Ground", "type": "recreational", "ward": "Riverside", "area_sq_m": 22000}, "geometry": {"type": "Point", "coordinates": [28.2190, -12.8090]}},
        {"type": "Feature", "properties": {"id": 42, "name": "Wusakile Sports Complex", "type": "recreational", "ward": "Wusakile", "area_sq_m": 28000}, "geometry": {"type": "Point", "coordinates": [28.2480, -12.8080]}},
        {"type": "Feature", "properties": {"id": 43, "name": "Parklands Recreation Area", "type": "recreational", "ward": "Parklands", "area_sq_m": 16000}, "geometry": {"type": "Point", "coordinates": [28.2100, -12.8140]}},
        {"type": "Feature", "properties": {"id": 44, "name": "Mukuba Sports Ground", "type": "recreational", "ward": "Mukuba", "area_sq_m": 20000}, "geometry": {"type": "Point", "coordinates": [28.2350, -12.8190]}},
        {"type": "Feature", "properties": {"id": 45, "name": "Bulangililo Recreation Center", "type": "recreational", "ward": "Bulangililo", "area_sq_m": 24000}, "geometry": {"type": "Point", "coordinates": [28.2430, -12.8130]}},

        // Golf Courses (3 spaces)
        {"type": "Feature", "properties": {"id": 46, "name": "Nkana Golf Club", "type": "golf course", "ward": "Nkana West", "area_sq_m": 85000}, "geometry": {"type": "Point", "coordinates": [28.2000, -12.8000]}},
        {"type": "Feature", "properties": {"id": 47, "name": "Kitwe Golf Club", "type": "golf course", "ward": "Riverside", "area_sq_m": 92000}, "geometry": {"type": "Point", "coordinates": [28.2200, -12.8100]}},
        {"type": "Feature", "properties": {"id": 48, "name": "Mindolo Golf Course", "type": "golf course", "ward": "Mindolo", "area_sq_m": 78000}, "geometry": {"type": "Point", "coordinates": [28.2290, -12.8220]}},

        // Other (3 spaces)
        {"type": "Feature", "properties": {"id": 49, "name": "Kitwe Cemetery Green Space", "type": "other", "ward": "Kitwe Central", "area_sq_m": 15000}, "geometry": {"type": "Point", "coordinates": [28.2230, -12.8150]}},
        {"type": "Feature", "properties": {"id": 50, "name": "Copperbelt University Campus Green", "type": "other", "ward": "Riverside", "area_sq_m": 25000}, "geometry": {"type": "Point", "coordinates": [28.2200, -12.8090]}},
        {"type": "Feature", "properties": {"id": 51, "name": "Kitwe Teaching Hospital Gardens", "type": "other", "ward": "Kitwe Central", "area_sq_m": 8000}, "geometry": {"type": "Point", "coordinates": [28.2240, -12.8160]}}
    ]
};