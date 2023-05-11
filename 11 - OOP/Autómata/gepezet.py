from udito import *
from os import system

class Automata:
    def __init__(self, coke:Udito, fanta:Udito, sprite:Udito, pepsi:Udito, siobarack:Udito):
        super().__init__()
        self.coke:Udito=coke
        self.fanta:Udito=fanta
        self.sprite:Udito=sprite
        self.pepsi:Udito=pepsi
        self.siobarack:Udito=siobarack

    def __str__(self) -> str:
        return f"{self.coke}\n{self.fanta}\n{self.sprite}\n{self.pepsi}\n{self.siobarack}"
    

        