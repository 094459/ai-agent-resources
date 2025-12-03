-- Sample queries for Star Wars test database

-- 1. Get all Force-sensitive characters with their details
SELECT * FROM character_details WHERE force_sensitive = TRUE;

-- 2. Show battle summary with locations and outcomes
SELECT * FROM battle_summary ORDER BY battle_date;

-- 3. Fleet statistics by faction
SELECT * FROM faction_fleets ORDER BY ship_count DESC;

-- 4. Characters who appeared in multiple films
SELECT character_name, COUNT(*) as film_count 
FROM character_filmography 
GROUP BY character_name 
HAVING COUNT(*) > 1 
ORDER BY film_count DESC;

-- 5. Planets with the most native characters
SELECT * FROM planet_stats 
WHERE native_characters > 0 
ORDER BY native_characters DESC 
LIMIT 10;

-- 6. Force users by faction
SELECT * FROM force_users ORDER BY force_sensitive_count DESC;

-- 7. Most expensive starships
SELECT name, model, cost_in_credits, starship_class 
FROM starships 
ORDER BY cost_in_credits DESC 
LIMIT 10;

-- 8. Battles with highest casualties
SELECT name, location_planet_id, casualties, battle_type 
FROM battles 
ORDER BY casualties DESC 
LIMIT 10;

-- 9. Characters and their starships
SELECT c.name as character_name, s.name as starship_name, cs.role
FROM characters c
JOIN character_starships cs ON c.character_id = cs.character_id
JOIN starships s ON cs.starship_id = s.starship_id
ORDER BY c.name;

-- 10. Species distribution across planets
SELECT s.name as species, p.name as planet, COUNT(c.character_id) as character_count
FROM species s
JOIN characters c ON s.species_id = c.species_id
JOIN planets p ON c.homeworld_id = p.planet_id
GROUP BY s.species_id, p.planet_id
HAVING character_count > 5
ORDER BY character_count DESC;
