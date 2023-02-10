from random import randint
from os import system
system('cls')

paros:int=None
paratlan:int=None
random:int=None
atlag:int=0
atlagszamlalo:int=0
neggyel:int=0


print("Adjon meg egy páros számot")
paros=int(input())

while(paros%2!=0):
    print("Helyes értéket adjon meg")
    paros=int(input())

print("Adjon meg egy, az előzőnél nagyobb páratla számot")
paratlan=int(input())

while(paratlan%2==0 or paratlan<=paros):
    print("Helyes értéket adjon meg")
    paratlan=int(input())

random=randint(paros, paratlan)

if(random-paros>paratlan-random):
    print("A páros szám messzebb van a random számtól")
elif(random-paros<paratlan-random):
    print("A páratlan szám van messzebb a random számtól")

for i in range(paros, paratlan):
    atlag=atlag+i
    atlagszamlalo+=1
    if(i%4==0):
        neggyel+=1
atlag=atlag/atlagszamlalo
print(atlag)
print(neggyel)