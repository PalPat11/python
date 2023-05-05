from importlib.util import module_for_loader
from pyexpat import model
from unittest.mock import MagicMock
from os import system
from alaplap import *
from ram import *
from hdd import *
from vga import *
from cpu import *
from tap import *

class Computer:
    def __init__(self, proci:Processor, videokartya:GraphicsCard, ram:Ram, alaplap:Alaplap, tap:Tapegyseg, hdd:Hattertar):
        super().__init__()
        self.proci:Processor=proci
        self.videokartya:GraphicsCard=videokartya
        self.ram:Ram=ram
        self.alaplap:Alaplap=alaplap
        self.tap:Tapegyseg=tap
        self.hdd:Hattertar=hdd

    def __str__(self)->str:
        return f"{self.proci} {self.videokartya} {self.ram} {self.alaplap} {self.tap} {self.hdd}"

    

        
        
        

        
            