from os import system
system('cls')
from random import randint

paros:str=None
atalakitottparos:str=None
intParos:int=0
isNumber:bool=None
paratlan:str=None
intParatlan:int=0
atalakitottparatlan:str=None

while(paros==None or intParos%2!=0):
    print("Adjon meg egy páros számot")
    paros=str(input())
    atalakitottparos=paros.replace(".", "").replace("-", "")
    isNumber=atalakitottparos.isnumeric()
    if(isNumber):
        intParos=int(paros)


while(paratlan==None or intParatlan%2==0 or intParatlan<intParos):
    print("Adjon meg egy páratlan számot")
    paratlan=str(input())
    atalakitottparatlan=paratlan.replace(".", "").replace("-", "")
    isNumber=atalakitottparatlan.isnumeric()
    if(isNumber):
        intParatlan=int(paratlan)


randomszam:int=randint(intParos, intParatlan)

if(randomszam-intParos>intParatlan-randomszam):
    print("a páros van messzebb")
elif(randomszam-intParos<intParatlan-randomszam):
    print("A páratlan van messzebb")

szamlalo:int=0
atlag:int=0
szamlalo22:int=0
for i in range(intParos, intParatlan):
    if(i%4==0):
        szamlalo+=1
    szamlalo22+=1
    atlag=i+i
atlag=atlag/szamlalo22

print(szamlalo)
print(atlag)
