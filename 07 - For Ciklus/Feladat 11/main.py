from os import system
system('cls')

print("Adja meg a kezdő vég")
kez=int(input())
veg=int(input())

osszeg=0

for i in range(kez, veg):
    if i%2==0:
        osszeg=osszeg+i
print(osszeg)

szorzat=1

for i in range(kez, veg):
    if i%2!=0:
        szorzat=szorzat*i
print(szorzat)