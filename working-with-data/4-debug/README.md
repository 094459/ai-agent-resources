# Star Wars Test Database

A comprehensive SQLite test database with Star Wars themed data containing thousands of records across multiple related tables.

## Database Structure

### Main Tables
- **films** (6 records) - Star Wars movies with details
- **species** (10 records) - Different alien species 
- **planets** (100 records) - Planets across the galaxy
- **factions** (10 records) - Organizations and governments
- **characters** (2,000 records) - Individual characters
- **starships** (500 records) - Spaceships and vehicles
- **battles** (200 records) - Military conflicts

### Junction Tables (Many-to-Many Relationships)
- **character_films** (~5,000 records) - Character appearances in films
- **character_starships** (~3,000 records) - Character-ship relationships
- **battle_participants** (~4,000 records) - Characters in battles

### Views
- **character_details** - Characters with homeworld, species, and faction info
- **battle_summary** - Battles with location and faction details
- **faction_fleets** - Starship statistics by faction
- **character_filmography** - Character film appearances
- **planet_stats** - Planet statistics with character and battle counts
- **force_users** - Force-sensitive characters by faction

## Files

- `starwars_schema.sql` - Database schema definition
- `starwars_views.sql` - View definitions
- `generate_starwars_data.py` - Python script to generate test data
- `starwars_test.db` - SQLite database file
- `sample_queries.sql` - Example queries to explore the data

## Usage

### Connect to Database
```bash
sqlite3 starwars_test.db
```

### Sample Queries

```sql
-- Get all Force-sensitive characters
SELECT * FROM character_details WHERE force_sensitive = TRUE;

-- Show battle outcomes
SELECT * FROM battle_summary ORDER BY casualties DESC;

-- Fleet sizes by faction
SELECT * FROM faction_fleets ORDER BY ship_count DESC;

-- Most expensive starships
SELECT name, cost_in_credits FROM starships ORDER BY cost_in_credits DESC LIMIT 10;
```

### Regenerate Database
```bash
python3 generate_starwars_data.py
```

## Data Statistics

- Total records: ~15,000+
- Characters: 2,000 with varied attributes (species, homeworld, faction, Force sensitivity)
- Starships: 500 with technical specifications
- Planets: 100 with environmental data
- Battles: 200 with casualties and outcomes
- Relationships: ~12,000 junction table records

## Features

- Realistic Star Wars themed data
- Complex relationships between entities
- Useful views for common queries
- Proper indexing for performance
- Foreign key constraints for data integrity
- Mix of canonical and generated content

Perfect for testing database operations, practicing SQL queries, or demonstrating relational database concepts.
