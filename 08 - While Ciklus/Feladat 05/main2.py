from os import system
system('cls')


hatarertek:str=None
intHatarertek:int=0
isNumber:bool=None
atalakitHatarertek:str=None

bekert:str=None
intBekert:int=None
atalakitBekert:str=None
osszeg:int=0
szamlalo:int=0


while(hatarertek==None or intHatarertek<100):
    print("Ajon meg egy határértéket")
    hatarertek=str(input())
    atalakitHatarertek=hatarertek.replace(".", "").replace("-", "")
    isNumber=atalakitHatarertek.isnumeric()
    if(isNumber):
        intHatarertek=int(hatarertek)


while(bekert==None or osszeg<intHatarertek):
    print("Kezdje el összeadni a számokat")
    bekert=str(input())
    atalakitBekert=bekert.replace(".", "").replace("-", "")
    isNumber=atalakitBekert.isnumeric()
    if(isNumber):
        intBekert=int(bekert)
        szamlalo+=1
        osszeg=osszeg+intBekert
print(szamlalo)
print(osszeg)
