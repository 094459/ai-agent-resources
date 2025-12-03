-- Star Wars Test Database Schema
-- SQLite compatible

-- Films table
CREATE TABLE films (
    film_id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    episode_number INTEGER,
    release_date DATE,
    director VARCHAR(50),
    producer VARCHAR(100),
    opening_crawl TEXT,
    box_office DECIMAL(12,2)
);

-- Species table
CREATE TABLE species (
    species_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    classification VARCHAR(30),
    homeworld_id INTEGER,
    language VARCHAR(50),
    average_height INTEGER,
    average_lifespan INTEGER,
    skin_colors VARCHAR(100),
    hair_colors VARCHAR(100),
    eye_colors VARCHAR(100)
);

-- Planets table
CREATE TABLE planets (
    planet_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    rotation_period INTEGER,
    orbital_period INTEGER,
    diameter INTEGER,
    climate VARCHAR(50),
    gravity VARCHAR(20),
    terrain VARCHAR(100),
    surface_water INTEGER,
    population BIGINT,
    sector VARCHAR(50),
    system VARCHAR(50)
);

-- Factions table
CREATE TABLE factions (
    faction_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type VARCHAR(30),
    leader VARCHAR(50),
    homeworld_id INTEGER,
    founded_year INTEGER,
    dissolved_year INTEGER,
    description TEXT
);

-- Characters table
CREATE TABLE characters (
    character_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    birth_year VARCHAR(20),
    gender VARCHAR(20),
    height INTEGER,
    mass INTEGER,
    hair_color VARCHAR(30),
    skin_color VARCHAR(30),
    eye_color VARCHAR(30),
    homeworld_id INTEGER,
    species_id INTEGER,
    faction_id INTEGER,
    force_sensitive BOOLEAN DEFAULT FALSE,
    occupation VARCHAR(50),
    FOREIGN KEY (homeworld_id) REFERENCES planets(planet_id),
    FOREIGN KEY (species_id) REFERENCES species(species_id),
    FOREIGN KEY (faction_id) REFERENCES factions(faction_id)
);

-- Starships table
CREATE TABLE starships (
    starship_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    model VARCHAR(50),
    manufacturer VARCHAR(50),
    cost_in_credits BIGINT,
    length DECIMAL(10,2),
    max_atmosphering_speed INTEGER,
    crew INTEGER,
    passengers INTEGER,
    cargo_capacity BIGINT,
    consumables VARCHAR(30),
    hyperdrive_rating DECIMAL(3,1),
    mglt INTEGER,
    starship_class VARCHAR(30),
    faction_id INTEGER,
    FOREIGN KEY (faction_id) REFERENCES factions(faction_id)
);

-- Battles table
CREATE TABLE battles (
    battle_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location_planet_id INTEGER,
    battle_date VARCHAR(20),
    duration_days INTEGER,
    battle_type VARCHAR(30),
    victor_faction_id INTEGER,
    loser_faction_id INTEGER,
    casualties INTEGER,
    description TEXT,
    FOREIGN KEY (location_planet_id) REFERENCES planets(planet_id),
    FOREIGN KEY (victor_faction_id) REFERENCES factions(faction_id),
    FOREIGN KEY (loser_faction_id) REFERENCES factions(faction_id)
);

-- Junction tables for many-to-many relationships
CREATE TABLE character_films (
    character_id INTEGER,
    film_id INTEGER,
    PRIMARY KEY (character_id, film_id),
    FOREIGN KEY (character_id) REFERENCES characters(character_id),
    FOREIGN KEY (film_id) REFERENCES films(film_id)
);

CREATE TABLE character_starships (
    character_id INTEGER,
    starship_id INTEGER,
    role VARCHAR(30),
    PRIMARY KEY (character_id, starship_id),
    FOREIGN KEY (character_id) REFERENCES characters(character_id),
    FOREIGN KEY (starship_id) REFERENCES starships(starship_id)
);

CREATE TABLE battle_participants (
    battle_id INTEGER,
    character_id INTEGER,
    faction_id INTEGER,
    role VARCHAR(30),
    PRIMARY KEY (battle_id, character_id),
    FOREIGN KEY (battle_id) REFERENCES battles(battle_id),
    FOREIGN KEY (character_id) REFERENCES characters(character_id),
    FOREIGN KEY (faction_id) REFERENCES factions(faction_id)
);

-- Indexes for better performance
CREATE INDEX idx_characters_homeworld ON characters(homeworld_id);
CREATE INDEX idx_characters_species ON characters(species_id);
CREATE INDEX idx_characters_faction ON characters(faction_id);
CREATE INDEX idx_battles_location ON battles(location_planet_id);
CREATE INDEX idx_starships_faction ON starships(faction_id);
