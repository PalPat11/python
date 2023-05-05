from coke import *
from fanta import *
from sprite import *
from pepsi import *
from siobarack import *
from os import system

class Automata:
    def __init__(self, coke:Coke, fanta:Fanta, sprite:Sprite, pepsi:Pepsi, siobarack:SioBarack):
        super().__init__()
        self.coke:Coke=coke
        self.fanta:Fanta=fanta
        self.sprite:Sprite=sprite
        self.pepsi:Pepsi=pepsi
        self.siobarack:SioBarack=siobarack

    def __str__(self) -> str:
        return f"{self.coke}\n{self.fanta}\n{self.sprite}\n{self.pepsi}\n{self.siobarack}"
    

        