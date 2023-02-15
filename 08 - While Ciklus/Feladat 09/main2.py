from os import system
system("cls")

szam:str=None
intSzam:int=0
isNumber:bool=None
atalakitottSzam:str=None

while(szam==None or intSzam<=99 or intSzam>=1000):
    print("Adjon meg egy 3 jegyű számot")
    szam=str(input())
    atalakitottSzam=szam.replace(".", "").replace("-", "")
    isNumber=atalakitottSzam.isnumeric()
    if(isNumber):
        intSzam=int(szam)
if(intSzam%7==0):
    print("Osztható 7-tel a szám")
else:
    print("nem oszható")