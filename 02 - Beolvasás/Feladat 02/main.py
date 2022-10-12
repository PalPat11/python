from os import system

system('cls')

print("Adja meg a nevét!", end="")

nev:str=str(input())

print("Adja meg a születési évét!", end="")

szuletesiEv:int=int(input())

print(f"{nev}, ön {szuletesiEv} született")