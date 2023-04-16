import time
import player
import insect
import weapon

from user_interface import print_slow, loading_screen

### Print opening title

###### DIALOGUE ######
print_slow('Welcome to Bug Bed Battles!')
time.sleep(1)

print_slow('As a toy soldier, your mission is to protect your child from the hordes of bugs that come out at night.')
time.sleep(2)

print_slow('During the day, you have time to complete tasks such as farming, crafting weapons, exploring and talking to friendlies.')
time.sleep(3)

print_slow('Your goal is to advance your territory and destroy the nest as fast as possible. If you want a promotion anytime soon, keep track of your time and score')
time.sleep(2)

print_slow('Let the battle begin!')
###### DIALOGUE ######


# ask player for their name
name = input('What is your name, soldier? ')
time.sleep(1)
print_slow(f"Welcome to the battle, {name}!")

# create player object
advent = player.Player(name, 0, 100)

# display player score and health
advent.display_score()
advent.display_start_health()

loading_screen()

print('Second in Command:')

print_slow("Sir, we are ready to dismount the bed")
print_slow('There are three types of soldiers: riflemen, snipers, and grenadiers.')
print_slow('Each type has its own strengths and weaknesses, so choose wisely.')
print_slow('You also notice a few objects lying around the room that might be useful.')

