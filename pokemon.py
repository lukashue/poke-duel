import math

class Pokemon():
  def __init__(self):
    self.lvl = 5
    self.base = {
      'hp': 39, 'atk': 52, 'def': 43, 'spa': 60, 'spd': 50, 'spe': 65, 
    }
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

poke = Pokemon()
print(poke.max('hp'))
print(poke.max('atk'))
print(poke.max('def'))
print(poke.max('spa'))
print(poke.max('spd'))
print(poke.max('spe'))
