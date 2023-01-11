from os import system
system('cls')

print("kezdő és vég")
kezdo=int(input())
veg=int(input())

osszeg=0

for i in range(kezdo,veg):
    i+=1
    osszeg=osszeg+i

    print(osszeg)
