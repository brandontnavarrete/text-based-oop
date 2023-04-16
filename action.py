import random
import weapon

import insect
from insect import select_insect

import player
import user_interface

############### ATTACK ###############

def attack(advent, insects):
    """Function for attacking insects"""
    
    # Get the player's weapons
    weapons = advent.get_weapons()
    
    # Loop until the player selects a valid weapon
    while True:
        # Ask the player to select a weapon
        weapon_name = input('Select a weapon: ').lower()
        selected_weapon = None
        
        # Search for the weapon in the player's inventory
        for weapon in weapons:
            if weapon.name.lower() == weapon_name:
                selected_weapon = weapon
                break
        
        # If the weapon wasn't found, ask the player to try again
        if selected_weapon is None:
            print("You don't have that weapon!")
        else:
            break
    
    # Attack the selected insect with the selected weapon
    insect = select_insect(insects)
    damage = selected_weapon.use_weapon()
    insect.take_damage(damage, selected_weapon.damage_type)
    print(f"You attacked the {insect.name} with your {selected_weapon.name} for {damage} damage!")
 
############### ATTACK ###############


############### TALK  ###############

'''def talk(advent, npc):
    """Function for talking to NPCs"""
    print("Choose an NPC to talk to:")
    for i, npc in enumerate(npcs):
        print(f"{i+1}: {npc.name}")
    choice = int(input()) - 1
    selected_npc = npcs[choice]
    print(f"You talk to {selected_npc.name}.")
    selected_npc.dialogue()'''

############### CRAFT  ###############

'''def craft(advent):
    """Function for crafting weapons"""
    print("Choose a weapon to craft:")
    weapons = advent.get_available_weapons()
    for i, weapon in enumerate(weapons):
        print(f"{i+1}: {weapon.name}")
    choice = int(input()) - 1
    selected_weapon = weapons[choice]
    print(f"You craft a {selected_weapon.name}!")
    advent.add_weapon(selected_weapon)'''

############### EXPLORE  ###############

'''def explore(advent):
    """Function for exploring"""
    print("You explore the surroundings...")
    # generate random events, such as finding a weapon or encountering insects'''

############### FARM  ###############

'''def farm(advent):
    """Function for farming"""
    print("You tend to your crops...")
    # generate resources or other events related to farming
'''
