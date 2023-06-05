from random import randint

class Fish :

    APPEARANCE = "p"

    def __init__(self) -> None:
        self.position:tuple
        self.timeBfrReproduction = 5
# region Movement
    def get_free_position(self, line:int, column:int, available_pos_list:list) -> None : 
        """Check if a cell is occupied at the given line and column given 
        and add it to the list of available positions.

        Note: if the given position exceed the planet borders, 
        find the correct position"""
        from simulation import PLANET_WIDTH
        from simulation import PLANET_HEIGHT
        from simulation import planet_map
        # Fix the coordonates if the position exceed the limits
        """if line < 0 : line = PLANET_WIDTH - 1
        if line >= PLANET_WIDTH : line = 0
        if column < 0 : column = PLANET_HEIGHT
        if column >= PLANET_HEIGHT : column = 0"""
        # Code below is the same as above
        line = line % PLANET_WIDTH
        column = column % PLANET_HEIGHT

        if not isinstance(planet_map[line, column], Fish) : 
            available_pos_list.append((line, column))
        #return available_pos_list

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
    # Q : Demander si on peut se passer de l'assignation car les listes sont liées ?
    # (Pas besoin de list.copy)

    def move(self, available_positions:list) -> None:
        """If an adjacent position is available, move to it, else stay at our current position"""
        from simulation import planet_map
        
        if len(available_positions) > 0 :
            # nextPosition = Tuple
            nextPosition = available_positions[randint(0, len(available_positions)-1)] 
            old_x, old_y = self.position
            planet_map[old_x, old_y] = "." # Modify here for reproduction
            self.position = nextPosition
            planet_map[self.position] = self

#endregion
    def reproduction(self) -> None :
        """_summary_"""

    # Update is called at each frame
    def update(self) -> None :
        """Determine next action at each frame depending of
        the current fish state and its surrounding"""
        # Check if movement is possible, if yes : has reproduction counter
        # reached 0 ? if yes : make a baby when moving, else move only
        
        self.move(self.search_available_positions())


class Shark (Fish) :

    APPEARANCE = "$"
    MAX_ENERGY = 9
    ENERGY_BY_DISHS = 3

    def __init__(self) -> None:
        super().__init__()
        self.timeBfrReproduction = 7
        self.currentEnergy = 5
    
#region Determine if movement is possible and move if yes
    def search_available_positions(self) -> None:
        """_summary_"""
        return super().search_available_positions()
    
    def move(self) -> None:
        """_summary_"""
        return super().move()
#endregion
    
#region Find fish and eat it
    def find_fish() -> None:
        """_summary_"""

    def eat_fish(self) -> None:
        """_summary_"""
#endregion
    
    def reproduction(self) -> None:
        """_summary_"""
        return super().reproduction()
    
    def update(self) -> None:
        """Determine next action at each frame depending of
        the current shark state and its surrounding"""
        # When its turn begins : First, search fish in adjacent cells (Find Fish) 
        # if finded, eat them by moving to their cell (Eat Fish), else try to move
        # to a random location, adjacent cell (CanMove). If yes :
        # If reproduction counter has reached 0 => make a baby when moving, move only.
        # Special : movement cost one energy, if energy has reached 0 : die and delete shark