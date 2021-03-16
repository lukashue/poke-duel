import json 
import sys

moves = { 
    'scratch': {
        'type'          : 'normal',
        'power'         :  40,
        'accuracy'      :  1,
        'category'      :  'physical',
        'pp'            :  35,
        'crit_level'    :  1,
        'priority'      :  0
    },
    'tackle': {
        'type'          : 'normal',
        'power'         :  40,
        'accuracy'      :  1,
        'category'      :  'physical',
        'pp'            :  35,
        'crit_level'    :  1,
        'priority'      :  0
    },
    'ember': {
        'type'          : 'fire',
        'power'         :  40,
        'accuracy'      :  1,
        'category'      :  'special',
        'pp'            :  25,
        'crit_level'    :  1,
        'priority'      :  0
    },
    'water_gun': {
        'type'          : 'water',
        'power'         :  40,
        'accuracy'      :  1,
        'category'      :  'special',
        'pp'            :  25,
        'crit_level'    :  1,
        'priority'      :  0
    },
    'vine_whip': {
        'type'          : 'grass',
        'power'         :  45,
        'accuracy'      :  1,
        'category'      :  'physical',
        'pp'            :  25,
        'crit_level'    :  1,
        'priority'      :  0
    },
}

with open(f'{sys.path[0]}/moves.json', "w") as file:
  json.dump(moves, file, indent=2)