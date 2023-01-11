from os import system
system('cls')

print("kezdő és vég")
kezdo=int(input())
veg=int(input())

osszeg=0

for i in range(kezdo,veg):
    osszeg=osszeg+i

print(osszeg)

szorzat=1

for i in range(kezdo, veg):
    szorzat=szorzat*i
print(szorzat)