from os import system
system('cls')

intSzam:int=None
szam:str=None
isNUmber:bool=False
atalakitott:str=None

while(szam==None or intSzam==None or (intSzam<0) or (intSzam>9)):
    print("Adjon meg egy számot 0 és 9 között", end=" ")
    szam=str(input())
    atalakitott=szam.replace(".", "").replace("-", "")
    isNUmber=atalakitott.isnumeric()
    if(isNUmber):
        intSzam=int(szam)
        
    else:
        continue
        
print(intSzam)