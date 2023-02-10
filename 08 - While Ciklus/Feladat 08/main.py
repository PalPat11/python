from os import system
system('cls')

print("Válasszon az üdítők közül")
print("Coca Cola: [1]")
print("Pepsi Cola: [2]")
print("Fanta: [3]")
print("Sprite: [4]")
szam=str(input())

while (szam!="1" and szam!="2" and szam!="3" and szam!="4"):
    print("Helyes számot válasszon")
    szam=str(input())

match szam:
    case "1":
        print("Ön a Coca Colát választotta")
    case "2":
        print("Ön a Pepsi Colát választotta")
    case "3":
        print("Ön a Fantát választotta")
    case "4":
        print("Ön a Spriteot választotta")
