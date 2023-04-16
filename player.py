class Player:
  def __init__(self, name, score, health , weapon = None):
    self.name = name
    self.score = score
    self.health = health
    self.weapon = weapon
    self.weapons = [weapon]

  ################## SElF ##################
  def display_self(self):
    print(f'{self.name }, {self.score}, {self.health},{self.weapon},{self.weapons}')

  
  def display_score(self):
        print(f"{self.name}'s score is     {self.score}.")

  def display_start_health(self):
        print(f"{self.name}'s starting health is    {self.health}.")

  ################## WEAPON ##################
  
  def weapon_status(self):
        print(f" You're holding a {self.weapon}")

  def get_weapons(self):
    return self.weapons
   ################## WEAPON ##################



