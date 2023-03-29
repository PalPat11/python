from os import system
system('cls')

print('Adja meg az intervallumot')
kezdo=int(input())
veg=int(input())

osszeg=0

for i in range(kezdo, veg):
    if (i%2!=0) and (i%3==0):
        osszeg+=1
print(osszeg)