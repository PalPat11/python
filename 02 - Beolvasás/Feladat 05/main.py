from os import system

system('cls')

print("Irja be a kedvenc együttesének nevét! ", end="")

egyuttes:str=str(input())

print("írja be a kedvenc számának nevét ettől az együttestől! ", end="")

kedvencSzam:str=str(input())

print("irja be ennek a számnak hosszát! ", end="")

szamHossza:int=int(input())


print(f"Az ön kedvenc együttesének {egyuttes} a legjobb szeneszáma {kedvencSzam} melynek hossza {szamHossza} perc")