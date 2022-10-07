from os import system
system('cls')
egyuttes:str=str(input("Irja be a kedvenc együttesének nevét! "))

kedvencSzam:str=str(input("írja be a kedvenc számának nevét ettől az együttestől! "))

szamHossza:int=int(input("irja be ennek a számnak hosszát! "))

print(f"Az ön kedvenc együttesének {egyuttes} a legjobb szeneszáma {kedvencSzam} melynek hossza {szamHossza} perc")