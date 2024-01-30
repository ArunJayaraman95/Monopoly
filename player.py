class Player:
    def __init__(self) -> None:
        self.money: int = 0
        self.properties = []
        self.boardPosition = None
        self.jailed: bool = False


    def gain(self, amount) -> None:
        self.money += amount

    def lose(self, amount) -> None:
        self.money -= amount

