import json
import sys

# This script serves as a generator for the corresponding JSON file
# I use it because some huge changes in the JSON file can be easily generated in here
# If you want to edit the stats of some Pokemon, change them here and run the script.

pkmnData = {
  "charmander": {
    "base_stats": {
      'hp': 39, 'atk': 52, 'def': 43, 'spa': 60, 'spd': 50, 'spe': 65
    },
    "type": ["fire", None],
    "learnset": {
      'scratch': 1, 'ember': 4 
    }   
  },
  "squirtle": {
    "base_stats": {
      'hp': 44, 'atk': 48, 'def': 65, 'spa': 50, 'spd': 64, 'spe': 43
    },
    "type": ["water", None],
    "learnset": {
      'tackle': 1, 'water_gun': 3
    }   
  },
  "bulbasaur": {
    "base_stats": {
      'hp': 45, 'atk': 49, 'def': 49, 'spa': 65, 'spd': 65, 'spe': 45
    },
    "type": ["grass", "poison"],
    "learnset": {
      'tackle': 1, 'vine_whip': 3
    }   
  }
}

with open(f'{sys.path[0]}/pkmnData.json', "w") as file:
  json.dump(pkmnData, file, indent=2)