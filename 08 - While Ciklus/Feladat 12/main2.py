from os import system
system('cls')

strSzam:str=None
szam:int=0
atalakitott:str=None
isNumber:bool=None
szamlalo:int=0
osszeg:int=szam

while(szam<1):
    print("Adja meg mennyi péne van")
    strSzam=input()
    atalakitott=strSzam.replace(".", "").replace("-", "")
    isNumber=atalakitott.isnumeric()
    if(isNumber):
        szam=int(strSzam)

while(osszeg<100000):
    szamlalo+=1
    osszeg=osszeg+(szam*0.02)

print(f"{szamlalo} hónap alatt éri el")
print(f"Az összeg:{osszeg}")