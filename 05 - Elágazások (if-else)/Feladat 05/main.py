from os import system
system("cls")

print("Irjon be két számpot")
szam1=int(input())
szam2=int(input())

if szam1>szam2:
    print(f"{szam1}, {szam2}")
elif szam1==szam2:
    print("A két szám egyenl")
else:
    print(f"{szam2}, {szam1}")