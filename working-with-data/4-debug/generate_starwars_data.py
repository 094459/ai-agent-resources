#!/usr/bin/env python3
import sqlite3
import random
from datetime import datetime, timedelta

def create_database():
    conn = sqlite3.connect('starwars_test.db')
    
    # Read and execute schema
    with open('starwars_schema.sql', 'r') as f:
        conn.executescript(f.read())
    
    # Films data
    films = [
        (1, 'A New Hope', 4, '1977-05-25', 'George Lucas', 'Gary Kurtz', 'It is a period of civil war...', 775000000),
        (2, 'The Empire Strikes Back', 5, '1980-05-21', 'Irvin Kershner', 'Gary Kurtz', 'It is a dark time for the Rebellion...', 547969618),
        (3, 'Return of the Jedi', 6, '1983-05-25', 'Richard Marquand', 'Howard Kazanjian', 'Luke Skywalker has returned...', 475106177),
        (4, 'The Phantom Menace', 1, '1999-05-19', 'George Lucas', 'Rick McCallum', 'Turmoil has engulfed the Galactic Republic...', 1027044677),
        (5, 'Attack of the Clones', 2, '2002-05-16', 'George Lucas', 'Rick McCallum', 'There is unrest in the Galactic Senate...', 653779970),
        (6, 'Revenge of the Sith', 3, '2005-05-19', 'George Lucas', 'Rick McCallum', 'War! The Republic is crumbling...', 868390560)
    ]
    
    # Species data
    species_data = [
        (1, 'Human', 'mammal', 1, 'Galactic Basic', 180, 120, 'caucasian, black, asian, hispanic', 'blonde, brown, black, red', 'brown, blue, green, hazel, grey, amber'),
        (2, 'Wookiee', 'mammal', 14, 'Shyriiwook', 210, 400, 'brown', 'brown, black', 'blue, green, yellow, brown, red'),
        (3, 'Rodian', 'sentient', 23, 'Galactic Basic', 170, 90, 'green, blue', 'n/a', 'black'),
        (4, 'Hutt', 'gastropod', 24, 'Huttese', 175, 1000, 'green, brown, tan', 'n/a', 'yellow, red'),
        (5, 'Yoda\'s species', 'mammal', None, 'Galactic Basic', 66, 900, 'green, yellow', 'brown, white', 'brown, green, yellow'),
        (6, 'Twi\'lek', 'mammal', 42, 'Twi\'leki', 200, 75, 'blue, green, yellow, pink, purple, tan, white', 'none', 'brown, blue, hazel, green, pink'),
        (7, 'Ewok', 'mammal', 7, 'Ewokese', 100, 60, 'brown', 'white, brown, black', 'orange, brown'),
        (8, 'Sullustan', 'mammal', 33, 'Sullustese', 180, 90, 'grey', 'none', 'black'),
        (9, 'Neimodian', 'unknown', 18, 'Neimoidia', 191, 90, 'grey, green', 'none', 'red, pink'),
        (10, 'Gungan', 'amphibian', 8, 'Gungan basic', 190, 65, 'brown, orange', 'none', 'orange')
    ]
    
    # Planets data
    planets_data = [
        (1, 'Tatooine', 23, 304, 10465, 'arid', '1 standard', 'desert', 1, 200000, 'Arkanis', 'Tatoo'),
        (2, 'Alderaan', 24, 364, 12500, 'temperate', '1 standard', 'grasslands, mountains', 40, 2000000000, 'Core Worlds', 'Alderaan'),
        (3, 'Yavin IV', 24, 4818, 10200, 'temperate, tropical', '1 standard', 'jungle, rainforests', 8, 1000, 'Outer Rim', 'Yavin'),
        (4, 'Hoth', 23, 549, 7200, 'frozen', '1.1 standard', 'tundra, ice caves, mountain ranges', 100, 0, 'Outer Rim', 'Hoth'),
        (5, 'Dagobah', 23, 341, 8900, 'murky', 'N/A', 'swamp, jungles', 8, 0, 'Outer Rim', 'Dagobah'),
        (6, 'Bespin', 12, 5110, 118000, 'temperate', '1.5 standard', 'gas giant', 0, 6000000, 'Outer Rim', 'Bespin'),
        (7, 'Endor', 18, 402, 4900, 'temperate', '0.85 standard', 'forests, mountains, lakes', 8, 30000000, 'Outer Rim', 'Endor'),
        (8, 'Naboo', 26, 312, 12120, 'temperate', '1 standard', 'grassy hills, swamps, forests, mountains', 12, 4500000000, 'Mid Rim', 'Naboo'),
        (9, 'Coruscant', 24, 368, 12240, 'temperate', '1 standard', 'cityscape, mountains', 0, 1000000000000, 'Core Worlds', 'Coruscant'),
        (10, 'Kamino', 27, 463, 19720, 'temperate', '1 standard', 'ocean', 100, 1000000000, 'Outer Rim', 'Kamino')
    ]
    
    # Factions data
    factions_data = [
        (1, 'Galactic Republic', 'Government', 'Chancellor Palpatine', 9, -25000, -19, 'Democratic government of the galaxy'),
        (2, 'Galactic Empire', 'Government', 'Emperor Palpatine', 9, -19, 4, 'Authoritarian regime that replaced the Republic'),
        (3, 'Rebel Alliance', 'Rebellion', 'Mon Mothma', 2, -2, 4, 'Resistance movement against the Empire'),
        (4, 'New Republic', 'Government', 'Mon Mothma', 9, 4, 25, 'Government that replaced the Empire'),
        (5, 'Jedi Order', 'Religious Order', 'Yoda', 9, -25000, -19, 'Force-sensitive peacekeepers'),
        (6, 'Sith Order', 'Religious Order', 'Darth Sidious', 9, -6900, 4, 'Dark side Force users'),
        (7, 'Trade Federation', 'Corporation', 'Nute Gunray', 18, -350, -32, 'Powerful trade organization'),
        (8, 'Separatist Alliance', 'Rebellion', 'Count Dooku', 18, -24, -19, 'Confederacy opposing the Republic'),
        (9, 'Bounty Hunters Guild', 'Criminal Organization', 'Various', None, -7000, None, 'Organization of bounty hunters'),
        (10, 'Hutt Cartel', 'Criminal Organization', 'Jabba the Hutt', 24, -15000, None, 'Criminal syndicate')
    ]
    
    # Insert base data
    conn.executemany('INSERT INTO films VALUES (?,?,?,?,?,?,?,?)', films)
    conn.executemany('INSERT INTO species VALUES (?,?,?,?,?,?,?,?,?,?)', species_data)
    conn.executemany('INSERT INTO planets VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', planets_data)
    conn.executemany('INSERT INTO factions VALUES (?,?,?,?,?,?,?,?)', factions_data)
    
    # Generate additional planets (100 total)
    planet_names = ['Ryloth', 'Sullust', 'Mon Cala', 'Kashyyyk', 'Geonosis', 'Mustafar', 'Utapau', 'Felucia', 
                   'Mygeeto', 'Cato Neimoidia', 'Saleucami', 'Ord Mantell', 'Malastare', 'Dathomir', 'Rishi',
                   'Iego', 'Teth', 'Quell', 'Dorin', 'Champala', 'Rodia', 'Nal Hutta', 'Toydaria', 'Malastare',
                   'Shili', 'Kalee', 'Umbara', 'Ringo Vinda', 'Lola Sayu', 'Zygerria', 'Mandalore', 'Concord Dawn',
                   'Krownest', 'Sundari', 'Lothal', 'Ryloth', 'Lasan', 'Jedha', 'Scarif', 'Eadu', 'Wobani',
                   'Jakku', 'Takodana', 'Hosnian Prime', 'Starkiller Base', 'Ahch-To', 'Crait', 'Cantonica',
                   'Exegol', 'Pasaana', 'Kijimi', 'Kef Bir', 'Ajan Kloss']
    
    climates = ['arid', 'temperate', 'tropical', 'frozen', 'murky', 'windy', 'hot', 'humid', 'dry', 'wet']
    terrains = ['desert', 'grasslands', 'mountains', 'jungle', 'forest', 'swamp', 'tundra', 'ice', 'ocean', 'cityscape', 'volcanic', 'canyon']
    
    for i in range(11, 101):
        name = random.choice(planet_names) + f" {i-10}"
        rotation = random.randint(18, 30)
        orbital = random.randint(200, 500)
        diameter = random.randint(5000, 15000)
        climate = random.choice(climates)
        terrain = random.choice(terrains)
        water = random.randint(0, 100)
        population = random.randint(1000, 10000000000)
        
        conn.execute('INSERT INTO planets VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', 
                    (i, name, rotation, orbital, diameter, climate, '1 standard', terrain, water, population, 'Outer Rim', name))
    
    # Generate characters (2000 total)
    first_names = ['Luke', 'Leia', 'Han', 'Chewbacca', 'Obi-Wan', 'Anakin', 'Padme', 'Yoda', 'Mace', 'Qui-Gon',
                  'Darth', 'Count', 'General', 'Captain', 'Commander', 'Admiral', 'Senator', 'Master', 'Jedi', 'Sith',
                  'Boba', 'Jango', 'Lando', 'C-3PO', 'R2-D2', 'BB-8', 'Rey', 'Finn', 'Poe', 'Kylo', 'Ahsoka', 'Ezra']
    
    last_names = ['Skywalker', 'Solo', 'Organa', 'Kenobi', 'Amidala', 'Windu', 'Jinn', 'Vader', 'Sidious', 'Dooku',
                 'Fett', 'Calrissian', 'Dameron', 'Ren', 'Tano', 'Bridger', 'Kanan', 'Hera', 'Sabine', 'Zeb',
                 'Thrawn', 'Tarkin', 'Krennic', 'Grievous', 'Maul', 'Savage', 'Ventress', 'Rex', 'Cody', 'Wolffe']
    
    occupations = ['Jedi Knight', 'Sith Lord', 'Pilot', 'Smuggler', 'Bounty Hunter', 'Senator', 'General', 'Admiral',
                  'Captain', 'Commander', 'Trooper', 'Mechanic', 'Diplomat', 'Spy', 'Assassin', 'Merchant', 'Farmer']
    
    for i in range(1, 2001):
        name = f"{random.choice(first_names)} {random.choice(last_names)} {i}"
        birth_year = f"{random.randint(-200, 50)}BBY" if random.randint(-200, 50) < 0 else f"{random.randint(1, 50)}ABY"
        gender = random.choice(['male', 'female', 'hermaphrodite', 'none'])
        height = random.randint(50, 250)
        mass = random.randint(30, 200)
        hair_color = random.choice(['brown', 'black', 'blonde', 'red', 'white', 'grey', 'none'])
        skin_color = random.choice(['fair', 'gold', 'white', 'light', 'green', 'grey', 'mottled green', 'pale', 'metal', 'dark'])
        eye_color = random.choice(['brown', 'blue', 'green', 'yellow', 'black', 'pink', 'red', 'orange'])
        homeworld_id = random.randint(1, 100)
        species_id = random.randint(1, 10)
        faction_id = random.randint(1, 10)
        force_sensitive = random.choice([True, False]) if random.random() < 0.1 else False
        occupation = random.choice(occupations)
        
        conn.execute('INSERT INTO characters VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (i, name, birth_year, gender, height, mass, hair_color, skin_color, eye_color,
                     homeworld_id, species_id, faction_id, force_sensitive, occupation))
    
    # Generate starships (500 total)
    ship_names = ['Star Destroyer', 'X-wing', 'TIE Fighter', 'Millennium Falcon', 'Death Star', 'Super Star Destroyer',
                 'A-wing', 'B-wing', 'Y-wing', 'TIE Interceptor', 'Lambda Shuttle', 'Nebulon-B Frigate', 'Mon Calamari Cruiser',
                 'Corellian Corvette', 'Dreadnought', 'Interdictor', 'Victory Star Destroyer', 'Executor', 'Home One']
    
    manufacturers = ['Kuat Drive Yards', 'Incom Corporation', 'Sienar Fleet Systems', 'Corellian Engineering Corporation',
                    'Mon Calamari Shipyards', 'Rendili StarDrive', 'Republic Engineering Corporation']
    
    ship_classes = ['Star Destroyer', 'Starfighter', 'Frigate', 'Corvette', 'Cruiser', 'Dreadnought', 'Transport', 'Shuttle']
    
    for i in range(1, 501):
        name = f"{random.choice(ship_names)} {i}"
        model = f"Model-{random.randint(1, 100)}"
        manufacturer = random.choice(manufacturers)
        cost = random.randint(50000, 100000000)
        length = random.randint(10, 5000)
        speed = random.randint(500, 1500)
        crew = random.randint(1, 50000)
        passengers = random.randint(0, 10000)
        cargo = random.randint(100, 1000000)
        consumables = random.choice(['1 day', '1 week', '1 month', '6 months', '1 year', '2 years'])
        hyperdrive = random.choice([1.0, 1.5, 2.0, 3.0, 4.0, 5.0])
        mglt = random.randint(50, 150)
        ship_class = random.choice(ship_classes)
        faction_id = random.randint(1, 10)
        
        conn.execute('INSERT INTO starships VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (i, name, model, manufacturer, cost, length, speed, crew, passengers, cargo,
                     consumables, hyperdrive, mglt, ship_class, faction_id))
    
    # Generate battles (200 total)
    battle_names = ['Battle of Yavin', 'Battle of Hoth', 'Battle of Endor', 'Battle of Naboo', 'Battle of Geonosis',
                   'Battle of Coruscant', 'Battle of Kashyyyk', 'Battle of Utapau', 'Battle of Mygeeto', 'Battle of Felucia',
                   'Siege of Mandalore', 'Battle of Ryloth', 'Battle of Christophsis', 'Battle of Teth', 'Battle of Malastare']
    
    battle_types = ['Space Battle', 'Ground Assault', 'Siege', 'Skirmish', 'Naval Battle', 'Aerial Combat']
    
    for i in range(1, 201):
        name = f"{random.choice(battle_names)} {i}" if i > 15 else battle_names[i-1] if i <= len(battle_names) else f"Battle {i}"
        location_id = random.randint(1, 100)
        battle_date = f"{random.randint(-50, 50)}{'BBY' if random.randint(-50, 50) < 0 else 'ABY'}"
        duration = random.randint(1, 365)
        battle_type = random.choice(battle_types)
        victor_id = random.randint(1, 10)
        loser_id = random.randint(1, 10)
        while loser_id == victor_id:
            loser_id = random.randint(1, 10)
        casualties = random.randint(100, 100000)
        description = f"A {battle_type.lower()} that lasted {duration} days with {casualties} casualties."
        
        conn.execute('INSERT INTO battles VALUES (?,?,?,?,?,?,?,?,?,?)',
                    (i, name, location_id, battle_date, duration, battle_type, victor_id, loser_id, casualties, description))
    
    # Generate junction table data
    # Character-Film relationships
    for i in range(1, 5000):
        character_id = random.randint(1, 2000)
        film_id = random.randint(1, 6)
        try:
            conn.execute('INSERT INTO character_films VALUES (?,?)', (character_id, film_id))
        except sqlite3.IntegrityError:
            pass  # Skip duplicates
    
    # Character-Starship relationships
    roles = ['Pilot', 'Gunner', 'Navigator', 'Engineer', 'Captain', 'Crew Member']
    for i in range(1, 3000):
        character_id = random.randint(1, 2000)
        starship_id = random.randint(1, 500)
        role = random.choice(roles)
        try:
            conn.execute('INSERT INTO character_starships VALUES (?,?,?)', (character_id, starship_id, role))
        except sqlite3.IntegrityError:
            pass
    
    # Battle participants
    battle_roles = ['Commander', 'Soldier', 'Pilot', 'Officer', 'Specialist', 'Medic']
    for i in range(1, 4000):
        battle_id = random.randint(1, 200)
        character_id = random.randint(1, 2000)
        faction_id = random.randint(1, 10)
        role = random.choice(battle_roles)
        try:
            conn.execute('INSERT INTO battle_participants VALUES (?,?,?,?)', (battle_id, character_id, faction_id, role))
        except sqlite3.IntegrityError:
            pass
    
    conn.commit()
    
    # Create views
    with open('starwars_views.sql', 'r') as f:
        conn.executescript(f.read())
    
    conn.close()
    print("Star Wars test database created successfully!")
    print("Database: starwars_test.db")
    print("Total records:")
    print("- Films: 6")
    print("- Species: 10") 
    print("- Planets: 100")
    print("- Factions: 10")
    print("- Characters: 2,000")
    print("- Starships: 500")
    print("- Battles: 200")
    print("- Character-Film relationships: ~5,000")
    print("- Character-Starship relationships: ~3,000")
    print("- Battle participants: ~4,000")

if __name__ == "__main__":
    create_database()
