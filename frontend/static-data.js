// Static green spaces data for GitHub Pages deployment
const STATIC_GREEN_SPACES_DATA = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.213611, -12.817778] },
            "properties": { "id": 1, "name": "Kitwe City Square", "type": "park", "area_sq_m": 18000, "ward": "City Centre" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.210000, -12.815000] },
            "properties": { "id": 2, "name": "Central Park Kitwe", "type": "park", "area_sq_m": 35000, "ward": "City Centre" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.226389, -12.825556] },
            "properties": { "id": 3, "name": "Copperbelt University Arboretum", "type": "forest", "area_sq_m": 42000, "ward": "Riverside" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.240000, -12.800000] },
            "properties": { "id": 4, "name": "Kitwe Golf Club", "type": "golf course", "area_sq_m": 380000, "ward": "Ndeke" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.208333, -12.827778] },
            "properties": { "id": 5, "name": "Parklands Community Park", "type": "park", "area_sq_m": 22000, "ward": "Parklands" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.206667, -12.831111] },
            "properties": { "id": 6, "name": "Riverside Gardens", "type": "garden", "area_sq_m": 15000, "ward": "Parklands" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.204444, -12.829167] },
            "properties": { "id": 7, "name": "Mukuba Park", "type": "park", "area_sq_m": 28000, "ward": "Parklands" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.218056, -12.810833] },
            "properties": { "id": 8, "name": "Nkana Sports Complex", "type": "recreational", "area_sq_m": 55000, "ward": "Nkana" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.221111, -12.808333] },
            "properties": { "id": 9, "name": "Nkana Dam Recreation Area", "type": "park", "area_sq_m": 95000, "ward": "Nkana" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.231944, -12.805000] },
            "properties": { "id": 10, "name": "Wusakile Community Garden", "type": "garden", "area_sq_m": 12000, "ward": "Wusakile" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.195833, -12.834722] },
            "properties": { "id": 11, "name": "Chimwemwe Children's Park", "type": "park", "area_sq_m": 18000, "ward": "Chimwemwe" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.198056, -12.836111] },
            "properties": { "id": 12, "name": "Chimwemwe Football Ground", "type": "recreational", "area_sq_m": 32000, "ward": "Chimwemwe" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.200000, -12.838889] },
            "properties": { "id": 13, "name": "Chimwemwe Market Garden", "type": "garden", "area_sq_m": 8500, "ward": "Chimwemwe" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.234722, -12.832778] },
            "properties": { "id": 14, "name": "Mindolo Dam Park", "type": "park", "area_sq_m": 120000, "ward": "Mindolo" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.232500, -12.830556] },
            "properties": { "id": 15, "name": "Mindolo Ecumenical Centre Gardens", "type": "garden", "area_sq_m": 25000, "ward": "Mindolo" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.236111, -12.828333] },
            "properties": { "id": 16, "name": "Mindolo Lake View Park", "type": "park", "area_sq_m": 42000, "ward": "Mindolo" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.186111, -12.850000] },
            "properties": { "id": 17, "name": "Buchi Park", "type": "park", "area_sq_m": 32000, "ward": "Buchi" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.188889, -12.847222] },
            "properties": { "id": 18, "name": "Buchi Football Stadium", "type": "recreational", "area_sq_m": 48000, "ward": "Buchi" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.183333, -12.845833] },
            "properties": { "id": 19, "name": "Buchi Community Forest", "type": "forest", "area_sq_m": 65000, "ward": "Buchi" }
        },
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [28.255556, -12.783333] },
            "properties": { "id": 20, "name": "Garneton Public Park", "type": "park", "area_sq_m": 29000, "ward": "Garneton" }
        }
    ]
};

// Function to simulate API call for static deployment
window.getStaticGreenSpaces = function() {
    return Promise.resolve(STATIC_GREEN_SPACES_DATA);
};