from os import system
system('cls')

strSzam:str=None
szam:int=None
atalakitott:str=None
isNumber:bool=None
szamlalo:int=0
osszeg:int=szam

while(szam==None or osszeg<100000 or osszeg==None):
    print("Adja meg mekkora összege van")
    strSzam=str(input())
    atalakitott=strSzam.replace(".", "").replace("-", "")
    isNumber=atalakitott.isnumeric()
    if(isNumber):
        szam=int(strSzam)
    else:
        continue
    if(szam<100000):
        osszeg=osszeg*1.02
        szamlalo+=1
    else:
        break
print(osszeg)