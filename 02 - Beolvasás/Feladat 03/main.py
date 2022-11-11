from os import system

system('cls')

print("Adja meg a nevét!", end="")

nev:str=str(input())

print("Adja meg a magasságát(m)!", end="")


magassag:float=float(input())

print(f"{nev}, ön magassága {magassag}m")