-- Star Wars Database Views

-- Character details with homeworld and species info
CREATE VIEW character_details AS
SELECT 
    c.character_id,
    c.name,
    c.birth_year,
    c.gender,
    c.height,
    c.mass,
    c.force_sensitive,
    c.occupation,
    p.name AS homeworld,
    s.name AS species,
    f.name AS faction
FROM characters c
LEFT JOIN planets p ON c.homeworld_id = p.planet_id
LEFT JOIN species s ON c.species_id = s.species_id
LEFT JOIN factions f ON c.faction_id = f.faction_id;

-- Battle summary with location and factions
CREATE VIEW battle_summary AS
SELECT 
    b.battle_id,
    b.name AS battle_name,
    b.battle_date,
    b.duration_days,
    b.battle_type,
    p.name AS location,
    vf.name AS victor,
    lf.name AS defeated,
    b.casualties
FROM battles b
LEFT JOIN planets p ON b.location_planet_id = p.planet_id
LEFT JOIN factions vf ON b.victor_faction_id = vf.faction_id
LEFT JOIN factions lf ON b.loser_faction_id = lf.faction_id;

-- Starship fleet by faction
CREATE VIEW faction_fleets AS
SELECT 
    f.name AS faction,
    COUNT(s.starship_id) AS ship_count,
    AVG(s.length) AS avg_length,
    SUM(s.crew) AS total_crew,
    SUM(s.passengers) AS total_passenger_capacity
FROM factions f
LEFT JOIN starships s ON f.faction_id = s.faction_id
GROUP BY f.faction_id, f.name;

-- Character film appearances
CREATE VIEW character_filmography AS
SELECT 
    c.name AS character_name,
    f.title AS film_title,
    f.episode_number,
    f.release_date
FROM characters c
JOIN character_films cf ON c.character_id = cf.character_id
JOIN films f ON cf.film_id = f.film_id
ORDER BY c.name, f.episode_number;

-- Planet statistics
CREATE VIEW planet_stats AS
SELECT 
    p.name AS planet_name,
    p.population,
    p.climate,
    p.terrain,
    COUNT(DISTINCT c.character_id) AS native_characters,
    COUNT(DISTINCT b.battle_id) AS battles_fought
FROM planets p
LEFT JOIN characters c ON p.planet_id = c.homeworld_id
LEFT JOIN battles b ON p.planet_id = b.location_planet_id
GROUP BY p.planet_id, p.name, p.population, p.climate, p.terrain;

-- Force users by faction
CREATE VIEW force_users AS
SELECT 
    f.name AS faction,
    COUNT(c.character_id) AS force_sensitive_count,
    GROUP_CONCAT(c.name) AS force_users_list
FROM factions f
LEFT JOIN characters c ON f.faction_id = c.faction_id AND c.force_sensitive = TRUE
GROUP BY f.faction_id, f.name
HAVING COUNT(c.character_id) > 0;
