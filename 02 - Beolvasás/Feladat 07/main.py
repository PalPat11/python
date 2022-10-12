from operator import mod
from os import system
system('cls')
print("A kedvenc autómárkája ", end="")

marka:str=str(input())

print("A modellszámát ", end="")

modell:str=str(input())

print("A típusát ", end="")

tipus:str=str(input())

print("köbcenti (ccm) ", end="")

kobcenti:int=int(input())

print("megjelenési évet ", end="")

megjelenesiEv:int=int(input())

print(f"Márka: {marka} \nModell: {modell} \nTípus: {tipus} \nKöbcenti: {kobcenti} \nMegjelenési év: {megjelenesiEv}")