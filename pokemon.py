import math
import json

# imports the base stats of all implemented pokemon
with open('base_stats.json') as base_stats_file:
  base_stats = json.loads(base_stats_file.read())

# Creating an instance of this class will create an error because I didn´t define base stats for an arbitrary pokemon
# This class only serves as a template for its child classes
class Pokemon():
  def __init__(self):
    self.name = self.__class__.__name__ 
    self.lvl = 5
    self.type = [None, None]
    self.base = base_stats[self.__class__.__name__]
    self.IV = {
      'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0, 
    }
    self.EV = {
      'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0, 
    }
    
  def max(self, stat):
    if stat=='hp':
      return math.floor(0.01*(2*self.base['hp'] + self.IV['hp'] + math.floor(0.25*self.EV['hp']))*self.lvl) + self.lvl + 10
    else:
      return math.floor(0.01*(2*self.base[stat] + self.IV[stat] + math.floor(0.25*self.EV[stat]))*self.lvl) + 5 
      # need to multiply with nature coefficient once implemented


class Charmander(Pokemon):
  def __init__(self):
    super().__init__()

class Squirtle(Pokemon):
  def __init__(self):
    super().__init__()


# For testing:
cha = Charmander()
squ = Squirtle()
print("At level 5, with zero IV/EV and neutral nature, the stats are:")
for poke in [cha, squ]:
  print(f'{poke.name}:')
  for stat in ["hp","atk","def","spa","spd","spe"]:
    print(stat, poke.max(stat), end="\t")
  print()


