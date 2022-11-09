from os import system
system("cls")

print("Adja meg a számot")
szam=int(input())

if (szam<=40 and szam>=-30):
    print("a száma -30 és 40 között vagyon")
else:
    print("A száma rossz")