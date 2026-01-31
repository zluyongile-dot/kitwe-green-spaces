-- Supabase Database Setup for Kitwe Green Spaces
-- Run this in Supabase SQL Editor

-- Create green_spaces table
CREATE TABLE IF NOT EXISTS green_spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100),
    area_hectares FLOAT,
    ward VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    description TEXT,
    facilities TEXT,
    accessibility TEXT,
    environmental_impact TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert your 51 green spaces
INSERT INTO green_spaces (name, type, area_hectares, ward, latitude, longitude, description, facilities, accessibility, environmental_impact) VALUES
('Kitwe City Square', 'public_square', 1.8, 'City Centre', -12.817778, 28.213611, 'Central public square in the heart of Kitwe', 'Benches, fountains, walkways', 'Fully accessible', 'Urban cooling, air purification'),
('Central Park Kitwe', 'park', 3.5, 'City Centre', -12.815000, 28.210000, 'Main recreational park in Kitwe city center', 'Playground, walking paths, benches, sports area', 'Wheelchair accessible', 'High - provides urban cooling and biodiversity'),
('Copperbelt University Arboretum', 'forest', 4.2, 'Riverside', -12.825556, 28.226389, 'Educational forest area with diverse tree species', 'Nature trails, research areas, educational signage', 'Partially accessible', 'Very high - carbon sequestration, biodiversity conservation'),
('Kitwe Golf Club', 'golf_course', 38.0, 'Ndeke', -12.800000, 28.240000, '18-hole golf course with maintained green spaces', 'Golf course, clubhouse, parking', 'Members only', 'Moderate - large green area but limited public access'),
('Parklands Community Park', 'park', 2.2, 'Parklands', -12.827778, 28.208333, 'Community park serving Parklands residential area', 'Children''s playground, sports field, picnic area', 'Fully accessible', 'High - community recreation and air quality improvement'),
('Riverside Gardens', 'garden', 1.5, 'Parklands', -12.831111, 28.206667, 'Botanical gardens along the riverside', 'Walking paths, flower beds, seating areas', 'Wheelchair accessible', 'High - biodiversity, water management'),
('Mukuba Park', 'park', 2.8, 'Parklands', -12.829167, 28.204444, 'Large recreational park with multiple facilities', 'Sports courts, playground, amphitheater', 'Fully accessible', 'High - recreation, air purification, urban cooling'),
('Nkana Sports Complex', 'sports_field', 5.5, 'Nkana', -12.810833, 28.218056, 'Multi-sport complex with grass fields', 'Football fields, athletics track, changing rooms', 'Public access during events', 'Moderate - large grass areas, limited trees'),
('Nkana Dam Recreation Area', 'park', 9.5, 'Nkana', -12.808333, 28.221111, 'Recreational area around Nkana Dam', 'Fishing spots, picnic areas, walking trails', 'Partially accessible', 'Very high - water ecosystem, wildlife habitat'),
('Wusakile Community Garden', 'garden', 1.2, 'Wusakile', -12.805000, 28.231944, 'Community-managed vegetable and flower garden', 'Garden plots, tool shed, water access', 'Community members', 'High - food security, community engagement'),
('Chimwemwe Children''s Park', 'park', 1.8, 'Chimwemwe', -12.834722, 28.195833, 'Dedicated children''s recreational park', 'Playground equipment, sandbox, seating', 'Fully accessible', 'Moderate - child development, limited green coverage'),
('Chimwemwe Football Ground', 'sports_field', 3.2, 'Chimwemwe', -12.836111, 28.198056, 'Community football field with grass surface', 'Football field, goalposts, spectator area', 'Public access', 'Moderate - grass surface, community recreation'),
('Chimwemwe Market Garden', 'garden', 0.85, 'Chimwemwe', -12.838889, 28.200000, 'Small market garden for local produce', 'Vegetable plots, market stalls, storage', 'Vendors and customers', 'High - local food production, reduced transport emissions'),
('Mindolo Dam Park', 'park', 12.0, 'Mindolo', -12.832778, 28.234722, 'Large park surrounding Mindolo Dam', 'Walking trails, fishing areas, picnic spots', 'Public access with some restrictions', 'Very high - water ecosystem, large green area'),
('Mindolo Ecumenical Centre Gardens', 'garden', 2.5, 'Mindolo', -12.830556, 28.232500, 'Well-maintained gardens at the ecumenical center', 'Flower gardens, meditation areas, pathways', 'Visitors welcome', 'High - biodiversity, peaceful environment'),
('Mindolo Lake View Park', 'park', 4.2, 'Mindolo', -12.828333, 28.236111, 'Scenic park with lake views', 'Viewing platforms, benches, walking paths', 'Fully accessible', 'High - scenic value, air quality improvement'),
('Buchi Park', 'park', 3.2, 'Buchi', -12.850000, 28.186111, 'Community park in Buchi residential area', 'Playground, sports area, community hall', 'Public access', 'High - community recreation, air purification'),
('Buchi Football Stadium', 'sports_field', 4.8, 'Buchi', -12.847222, 28.188889, 'Local football stadium with grass pitch', 'Football field, stands, changing rooms', 'Public during events', 'Moderate - grass surface, community sports'),
('Buchi Community Forest', 'forest', 6.5, 'Buchi', -12.845833, 28.183333, 'Community-managed forest area', 'Nature trails, picnic areas, forest education', 'Public access with guides', 'Very high - carbon sequestration, biodiversity'),
('Garneton Public Park', 'park', 2.9, 'Garneton', -12.783333, 28.255556, 'Public park serving Garneton community', 'Playground, sports court, picnic area', 'Fully accessible', 'High - community recreation, green space'),
('Itimpi Nature Reserve', 'forest', 18.0, 'Itimpi', -12.775000, 28.266667, 'Protected nature reserve with indigenous species', 'Nature trails, bird watching areas, research station', 'Guided tours only', 'Very high - conservation, research, biodiversity'),
('Kamitondo Community Garden', 'garden', 1.1, 'Kamitondo', -12.766667, 28.277778, 'Community vegetable and herb garden', 'Garden plots, composting area, tool storage', 'Community members', 'High - food security, waste reduction'),
('Miseshi Public Square', 'public_square', 1.4, 'Miseshi', -12.791667, 28.244444, 'Central square for community gatherings', 'Open space, seating, market area', 'Fully accessible', 'Moderate - community space, limited vegetation'),
('Riverside Nature Trail', 'forest', 8.8, 'Riverside', -12.822222, 28.229167, 'Nature trail along the river with forest cover', 'Walking trails, bird watching points, rest areas', 'Hiking trails, moderate difficulty', 'Very high - riparian ecosystem, wildlife corridor'),
('Kitwe Tennis Club Gardens', 'garden', 0.95, 'City Centre', -12.818889, 28.215000, 'Landscaped gardens at the tennis club', 'Tennis courts, garden seating, clubhouse', 'Members and guests', 'Moderate - limited size but well-maintained'),
('Copperbelt Museum Gardens', 'garden', 1.25, 'City Centre', -12.816667, 28.212222, 'Educational gardens showcasing local flora', 'Educational displays, walking paths, museum access', 'Public access during museum hours', 'High - education, biodiversity showcase'),
('Kitwe Central Hospital Gardens', 'garden', 2.1, 'City Centre', -12.813889, 28.209167, 'Therapeutic gardens at the central hospital', 'Healing gardens, seating areas, accessible paths', 'Patients, visitors, staff', 'High - therapeutic benefits, air quality'),
('Ndeke Village Green', 'park', 1.65, 'Ndeke', -12.803333, 28.237500, 'Traditional village green space', 'Open grass area, traditional meeting space', 'Community access', 'Moderate - cultural significance, green space'),
('Kwacha Roundabout Garden', 'garden', 0.55, 'Kwacha', -12.823333, 28.205556, 'Landscaped roundabout with ornamental plants', 'Ornamental gardens, traffic management', 'Visual access only', 'Moderate - air quality, aesthetic value'),
('Mufuchani Stream Park', 'park', 3.1, 'Chamboli', -12.841667, 28.191667, 'Linear park along Mufuchani Stream', 'Walking paths, stream access, picnic areas', 'Public access', 'Very high - riparian habitat, flood management'),
('Chisokone Market Green Space', 'public_square', 1.35, 'City Centre', -12.819444, 28.211389, 'Green space adjacent to Chisokone Market', 'Market overflow area, seating, shade trees', 'Public access', 'Moderate - urban cooling, market support'),
('Kitwe Stadium Gardens', 'garden', 2.3, 'City Centre', -12.814500, 28.216000, 'Gardens surrounding the main stadium', 'Landscaped areas, parking, walkways', 'Public during events', 'Moderate - aesthetic value, air quality'),
('Zambia Airways Park', 'park', 4.1, 'Ndeke', -12.798000, 28.242000, 'Aviation-themed park near the airport area', 'Playground, aviation displays, picnic areas', 'Fully accessible', 'High - recreation, educational value'),
('Copperbelt Energy Corporation Gardens', 'garden', 1.8, 'City Centre', -12.812000, 28.214000, 'Corporate gardens with sustainable landscaping', 'Sustainable gardens, employee recreation', 'Employees and visitors', 'High - sustainable practices demonstration'),
('Kitwe Boys Secondary School Forest', 'forest', 5.2, 'Parklands', -12.825000, 28.207000, 'School forest for environmental education', 'Nature trails, outdoor classrooms, research plots', 'Students and educational groups', 'Very high - education, carbon sequestration'),
('Kafue River Green Corridor', 'forest', 15.5, 'Riverside', -12.840000, 28.195000, 'Protected corridor along Kafue River', 'Nature trails, bird watching, research station', 'Guided access only', 'Very high - river ecosystem, wildlife corridor'),
('Kitwe Civic Centre Gardens', 'garden', 1.6, 'City Centre', -12.816000, 28.213500, 'Formal gardens at the civic center', 'Formal gardens, fountains, ceremony areas', 'Public access', 'Moderate - civic pride, air quality'),
('Mopani Copper Mines Recreation Park', 'park', 7.8, 'Nkana', -12.806000, 28.220000, 'Employee recreation park with multiple facilities', 'Sports facilities, picnic areas, children''s play', 'Employees and families', 'High - large green space, recreation'),
('Kitwe Teaching Hospital Healing Garden', 'garden', 1.4, 'City Centre', -12.811000, 28.208000, 'Therapeutic garden for patients and families', 'Healing plants, quiet areas, accessible paths', 'Patients, families, staff', 'High - therapeutic benefits, air purification'),
('Kitwe Youth Centre Sports Ground', 'sports_field', 3.5, 'Parklands', -12.830000, 28.205000, 'Multi-sport facility for youth programs', 'Football field, basketball court, athletics track', 'Youth programs and community', 'Moderate - youth development, green space'),
('Chamboli Community Forest', 'forest', 9.2, 'Chamboli', -12.845000, 28.188000, 'Community-managed forest for sustainable use', 'Sustainable harvesting areas, education center', 'Community members with permits', 'Very high - sustainable forestry, carbon storage'),
('Kitwe Market Square Garden', 'garden', 0.8, 'City Centre', -12.818000, 28.212000, 'Small garden providing respite from market activity', 'Seating, shade trees, small vendor spaces', 'Public access', 'Moderate - urban cooling, market support'),
('Nkana East Community Park', 'park', 2.7, 'Nkana', -12.812000, 28.225000, 'Community park serving eastern Nkana residents', 'Playground, sports court, community garden', 'Public access', 'High - community recreation, food production'),
('Kitwe Industrial Area Green Buffer', 'forest', 6.8, 'Industrial', -12.835000, 28.230000, 'Green buffer zone around industrial facilities', 'Pollution mitigation trees, monitoring stations', 'Restricted access', 'Very high - pollution mitigation, air quality'),
('Wusakile Sports Complex Green Space', 'sports_field', 4.3, 'Wusakile', -12.803000, 28.235000, 'Sports complex with extensive green areas', 'Multiple sports fields, spectator areas', 'Public during events', 'Moderate - large grass areas, community sports'),
('Kitwe Airport Approach Green Corridor', 'forest', 11.2, 'Ndeke', -12.795000, 28.245000, 'Green corridor along airport approach path', 'Wildlife corridors, noise barriers, research areas', 'Restricted access', 'Very high - wildlife corridor, noise reduction'),
('Mindolo Dam Wetlands', 'wetland', 8.5, 'Mindolo', -12.835000, 28.238000, 'Natural wetlands supporting diverse wildlife', 'Bird watching hides, boardwalks, research station', 'Guided tours only', 'Very high - wetland ecosystem, water filtration'),
('Kitwe Cemetery Memorial Garden', 'garden', 3.2, 'City Centre', -12.820000, 28.218000, 'Memorial garden with mature trees and peaceful spaces', 'Memorial areas, mature trees, quiet paths', 'Public access during hours', 'High - mature trees, peaceful environment'),
('Copperbelt University Student Recreation Park', 'park', 5.1, 'Riverside', -12.828000, 28.228000, 'Recreation park for university students and staff', 'Sports facilities, study areas, amphitheater', 'University community', 'High - education support, large green space'),
('Kitwe Railway Station Gardens', 'garden', 1.3, 'City Centre', -12.815500, 28.211000, 'Historic gardens at the railway station', 'Historic landscaping, waiting areas, heritage trees', 'Public access', 'Moderate - heritage value, air quality'),
('Kafue River Confluence Park', 'park', 12.8, 'Riverside', -12.850000, 28.200000, 'Large park at the confluence of rivers', 'River access, fishing areas, picnic facilities', 'Public access', 'Very high - river ecosystem, large green area');

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_green_spaces_ward ON green_spaces(ward);
CREATE INDEX IF NOT EXISTS idx_green_spaces_type ON green_spaces(type);
CREATE INDEX IF NOT EXISTS idx_green_spaces_location ON green_spaces(latitude, longitude);

-- Verify the data
SELECT 
    COUNT(*) as total_spaces,
    SUM(area_hectares) as total_area_hectares,
    COUNT(DISTINCT ward) as unique_wards,
    COUNT(DISTINCT type) as unique_types
FROM green_spaces;