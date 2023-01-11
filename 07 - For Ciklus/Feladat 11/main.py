from os import system
system('cls')

print("Adja meg a kezdő vég")
kez=int(input())
veg=int(input())

osszeg=0

szorzat=1

for i in range(kez,veg):
    if i%2==0:
        i=i+2
        osszeg=osszeg+i
        print(osszeg)
    elif i%2!=0:
        i=i+2
        szorzat=osszeg*i
        print(szorzat)