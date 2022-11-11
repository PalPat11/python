from os import system

system('cls')

print("Írja be a kedvenc filmjének a címét!", end="")

kedvencFilm:str=str(input())

print("Megjelenési év", end="")

megjelenesiEv:int=int(input())

print("Megjelenési év", end="")

rendezoNeve:str=str(input())

print("főszereplő neve", end="")

foszereplo:str=str(input())

print(f"{megjelenesiEv}-ban {rendezoNeve} rendezésében megjelent a/az {kedvencFilm} című film {foszereplo} főszereplésével.")