from random import randint

class Fish :

    APPEARANCE = "\033[96mp\033[00m" # Char 'p' with cyan color
    TIME_BTW_REPRODUCTIONS = 3

    def __init__(self) -> None:
        self.position:tuple
        self.timeBfrReproduction = Fish.TIME_BTW_REPRODUCTIONS

#region Movement
    def get_free_position(self, line:int, column:int, available_pos_list:list) -> None : 
        """Check if a cell is occupied at the given line and column given 
        and add it to the list of available positions.

        Note: if the given position exceed the planet borders, 
        find the correct position"""
        from simulation import PLANET_WIDTH
        from simulation import PLANET_HEIGHT
        from simulation import planet_map

        # Fix the coordonates if the position exceed the limits
        line = line % PLANET_WIDTH
        column = column % PLANET_HEIGHT

        if not isinstance(planet_map[line, column], Fish) :
            available_pos_list.append((line, column))

    def search_available_positions(self) -> list:
        """Search for available positions in the adjacents cases
        and return a list of tuples which contains them"""
        available_positions = []
        x, y = self.position
        # Ci-dessous : Pas besoin de récupérer la liste, celle-ci est référencée et reste connectée 
        # à travers la fonction (on l'a assignée dans les paramètres). 
        # La mettre à jour va donc aussi avoir effet ici 
        self.get_free_position(x, y + 1, available_positions)
        self.get_free_position(x, y - 1, available_positions)
        self.get_free_position(x + 1, y, available_positions)
        self.get_free_position(x - 1, y, available_positions)
        return available_positions

    def move(self, available_positions:list) -> bool:
        """If an adjacent position is available, move to it, else stay at our current position"""
        from simulation import planet_map

        if len(available_positions) > 0 :
            # nextPosition is a Tuple
            nextPosition = available_positions[randint(0, len(available_positions)-1)]
            
            # If gestation ends, create a new fish at our old position. Else live an empty cell
            old_x, old_y = self.position
            self.timeBfrReproduction -= 1
            if self.timeBfrReproduction <= 0 :
                self.reproduction(old_x, old_y)
            else :
                planet_map[old_x, old_y] = "."
            
            self.position = nextPosition
            planet_map[self.position] = self
            return True
        else :
            return False

#endregion

    def reproduction(self, old_x, old_y) -> None :
        """Create a new fish at our old position and initialize it"""
        from simulation import planet_map
        from simulation import fishs_list

        babyFish = Fish()
        planet_map[old_x, old_y] = babyFish
        babyFish.position = (old_x, old_y)
        fishs_list.append(babyFish)
        
        self.timeBfrReproduction = Fish.TIME_BTW_REPRODUCTIONS

    # Update is called at each refresh
    def update(self) -> None :
        """Determine next action at each frame depending of
        the current fish state and its surrounding"""
        # Check if movement is possible, if yes : has reproduction counter
        # reached 0 ? if yes : make a baby when moving, else move only
        
        self.move(self.search_available_positions())


class Shark (Fish) :

    APPEARANCE = "\033[91m$\033[00m" # Char '$' with red color
    MAX_ENERGY = 10
    ENERGY_BY_DISHS = 1
    TIME_BTW_REPRODUCTIONS = 7

    def __init__(self) -> None:
        self.position:tuple
        self.timeBfrReproduction = Shark.TIME_BTW_REPRODUCTIONS
        self.currentEnergy = 4
    
#region Determine if movement is possible and move if yes
    def search_available_positions(self) -> None:
        return super().search_available_positions()
    
    def move(self, available_positions:list) -> None:
        if super().move(available_positions) :
            self.currentEnergy -= 1
                
#endregion
    
#region Find fish and eat it
    def try_fish_position(self, line:int, column:int, fish_pos_list:list):
        """Check a given cell position and add it to the given list if there is a fish"""
        from simulation import PLANET_WIDTH
        from simulation import PLANET_HEIGHT
        from simulation import planet_map
        # Fix the coordonates if the position exceed the limits
        line = line % PLANET_WIDTH
        column = column % PLANET_HEIGHT
        if isinstance(planet_map[line, column], Fish) and not isinstance(planet_map[line, column], Shark) :
            fish_pos_list.append((line, column))
    
    def find_fish(self) -> list[tuple] :
        """Looks at adjacent cells for fishs and return their positions if finded"""
        fish_positions = []
        x, y = self.position
        # Ci-dessous : Pas besoin de récupérer la liste, celle-ci est référencée et reste connectée 
        # à travers la fonction (on l'a assignée dans les paramètres). 
        # La mettre à jour va donc aussi avoir effet ici 
        self.try_fish_position(x, y + 1, fish_positions)
        self.try_fish_position(x, y - 1, fish_positions)
        self.try_fish_position(x + 1, y, fish_positions)
        self.try_fish_position(x - 1, y, fish_positions)
        return fish_positions

    def eat_fish(self, fish_positions:list[tuple]) -> bool:
        """If fishs were finded at adjacent cases, then eat it

        Args:
            fish_positions (list[tuple]): List of fish positions. Can be empty

        Returns:
            bool: Wether a fish has been it or not
        """
        from simulation import planet_map
        from simulation import fishs_list
        from simulation import sharks_list
               
        if len(fish_positions) > 0 :
            # nextPosition is a Tuple
            nextPosition = fish_positions[randint(0, len(fish_positions)-1)]
            
            # If gestation ends, create a new fish at our old position. Else live an empty cell
            old_x, old_y = self.position
            dead_fish = planet_map[nextPosition]
            fishs_list.remove(dead_fish)
            
            
            self.position = nextPosition
            planet_map[self.position] = self
            
            self.timeBfrReproduction -= 1
            if self.timeBfrReproduction <= 0 :
                self.reproduction(old_x, old_y)
            else :
                planet_map[old_x, old_y] = "."
            
            if self.currentEnergy + self.ENERGY_BY_DISHS > self.MAX_ENERGY :
                self.currentEnergy = self.MAX_ENERGY 
            else :
                self.currentEnergy += self.ENERGY_BY_DISHS
            
            return True
        else :
            return False
#endregion
    
    def reproduction(self, old_x, old_y) -> None:
        """Create a new shark at our old position and initialize it"""
        from simulation import planet_map
        from simulation import sharks_list

        babyShark = Shark()
        planet_map[old_x, old_y] = babyShark
        babyShark.position = (old_x, old_y)
        sharks_list.append(babyShark)
        
        self.timeBfrReproduction = Shark.TIME_BTW_REPRODUCTIONS
    
    def update(self) -> None:
        """Determine next action at each frame depending of
        the current shark state and its surrounding"""
        # When its turn begins : First, search fish in adjacent cells (Find Fish) 
        # if finded, eat them by moving to their cell (Eat Fish), else try to move
        # to a random location, adjacent cell (CanMove). If yes :
        # If reproduction counter has reached 0 => make a baby when moving, move only.
        # Special : movement cost one energy, if energy has reached 0 : die and delete shark
        from simulation import planet_map
        from simulation import sharks_list

        # First : try to eat a fish by checking adjcacents cases
        if not self.eat_fish(self.find_fish()) : 
            # Then, if no fishs were finded, try to move
            self.move(self.search_available_positions())

        if self.currentEnergy <= 0 :
            planet_map[self.position] = "."
            sharks_list.remove(self)
