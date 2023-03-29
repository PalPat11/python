from os import system
system('cls')

print("Addmeg az intervallumot")
kezdo=int(input())
veg=int(input())

paros=0
paratlan=0

for i in range(kezdo, veg):
    if i%2==0:
        paros=paros+i
    else:
        paratlan=paratlan+i

osszeg=(paros+paratlan)/2
print(osszeg)