from os import system
system('cls')

szam:str=None
intSzam:int=None
numericE:bool=None
atalakitottString:int=None
osszeg:int=0
print("Adjon meg szmot(")
szam=str(input())


    

while (szam==None or osszeg<100):
    
    atalakitottString=szam.replace(".", "").replace("-", "")
    numericE=atalakitottString.isnumeric()
    if(numericE):
        intSzam=int(szam)
    else:
        continue
    osszeg=intSzam
    probszam=1
    probszam+=1
    osszeg=osszeg+intSzam
    print("Adjon meg még  számokat")
    szam=str(input())


print(f"{probszam} próbálkozásból sikerült elérni" )
print(f"Az összeg: {osszeg}")