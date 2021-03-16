import sys
sys.path.append('.')
from pokemon import Pokemon

class Team():
  def __init__(self):
    self.setup = [None, None, None, None, None, None]     # maybe replace None with a K.O´d blank Pokemon
  
  def add(self, pkmn):
    try:
      pos = self.setup.index(None)
      self.setup[pos] = pkmn
    except ValueError:
      print("Team is full")
    # later set else condition to custom exception (or something else)

  def delete(self, index):
    self.setup[index] = None

if __name__=="__main__":
  team = Team()
  cha = Pokemon("Charmander")
  squ = Pokemon("Squirtle")
  team.add(cha)
  team.add(cha)
  team.add(cha)
  team.add(cha)
  team.add(cha)
  team.add(cha)
  team.add(squ)
  team.delete(0)
  print(team.setup, team.setup[1].name)