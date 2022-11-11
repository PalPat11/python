from os import system
system('cls')

print("Aja meg a számot")
szam=int(input())

if szam%4==0 and szam%6==0:
    print("A szám osthtao 6-al és 4-el")
else:
    (print("A szám nem osztható"))