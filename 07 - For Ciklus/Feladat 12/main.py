from os import system
system('cls')


print('Adja meg az intervallumot')
kezdo=int(input())
veg=int(input())

szam=0

for i in range(kezdo, veg):
    if i%3==0:
        szam+=1
print(szam)