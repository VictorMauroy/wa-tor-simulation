import os
import time
from random import randint
from livingthings import Fish
from livingthings import Shark

simulate = True
fish_population = 0
shark_population = 0
PLANET_WIDTH = 10
PLANET_HEIGHT = 20
REFRESH_DELAY = 0.5

# Create a dictionnary filled with dots
planet_map = { (x, y): "." for x in range(PLANET_WIDTH) for y in range(PLANET_HEIGHT)} 
fishs_list = []
sharks_list = []

def generate_ecosystem() -> None :
    """Create sharks and fishs at random position, at the beginning of the simulation"""
    # Advice : Create fishs on 1/3 of the map and a shark population equal to 1/3 of the fishs one
    # Generate fishs and sharks to a random position.
    global planet_map
    PLANET_WIDTH
    PLANET_HEIGHT
    global shark_population
    global fish_population

    dictionnayLength = len(planet_map)
    fish_population = fish_number = dictionnayLength // 3
    shark_population = shark_number = fish_number // 3

    while fish_number > 0 :
        randomLine = randint(0, PLANET_WIDTH -1)
        randomColumn = randint(0, PLANET_HEIGHT - 1)

        if planet_map[randomLine, randomColumn] == "." :
            fish_number -= 1
            planet_map[randomLine, randomColumn] = "p"    

def show_map() -> None :
    """Show the current situation of the planet, called each frame"""
    global planet_map
    PLANET_WIDTH
    PLANET_HEIGHT
    
    for x in range(PLANET_WIDTH) :
        print("|", end = "")
        for y in range(PLANET_HEIGHT) :
            if(planet_map[x,y]) == "." :
                print(".", end=" ")
            else:
                print(planet_map[x,y], end=" ")
        print("|")

generate_ecosystem()

while(simulate) :

    show_map()

    """for fish in fishs_list :  #Bien penser à assigner le type Fish
        fish.Update()
    for shark in sharks_list :
        shark.Update()"""

    time.sleep(REFRESH_DELAY)
    os.system("clear") #for linux and "cls" for windows