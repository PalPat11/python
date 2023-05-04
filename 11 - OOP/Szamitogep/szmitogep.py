from importlib.util import module_for_loader
from pyexpat import model
from unittest.mock import MagicMock
from os import system

class Processor:
    def __init__(self, gyarto:str, modell:str, szalak:int=0, magok:int=0 ):
        super().__init__()
        self.szalak:int=szalak
        self.magok:int=magok
        self.gyarto:str=gyarto
        self.modell:str=modell
    def __str__(self)->str:
        return f" Processzor: {self.gyarto} {self.modell} {self.szalak} szál {self.magok} mag\n"

class GraphicsCard:
    def __init__(self, gyarto:str, modell:str, vram:int=0, cores:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.vram:int=vram
        self.cores:int=cores
    def __str__(self)->str:
        return f"Videókártya: {self.gyarto} {self.modell} {self.vram}GB {self.cores} Core\n"



class Ram:
    def __init__(self, gyarto:str, modell:str, kapacitas:int=0, mennyiseg:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.kapacitas:int=kapacitas
        self.mennyiseg:int=mennyiseg
    def __str__(self)->str:
        return f"RAM: {self.gyarto} {self.modell} {self.kapacitas}GB {self.mennyiseg}db szlot\n"

class Alaplap:
    def __init__(self, gyarto:str, modell:str, vidikartyahely:str, ramszlotokSzama:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.ramszlotokSzama:int=ramszlotokSzama
        self.vidikartyahely:int=vidikartyahely
    def __str__(self)->str:
        return f"Alaplap: {self.gyarto} {self.modell} {self.ramszlotokSzama}db, videokártya szlot típusa: {self.vidikartyahely}\n"

class Tapegyseg:
    def __init__(self, gyarto:str, modell:str, fogyasztas:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.fogyasztas:int=fogyasztas
    def __str__(self)->str:
        return f"Tapegység: {self.gyarto} {self.modell} {self.fogyasztas} Watt\n"


class Hattertar:
    def __init__(self, gyarto:str, modell:str, kapacitas:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.kapacitas:int=kapacitas
    def __str__(self)->str:
        return f"Háttértár: {self.gyarto} {self.modell} {self.kapacitas}GB \n"


class Computer:
    def __init__(self, proci:Processor=Processor("AMD", "Ryzen 5 1600", 12, 6), 
                    videokartya:GraphicsCard=GraphicsCard("AMD", "RX 580", 8, 2034), 
                    ram:Ram=Ram("Corsair", "DDR4 3000MHz Vengeance", 8, 2), 
                    alaplap:Alaplap=Alaplap("Asus", "TUF Gaming B550M PLUSZ", "PCI Express", 4), 
                    tap:Tapegyseg=Tapegyseg("APPROX","APP500PSV2", 500),
                    hdd:Hattertar=Hattertar("Kingston", "SSD", 1024)):
        super().__init__()
        self.proci:Processor=proci
        self.videokartya:GraphicsCard=videokartya
        self.ram:Ram=ram
        self.alaplap:Alaplap=alaplap
        self.tap:Tapegyseg=tap
        self.hdd:Hattertar=hdd

    def __str__(self)->str:
        return f"{self.proci} {self.videokartya} {self.ram} {self.alaplap} {self.tap} {self.hdd}"

    

        
        
        

        
            