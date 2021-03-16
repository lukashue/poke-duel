import json
import sys

# This script serves as a generator for the corresponding JSON file
# I use it because some huge changes in the JSON file can be easily generated in here
# If you want to edit the natures, change them here and run the script.

nature_coefficients = {
  "hardy": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 1},
  "lonely": {'hp': 1, 'atk': 1.1, 'def': 0.9, 'spa': 1, 'spd': 1, 'spe': 1},
  "brave": {'hp': 1, 'atk': 1.1, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 0.9},
  "adamant": {'hp': 1, 'atk': 1.1, 'def': 1, 'spa': 0.9, 'spd': 1, 'spe': 1},
  "naughty": {'hp': 1, 'atk': 1.1, 'def': 1, 'spa': 1, 'spd': 0.9, 'spe': 1},
  "bold": {'hp': 1, 'atk': 0.9, 'def': 1.1, 'spa': 1, 'spd': 1, 'spe': 1},
  "docile": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 1},
  "relaxed": {'hp': 1, 'atk': 1, 'def': 1.1, 'spa': 1, 'spd': 1, 'spe': 0.9},
  "impish": {'hp': 1, 'atk': 1, 'def': 1.1, 'spa': 0.9, 'spd': 1, 'spe': 1},
  "lax": {'hp': 1, 'atk': 1, 'def': 1.1, 'spa': 1, 'spd': 0.9, 'spe': 1},
  "timid": {'hp': 1, 'atk': 0.9, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 1.1},
  "hasty": {'hp': 1, 'atk': 1, 'def': 0.9, 'spa': 1, 'spd': 1, 'spe': 1.1},
  "serious": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 1},
  "jolly": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 0.9, 'spd': 1, 'spe': 1.1},
  "naive": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1, 'spd': 0.9, 'spe': 1.1},
  "modest": {'hp': 1, 'atk': 0.9, 'def': 1, 'spa': 1.1, 'spd': 1, 'spe': 1},
  "mild": {'hp': 1, 'atk': 1, 'def': 0.9, 'spa': 1.1, 'spd': 1, 'spe': 1},
  "quiet": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1.1, 'spd': 1, 'spe': 0.9},
  "bashful": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 1},
  "rash": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1.1, 'spd': 0.9, 'spe': 1},
  "calm": {'hp': 1, 'atk': 0.9, 'def': 1, 'spa': 1, 'spd': 1.1, 'spe': 1},
  "gentle": {'hp': 1, 'atk': 1, 'def': 0.9, 'spa': 1, 'spd': 1.1, 'spe': 1},
  "sassy": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1, 'spd': 1.1, 'spe': 0.9},
  "careful": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 0.9, 'spd': 1.1, 'spe': 1},
  "quirky": {'hp': 1, 'atk': 1, 'def': 1, 'spa': 1, 'spd': 1, 'spe': 1}
}

with open(f'{sys.path[0]}/natures.json', "w") as file:
  json.dump(nature_coefficients, file, indent=2)

