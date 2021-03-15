import math
import json

# imports the base stats of all implemented pokemon
with open('base_stats.json') as base_stats_file:
  base_stats = json.loads(base_stats_file.read())

# imports the nature coefficients
with open('natures.json') as nature_file:
  nature_coeffs = json.loads(nature_file.read())

# Creating an instance of this class will create an error because I didn´t define base stats for an arbitrary pokemon
# This class only serves as a template for its child classes
class Pokemon():
  def __init__(self):
    self.name = self.__class__.__name__ 
    self.nickname = self.__class__.__name__ 
    self.type = [None, None]
    self.lvl = 5
    self.base = base_stats[self.__class__.__name__]
    self.IV = {
      'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0, 
    }
    self.EV = {
      'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0, 
    }
    self.nature = "hardy"   # may be randomized later
    
  def max(self, stat):
    if stat=='hp':
      return math.floor(0.01*(2*self.base['hp'] + self.IV['hp'] + math.floor(0.25*self.EV['hp']))*self.lvl) + self.lvl + 10
    else:
      return math.floor(math.floor((0.01*(2*self.base[stat] + self.IV[stat] + math.floor(0.25*self.EV[stat]))*self.lvl) + 5)*nature_coeffs[self.nature][stat])
      # need to multiply with nature coefficient once implemented


class Charmander(Pokemon):
  def __init__(self):
    super().__init__()

class Squirtle(Pokemon):
  def __init__(self):
    super().__init__()

# ------------TEST AREA-----------------

cha = Charmander()
squ = Squirtle()
print("At level 100, with zero IV/EV and neutral nature, the stats are:")
for poke in [cha, squ]:
  print(f'{poke.name}:')
  poke.lvl = 100
  for stat in ["hp","atk","def","spa","spd","spe"]:
    print(stat, poke.max(stat), end="\t")
  print()

print('For Comparison:')
squ.nature = "lonely"
print('Squirtle (with lonely nature):')
for stat in ["hp","atk","def","spa","spd","spe"]:
    print(stat, squ.max(stat), end="\t")

