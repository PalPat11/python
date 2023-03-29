from os import system
system('cls')

from funkciok import *

ertak=printToConsole()
eredmeny:float=None
valasztas=kVagyF()

while(eredmeny==None):
    if(valasztas=="k"):
        eredmeny=atvaltoCToKelvin(ertak)
    elif(valasztas=="f"):
        eredmeny=atvaltCToFarentheit(ertak)
    else:
        valasztas=kVagyF()

print(eredmeny)