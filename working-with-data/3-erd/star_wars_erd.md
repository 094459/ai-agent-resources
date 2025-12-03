# Star Wars Database ERD

## Mermaid Entity Relationship Diagram

```mermaid
erDiagram
    CHARACTERS {
        int id PK
        text name
        text species
        text gender
        real height
        real weight
        text hair_color
        text eye_color
        text skin_color
        int year_born
        text homeworld
        int year_died
        text description
    }
    
    SPECIES {
        int id PK
        text name
        text classification
        text designation
        real average_height
        text skin_colors
        text hair_colors
        text eye_colors
        real average_lifespan
        text language
        text homeworld
    }
    
    PLANETS {
        int id PK
        text name
        real diameter
        real rotation_period
        real orbital_period
        text gravity
        int population
        text climate
        text terrain
        real surface_water
        text residents
        text films
    }
    
    FILMS {
        int id PK
        text title
        date release_date
        text director
        text producer
        text opening_crawl
    }
    
    STARSHIPS {
        int id PK
        text name
        text model
        text manufacturer
        real cost_in_credits
        real length
        real max_atmosphering_speed
        int crew
        int passengers
        real cargo_capacity
        text consumables
        real hyperdrive_rating
        int MGLT
        text starship_class
        text pilots
        text films
    }
    
    VEHICLES {
        int id PK
        text name
        text model
        text manufacturer
        real cost_in_credits
        real length
        real max_atmosphering_speed
        int crew
        int passengers
        real cargo_capacity
        text consumables
        text vehicle_class
        text pilots
        text films
    }
    
    DROIDS {
        int id PK
        text name
        text model
        text manufacturer
        real height
        real mass
        text sensor_color
        text plating_color
        text primary_function
        text films
    }
    
    WEAPONS {
        int id PK
        text name
        text model
        text manufacturer
        real cost_in_credits
        real length
        text type
        text description
        text films
    }
    
    ORGANIZATIONS {
        int id PK
        text name
        int founded
        int dissolved
        text leader
        text members
        text affiliation
        text description
        text films
    }
    
    CITIES {
        int id PK
        text name
        text planet
        int population
        text description
    }
    
    BATTLES {
        int id PK
        text name
        text location
        text date
        text result
        text participants
    }
    
    EVENTS {
        int id PK
        text event_name
        text date
        text location
        text description
    }
    
    TIMELINE {
        int id PK
        text event
        text year
    }
    
    QUOTES {
        int id PK
        text character_name
        text quote
        text source
    }
    
    MUSIC {
        int id PK
        text title
        text composer
        text type
        text associated_with
    }

    CHARACTERS ||--o{ SPECIES : "belongs to"
    CHARACTERS ||--o{ PLANETS : "homeworld"
    SPECIES ||--o{ PLANETS : "homeworld"
    CITIES ||--o{ PLANETS : "located on"
    QUOTES ||--o{ CHARACTERS : "attributed to"
    FILMS ||--o{ CHARACTERS : "appears in"
    FILMS ||--o{ STARSHIPS : "appears in"
    FILMS ||--o{ VEHICLES : "appears in"
    FILMS ||--o{ DROIDS : "appears in"
    FILMS ||--o{ WEAPONS : "appears in"
    FILMS ||--o{ ORGANIZATIONS : "appears in"
```

## Key Relationships

1. **Characters** → **Species**: Characters belong to species
2. **Characters** → **Planets**: Characters have homeworlds
3. **Species** → **Planets**: Species have homeworlds
4. **Cities** → **Planets**: Cities are located on planets
5. **Films**: Central entity referenced by many tables (characters, starships, vehicles, droids, weapons, organizations)
6. **Pilots**: Referenced in starships and vehicles (likely character names)
7. **Quotes** → **Characters**: Quotes are attributed to characters
8. **Battles/Events**: Location-based entities that may reference planets

## Entity Summary

- **Core Entities**: Characters, Species, Planets, Films
- **Vehicles & Technology**: Starships, Vehicles, Droids, Weapons
- **Organizations & Events**: Organizations, Battles, Events, Timeline
- **Locations**: Cities, Planets
- **Media**: Films, Music, Quotes

Note: Many relationships are stored as text fields (e.g., pilots, films, members) rather than proper foreign keys, indicating a denormalized design.
