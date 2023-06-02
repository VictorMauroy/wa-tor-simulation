import sys
from livingthings import Fish
from livingthings import Shark

fish_population = 0
shark_population = 0
planet_map = [[None] * 50] * 25 # Create an empty 2 by 2 array matrix : 1250 / 3 = 416,66.. 416/3 = 139
refresh_delay = 0.5

def Generate_Ecosystem() -> None :
    """Create sharks and fishs at the beginning of the simulation"""
    # Advice : Create fishs on 1/3 of the map and a shark population equal to 1/3 of the fishs one
    # Generate fishs and sharks to a random position. I must use an array which list every empty cell.

def Show_Map() -> None :
    """Show the current situation of the planet, called each frame"""

