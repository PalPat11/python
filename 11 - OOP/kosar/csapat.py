from player import *
from os import system

class Team:
    def __init__(self, player1:Player, player2:Player, player3:Player, player4:Player, player5:Player, ):
        super().__init__()
        self.player1:Player=player1
        self.player2:Player=player2
        self.player3:Player=player3
        self.player4:Player=player4
        self.player5:Player=player5

    def __str__(self) -> str:
        return f"Csapattagok:\n {self.player1}\n {self.player2}\n {self.player3}\n {self.player4}\n {self.player5}"