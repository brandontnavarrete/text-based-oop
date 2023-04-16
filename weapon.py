import random

############### WEAPON ###############
class Weapon:
  
    """
    A base class representing a weapon.
    """
    # Start out with name, strength, durability, weapon_type
    def __init__(self, name, strength, durability, weapon_type, range):
        """
        Initialize a new weapon with the given name, strength, durability, type, and range.
        """
        # naming convention
        self.name = name
      
        # damage capability
        self.strength = strength
      
        # how long the weapon can last
        self.durability = durability
      
        # class of weapons [Projectile, Striker, Blade, Explosive]
        self.weapon_type = weapon_type
        
        # range of the weapon
        self.range = range

    def __str__(self):
        """
        Return a string representation of the weapon.
        """
        return f"{self.name} ({self.weapon_type}, {self.strength} strength, {self.durability} durability, {self.range} range)"

    def use_weapon(self):
        # check weapon durability
        if self.durability > 0:
            # if yes, subtract one for use, and return the damage counter
            self.durability -= 1
            return self.strength
        else:
            # If it doesn't, return 0 (the weapon is broken) 
            return 0


############### PROJECTILE ###############

class Projectile(Weapon):
  
    """
    A subclass of Weapon representing a projectile weapon.
    """
  
    def __init__(self, name):
        """
        Initialize a new projectile weapon with the given name.
        """
      
        super().__init__(name, strength=random.randint(5, 15), durability=random.randint(50, 100), weapon_type='projectile', range=random.randint(10, 50))


class Striker(Weapon):
    """
    A subclass of Weapon representing a striker weapon.
    """
    def __init__(self, name):
        """
        Initialize a new striker weapon with the given name.
        """
        super().__init__(name, strength=random.randint(10, 20), durability=random.randint(30, 80), weapon_type='striker', range=random.randint(5, 30))

class Explosive(Weapon):
    """
    A subclass of Weapon representing an explosive weapon.
    """
    def __init__(self, name):
        """
        Initialize a new explosive weapon with the given name.
        """
        super().__init__(name, strength=random.randint(20, 40), durability=random.randint(10, 50), weapon_type='explosive', range=random.randint(5, 30))

class Blade(Weapon):
    """
    A subclass of Weapon representing a bladed weapon.
    """
    def __init__(self, name):
        """
        Initialize a new bladed weapon with the given name.
        """
        super().__init__(name, strength=random.randint(15, 30), durability=random.randint(20, 60), weapon_type='blade', range=random.randint(1, 10))

