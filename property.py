from player import Player

class Property:
    def __init__(self, name, color, rents, mortgageValue) -> None:
        self.name = name
        self.color = color
        self.rent = {
            0:rents[0],
            1:rents[1],
            2:rents[2],
            3:rents[3],
            4:rents[4],
            5:rents[5],
        }
        self.houseCount = 0
        self.mortgageValue = mortgageValue
        self.mortgaged = False
        self.owner:Player = None
        
    def isOwned(self) -> bool:
        return self.owner
    
    def getRent(self) -> int:
        return self.rent[self.houseCount]
    
    def isMortgaged(self) -> bool:
        return self.mortgaged
    
    def mortgage(self) -> None:
        if not self.owner:
            return
        
        if not self.isMortgaged():
            return
        
        self.mortgaged = True
        self.owner.pay()