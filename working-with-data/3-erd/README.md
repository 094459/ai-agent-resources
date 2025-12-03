# Star Wars Data Explorer

A simple Python web application for navigating Star Wars database with D3.js visualizations.

## Features

- **Species Distribution**: Bar chart showing character count by species
- **Character Network**: Interactive network graph grouping characters by homeworld
- **Planet Data**: Scatter plot of planet population vs diameter
- **Species Donut**: Donut chart showing species distribution
- **Battles**: Battle outcomes visualization
- **Timeline**: Major events in Star Wars chronology

## Setup

1. Install dependencies:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser to `http://localhost:5000`

## Usage

Click the buttons to switch between different visualizations:
- Species Distribution: Shows which species have the most characters
- Character Network: Interactive network showing character relationships by homeworld
- Planet Data: Scatter plot comparing planet size and population
- Species Donut: Donut chart of character species distribution
- Battles: Major battles with color-coded outcomes
- Timeline: Chronological events in Star Wars history

The visualizations are interactive - hover over elements for details and drag nodes in the network view.