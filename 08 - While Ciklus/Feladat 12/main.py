from os import system
system('cls')

strSzam:str=None
szam:int=None
atalakitott:str=None
isNumber:bool=None
szamlalo:int=0
osszeg:int=szam

while(szam==None):
    print("Adja meg mennyi péne van")
    strSzam=input()
    atalakitott=strSzam.replace(".", "").replace("-", "")
    isNumber=atalakitott.isnumeric()
    if(isNumber):
        szam=int(strSzam)

while(szam<100000):
    szamlalo+=1
    szam=szam*1.02
print(szamlalo)
print(szam)