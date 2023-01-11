from os import system
system('cls')

print("Adja meg a kezdő és végértéket")
kezdo=int(input())
veg=int(input())



for i in reversed(range(kezdo, veg)):
    if i%2==0:
        print(i)
