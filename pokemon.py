import math
import json
import sys

# imports the base stats of all implemented pokemon
with open(f'{sys.path[0]}/data/pkmnData.json') as pkmnData_file:
  pkmnData = json.loads(pkmnData_file.read())

# imports the nature coefficients
with open(f'{sys.path[0]}/data/natures.json') as nature_file:
  nature_coeffs = json.loads(nature_file.read())

# imports the moves
with open(f'{sys.path[0]}/data/moves.json') as moves_file:
  moves = json.loads(moves_file.read())


class Pokemon():
  def __init__(self, species):
    self.name = species.capitalize()
    self.nickname = species.capitalize() 
    species = species.lower()
    self.type = pkmnData[species]["type"]
    self.lvl = 5
    self.base = pkmnData[species]["base_stats"]
    self.IV = {
      'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0, 
    }
    self.EV = {
      'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0, 
    }
    self.nature = "hardy"   # may be randomized later
    #self.item = None
    self.moves = [None, None, None, None]
    
  def max(self, stat):
    if stat=='hp':
      return math.floor(0.01*(2*self.base['hp'] + self.IV['hp'] + math.floor(0.25*self.EV['hp']))*self.lvl) + self.lvl + 10
    else:
      return math.floor(math.floor((0.01*(2*self.base[stat] + self.IV[stat] + math.floor(0.25*self.EV[stat]))*self.lvl) + 5)*nature_coeffs[self.nature][stat])

  def can_learn_move(self, move):
    return move in pkmnData[self.name.lower()]["learnset"] and self.lvl >= pkmnData[self.name.lower()]["learnset"][move]

  # Replace terminal interaction later
  def learn(self, move):
    if self.can_learn_move(move):
      if move in self.moves:
        print(f"{self.nickname} already knows this move.")
      elif None in self.moves:
        pos = self.moves.index(None)
        self.moves[pos] = move
      else:
        pos = input("Choose which move you want to replace (0-3):")   
        self.moves[int(pos)] = move
    else:
      print(f"{self.nickname} cannot learn this move.")


# ------------TEST AREA-----------------
if __name__=="__main__":
  cha = Pokemon("charmAnder")
  squ = Pokemon("Squirtle")
  bul = Pokemon("Bulbasaur")
  print("At level 100, with zero IV/EV and neutral nature, the stats are:")
  for poke in [cha, squ, bul]:
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

  print()
  cha.learn("ember")
  cha.learn("vine_whip")
  print(cha.moves)




