import random

##### INSECT ########################################

class Insect:
  
    """
    A base class representing an insect.
    """

    def __init__(self, name, wings, legs, tone):
        """
        Initialize a new insect with the given name, number of wings, and number of legs.
        """
        
        self.name = name
        self.wings = wings
        self.legs = legs
        self.size = round(random.triangular(1,10,5),1)
        self.health = random.randint(1, 100)
        self.attack = random.randint(1, 100)
        self.tone = random.choice(['negative','neutral','postive'])

    def __str__(self):
      return f"{self.name} ({self.size} cm, {self.health} health, {self.tone} tone)"
      
  
    def describe(self):
        """
        Print a description of this insect.
        """
        print(f"{self.name} has {self.wings} wings and {self.legs} legs.")
        print(f"It is {self.size} in size and has {self.health} health points.")

    
##### INSECT ########################################



##### ANT ########################################

class Ant(Insect):
    """
    A subclass of Insect representing an ant.
    """

    def __init__(self, name):
        """
        Initialize a new ant with the given name.
        """
        super().__init__(name, wings=0, legs=6)

    def describe(self):
        """
        Print a description of this ant.
        """
        print(f"{self.name} is an ant with {self.legs} legs and no wings.")
        print(f"It is {self.size} in size and has {self.health} health points.")


##### BEE ########################################

class Bee(Insect):
    """
    A subclass of Insect representing a bee.
    """

    def __init__(self, name):
        """
        Initialize a new bee with the given name.
        """
        super().__init__(name, wings=4, legs=6)

    def describe(self):
        """
        Print a description of this bee.
        """
        print(f"{self.name} is a bee with {self.legs} legs and {self.wings} wings.")
        print(f"It is {self.size} in size and has {self.health} health points.")


class Butterfly(Insect):
    """
    A subclass of Insect representing a butterfly.
    """

    def __init__(self, name):
        """
        Initialize a new butterfly with the given name.
        """
        super().__init__(name, wings=2, legs=6)

    def describe(self):
        """
        Print a description of this butterfly.
        """
        print(f"{self.name} is a butterfly with {self.legs} legs and {self.wings} wings.")
        print(f"It is {self.size} in size and has {self.health} health points.")

    def describe_tone(self):
        """
        Print the tone of this butterfly.
        """
        if self.tone == 'positive':
            print(f"{self.name}'s tone is positive.")
        elif self.tone == 'negative':
            print(f"{self.name}'s tone is negative.")
        else:
            print(f"{self.name}'s tone is neutral.")

################################
          # FUNCTION
################################


def select_insect(insects):
    """
    Asks the player to select an insect to attack from a list of insects.
    """
    print("Please select an insect:")
    for i, insect in enumerate(insects):
        print(f"{i+1}. {insect.name}")

    # Wait for player input
    selection = None
    while selection is None:
        try:
            selection = int(input("Enter a number: "))
            if selection < 1 or selection > len(insects):
                selection = None
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid selection. Please try again.")
    
    # Return the selected insect
    return insects[selection-1]