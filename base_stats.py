import json

# This script serves as a generator for the corresponding JSON file
# I use it because some huge changes in the JSON file can be easily generated in here
# If you want to edit the stats of some Pokemon, change them here and run the script.

base_stats = {
  "Charmander": {
    'hp': 39, 'atk': 52, 'def': 43, 'spa': 60, 'spd': 50, 'spe': 65 
  },
  "Squirtle": {
    'hp': 44, 'atk': 48, 'def': 65, 'spa': 50, 'spd': 64, 'spe': 43
  }
}

with open('base_stats.json', "w") as file:
  json.dump(base_stats, file, indent=2)