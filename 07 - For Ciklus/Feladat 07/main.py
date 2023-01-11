from os import system
system('cls')

print("Adja meg a kezdő és végértéket")
kezdoertek=int(input())
vegertek=int(input())

for i in range(kezdoertek, vegertek, -1):
    print(i)