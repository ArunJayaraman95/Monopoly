from player import Player

class Board:
    def __init__(self) -> None:
        self.colorGroups = []
        self.chanceList = []
        self.communityChestList = []

    def pay(self, payer: Player, payee: Player, amount: int) -> None:
        payer.lose(amount)
        payee.gain(amount)