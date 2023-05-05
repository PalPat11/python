from pickletools import int4
from statistics import mode


class Motorcycle:

    def __init__(self, type:str, 
                        modell:str, 
                        fuelConsumption:float=0, 
                        productionyear:int=0, 
                        productionyear:int=0, 
                        horsePower:int=0, 
                        manufaturer:str, 
                        cylinders:int=0, 
                        torgue:int=0):
        super().__init__()

        self.type:str=type
        self.modell:str=modell
        self.fuelConsumption:float=fuelConsumption
        self.productionyear:productionyear
        self.horsePower:horsePower
        self.manufaturer:manufaturer
        self.cylinders:cylinders
        self.torgue:torgue
    
    #magoc methods
    def __str__(self)->str:
        return f"{self.manufaturer} {self.modell} ({self.productionyear})"
        