from os import system
system('cls')

print("Válasszon az üdítők közül")
print("Coca Cola: [1]")
print("Pepsi Cola: [2]")
print("Fanta: [3]")
print("Sprite: [4]")
szam=int(input())

while(szam<0 or szam>4):
    print("Jó számot adjon meg")
    szam=int(input())


match szam:
    case 1:
        print("Ön a Coca Colát választotta")
    case 2:
        print("Ön a Pepsi Colát választotta")
    case 3:
        print("Ön a Fantát választotta")
    case 4:
        print("Ön a Spriteot választotta")
