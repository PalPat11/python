from os import system
system('cls')

print("Adja meg a 2 oldalt")
a=int(input())
b=int(input())

print("Terület [1]\n Keület [2]\n Átló [3]")
valasztas=int(input())
eredmeny:int=None

import math
match valasztas:
    case 1:
        eredmeny=a*b
        print(eredmeny)
    case 2:
        eredmeny=(a+b)*2
        print(eredmeny)
    case 3:
        eredmeny=math.sqrt((a**2)+(b**2))
        print(eredmeny)

