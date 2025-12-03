#!/bin/bash

sqlite3 starwars_test.db "
WITH force_user_stats AS (
  SELECT 
    f.name AS faction_name,
    COUNT(CASE WHEN c.force_sensitive = 1 THEN 1 END) AS force_users,
    COUNT(c.character_id) AS total_members,
    ROUND(COUNT(CASE WHEN c.force_sensitive = 1 THEN 1 END) * 100.0 / COUNT(c.character_id), 2) AS force_percentage
  FROM factions f
  LEFT JOIN characters c ON f.faction_id = c.faction_id
  GROUP BY f.faction_id, f.name
),
battle_performance AS (
  SELECT 
    f.name AS faction_name,
    COUNT(CASE WHEN b.victor_faction_id = f.faction_id THEN 1 END) AS victories,
    COUNT(CASE WHEN b.loser_faction_id = f.faction_id THEN 1 END) AS defeats,
    SUM(CASE WHEN b.victor_faction_id = f.faction_id THEN b.casualties ELSE 0 END) AS enemy_casualties_inflicted,
    SUM(CASE WHEN b.loser_faction_id = f.faction_id THEN b.casualties ELSE 0 END) AS own_casualties_suffered
  FROM factions f
  LEFT JOIN battles b ON f.faction_id IN (b.victor_faction_id, b.loser_faction_id)
  GROUP BY f.faction_id, f.name
),
fleet_power AS (
  SELECT 
    f.name AS faction_name,
    COUNT(s.starship_id) AS fleet_size,
    AVG(s.length) AS avg_ship_length,
    SUM(s.crew + s.passengers) AS total_capacity,
    AVG(s.hyperdrive_rating) AS avg_hyperdrive
  FROM factions f
  LEFT JOIN starships s ON f.faction_id = s.faction_id
  GROUP BY f.faction_id, f.name
)
SELECT 
  fus.faction_name,
  fus.total_members,
  fus.force_users,
  fus.force_percentage || '%' AS force_percentage,
  bp.victories,
  bp.defeats,
  CASE 
    WHEN (bp.victories + bp.defeats) > 0 
    THEN ROUND(bp.victories * 100.0 / (bp.victories + bp.defeats), 1) || '%'
    ELSE 'No battles'
  END AS win_rate,
  fp.fleet_size,
  ROUND(fp.avg_ship_length, 1) AS avg_ship_length,
  fp.total_capacity,
  ROUND(fp.avg_hyperdrive, 1) AS avg_hyperdrive_rating,
  bp.enemy_casualties_inflicted,
  bp.own_casualties_suffered,
  CASE 
    WHEN bp.own_casualties_suffered > 0 
    THEN ROUND(bp.enemy_casualties_inflicted * 1.0 / bp.own_casualties_suffered, 2)
    ELSE 'N/A'
  END AS kill_death_ratio,
  (SELECT COUNT(*) FROM planets p WHERE p.planet_id IN 
    (SELECT DISTINCT c2.homeworld_id FROM characters c2 WHERE c2.faction_id = 
      (SELECT faction_id FROM factions WHERE name = fus.faction_name)
    )
  ) AS controlled_worlds
FROM force_user_stats fus
JOIN battle_performance bp ON fus.faction_name = bp.faction_name  
JOIN fleet_power fp ON fus.faction_name = fp.faction_name
WHERE fus.total_members > 0
ORDER BY 
  (bp.victories * 2 + fus.force_users * 3 + fp.fleet_size) DESC,
  fus.force_percentage DESC;
"
