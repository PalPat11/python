from os import system

system('cls')

system('color a')

print("Adja meg a nevét!", end="")

nev:str=str(input())

print("Nyomjon le egy billentyűt!", end="")

billentyu:str=str(input())

print(f"Ön, {nev} a/az {billentyu} billentyűt nyomta le")
