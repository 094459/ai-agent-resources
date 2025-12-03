from flask import Flask, render_template, jsonify
import sqlite3
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('star_wars.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/characters')
def get_characters():
    conn = get_db_connection()
    characters = conn.execute('SELECT * FROM characters LIMIT 50').fetchall()
    conn.close()
    return jsonify([dict(row) for row in characters])

@app.route('/api/planets')
def get_planets():
    conn = get_db_connection()
    planets = conn.execute('SELECT * FROM planets LIMIT 50').fetchall()
    conn.close()
    return jsonify([dict(row) for row in planets])

@app.route('/api/films')
def get_films():
    conn = get_db_connection()
    films = conn.execute('SELECT * FROM films').fetchall()
    conn.close()
    return jsonify([dict(row) for row in films])

@app.route('/api/species-count')
def get_species_count():
    conn = get_db_connection()
    species = conn.execute('''
        SELECT species, COUNT(*) as count 
        FROM characters 
        WHERE species IS NOT NULL 
        GROUP BY species 
        ORDER BY count DESC
    ''').fetchall()
    conn.close()
    return jsonify([dict(row) for row in species])

@app.route('/api/battles')
def get_battles():
    conn = get_db_connection()
    battles = conn.execute('SELECT * FROM battles').fetchall()
    conn.close()
    return jsonify([dict(row) for row in battles])

@app.route('/api/timeline')
def get_timeline():
    conn = get_db_connection()
    timeline = conn.execute('SELECT * FROM timeline ORDER BY year').fetchall()
    conn.close()
    return jsonify([dict(row) for row in timeline])

@app.route('/api/character-lifespans')
def get_character_lifespans():
    conn = get_db_connection()
    characters = conn.execute('''
        SELECT name, year_born, year_died, species, homeworld
        FROM characters 
        WHERE year_born IS NOT NULL
        ORDER BY year_born
    ''').fetchall()
    conn.close()
    return jsonify([dict(row) for row in characters])

@app.route('/api/battle-timeline')
def get_battle_timeline():
    conn = get_db_connection()
    battles = conn.execute('''
        SELECT name, location, date, result, participants
        FROM battles
        ORDER BY date
    ''').fetchall()
    conn.close()
    return jsonify([dict(row) for row in battles])

@app.route('/api/population-centers')
def get_population_centers():
    conn = get_db_connection()
    planets = conn.execute('''
        SELECT p.name, p.population, p.diameter, p.climate, p.terrain,
               CASE WHEN b.location IS NOT NULL THEN 1 ELSE 0 END as had_battle
        FROM planets p
        LEFT JOIN battles b ON p.name = b.location
        WHERE p.population > 0
        ORDER BY p.population DESC
    ''').fetchall()
    conn.close()
    return jsonify([dict(row) for row in planets])

@app.route('/api/species-survival')
def get_species_survival():
    conn = get_db_connection()
    species_data = conn.execute('''
        SELECT 
            species,
            COUNT(*) as total_count,
            COUNT(CASE WHEN year_died IS NOT NULL THEN 1 END) as died_count,
            ROUND(COUNT(CASE WHEN year_died IS NOT NULL THEN 1 END) * 100.0 / COUNT(*), 1) as mortality_rate
        FROM characters 
        WHERE species IS NOT NULL
        GROUP BY species
        HAVING COUNT(*) > 1
        ORDER BY mortality_rate DESC
    ''').fetchall()
    conn.close()
    return jsonify([dict(row) for row in species_data])

if __name__ == '__main__':
    app.run(debug=True)