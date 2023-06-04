import os
import time
from random import randint
from livingthings import Fish
from livingthings import Shark

simulate = True
fish_population = 0
shark_population = 0
planet_width = 10
planet_height = 20
planet_map = { (x, y): "." for x in range(planet_width) for y in range(planet_height)} # Create a dictionnary filled with dots
#planet_map = [["."] * 10] * 10 # Create an empty 2 by 2 array matrix
empty_cells = []
fishs_list = []
sharks_list = []
refresh_delay = 0.5

def generate_ecosystem() -> None :
    """Create sharks and fishs at the beginning of the simulation"""
    # Advice : Create fishs on 1/3 of the map and a shark population equal to 1/3 of the fishs one
    # Generate fishs and sharks to a random position. I must use an array which list every empty cell.
    #global empty_cells
    global planet_map
    global planet_width
    global planet_height
    #empty_cells = planet_map.copy()

    dictionnayLength = len(planet_map)
    fish_number = dictionnayLength // 3
    shark_number = fish_number // 3
    #print(f"Line : {vertical_size} and columns : {horizontal_size}")

    while fish_number > 0 :
        randomLine = randint(0, planet_width -1)
        randomColumn = randint(0, planet_height - 1)

        if planet_map[randomLine, randomColumn] == "." :
            fish_number -= 1
            planet_map[randomLine, randomColumn] = "p"
        

    """
    vertical_size = len(planet_map)
    horizontal_size =  len(planet_map[0])

    while fish_number > 0 :
        randomLine = randint(0, vertical_size-1)
        randomColumn = randint(0, horizontal_size-1)
        
        if planet_map[randomLine][randomColumn] == "." :
            fish_number -= 1
            planet_map[randomLine][randomColumn] = "p"
        
        print(fish_number)"""

def show_map() -> None :
    """Show the current situation of the planet, called each frame"""
    """for x in planet_map :
        print("|", end = "")
        for y in x :
            if(y == "."):
                print(".", end=" ")
            else:
                print(y, end=" ")
        print("|")"""
    global planet_map
    global planet_width
    global planet_height
    
    for x in range(planet_width) :
        print("|", end = "")
        for y in range(planet_height) :
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

    time.sleep(0.5)
    os.system("clear") #for linux and "cls" for windows