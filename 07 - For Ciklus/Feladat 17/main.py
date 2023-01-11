from os import system
system('cls')

print("Adja meg az intervallumot")
kezdo=int(input())
veg=int(input())

szam=0

for i in range(kezdo, veg):
    szam=szam+i

atlag=szam/len(range(kezdo, veg))
print(atlag)