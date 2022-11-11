from os import system
system('cls')
print("Adja meg a számot")
szam=int(input())

if (szam%2==0):
    print("A szám páros")
else:
    print("A szám páratlan")

if (szam>0):
    print("A szám pozitiv")
elif (szam==0):
    print("Ez nulaaa")
else:
    print("A szám negatív")
