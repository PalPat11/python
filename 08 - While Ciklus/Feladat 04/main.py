from os import system
system('cls')

szam:str=None
intSzam:int=None
numericE:bool=None
atalakitottString:int=None
osszeg:int=0
probszam:int=0

while (szam==None or osszeg<100):
    print("Adjon meg szmot(")
    szam=str(input())
    atalakitottString=szam.replace(".", "").replace("-", "")
    numericE=atalakitottString.isnumeric()
    if(numericE):
        intSzam=int(szam)
        probszam+=1
        osszeg=osszeg+intSzam


print(f"{probszam} próbálkozásból sikerült elérni" )
print(f"Az összeg: {osszeg}")