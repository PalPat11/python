from os import system
system('cls')

print("Mit kér?")
szam=int(input())

match szam:
    case 1:
        print("Coca Cola")
    case 2:
        print("Pepsi")
    case 3:
        print("Fanta")
    case 4:
        print("Sprite")
