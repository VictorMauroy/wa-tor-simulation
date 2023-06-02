class Fish :

    appearance = "p"

    def __init__(self) -> None:
        self.position = "To determine"
        self.timeBfrReproduction = 5
# region Movement
    def CanMove(self) -> None:
        """_summary_"""
    
    def Move(self) -> None:
        """_summary_"""
#endregion
    def Reproduction(self) -> None :
        """_summary_"""

    # Update is called at each frame
    def Update(self) -> None :
        """Determine next action at each frame depending of
        the current fish state and its surrounding"""
        # Check if movement is possible, if yes : has reproduction counter
        # reached 0 ? if yes : make a baby when moving, else move only

class Shark (Fish) :

    appearance = "$"
    maxEnergy = 9
    energyByDish = 3

    def __init__(self) -> None:
        super().__init__()
        self.timeBfrReproduction = 7
        self.currentEnergy = 5
    
#region Determine if movement is possible and move if yes
    def CanMove(self) -> None:
        """_summary_"""
        return super().CanMove()
    
    def Move(self) -> None:
        """_summary_"""
        return super().Move()
#endregion
    
#region Find fish and eat it
    def FindFish() -> None:
        """_summary_"""

    def Eat_Fish(self) -> None:
        """_summary_"""
#endregion
    
    def Reproduction(self) -> None:
        """_summary_"""
        return super().Reproduction()
    
    def Update(self) -> None:
        """Determine next action at each frame depending of
        the current shark state and its surrounding"""
        # When its turn begins : First, search fish in adjacent cells (Find Fish) 
        # if finded, eat them by moving to their cell (Eat Fish), else try to move
        # to a random location, adjacent cell (CanMove). If yes :
        # If reproduction counter has reached 0 => make a baby when moving, move only.
        # Special : movement cost one energy, if energy has reached 0 : die and delete shark