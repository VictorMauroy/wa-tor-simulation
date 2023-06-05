class Fish :

    APPEARANCE = "p"

    def __init__(self) -> None:
        self.position:tuple
        self.timeBfrReproduction = 5
# region Movement
    def can_move(self) -> None:
        """_summary_"""
    
    def move(self) -> None:
        """_summary_"""
#endregion
    def reproduction(self) -> None :
        """_summary_"""

    # Update is called at each frame
    def update(self) -> None :
        """Determine next action at each frame depending of
        the current fish state and its surrounding"""
        # Check if movement is possible, if yes : has reproduction counter
        # reached 0 ? if yes : make a baby when moving, else move only

class Shark (Fish) :

    APPEARANCE = "$"
    MAX_ENERGY = 9
    ENERGY_BY_DISHS = 3

    def __init__(self) -> None:
        super().__init__()
        self.timeBfrReproduction = 7
        self.currentEnergy = 5
    
#region Determine if movement is possible and move if yes
    def can_move(self) -> None:
        """_summary_"""
        return super().can_move()
    
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