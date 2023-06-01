class Fish :

    appearance = "p"

    def __init__(self) -> None:
        self.position = "To determine"
        self.timeBfrReproduction = 5
    
    def CanMove(self) -> None:
        """_summary_"""
    
    def Move(self) -> None:
        """_summary_"""

    def Reproduction(self) -> None :
        """_summary_"""

    # Update is called at each frame
    def Update(self) -> None :
        """Determine next action at each frame depending of
        the current fish state and its surrounding"""

class Shark (Fish) :

    appearance = "$"
    maxEnergy = 9
    energyByDish = 3

    def __init__(self) -> None:
        super().__init__()
        self.timeBfrReproduction = 7
        self.currentEnergy = 5
    
#region Determine if movement is possible and move if yes
    def Move(self) -> None:
        """_summary_"""
        return super().Move()
    
    def CanMove(self) -> None:
        """_summary_"""
        return super().CanMove()
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
        