from random import randint
from os import system
def ketRandomSzam(a:int, b:int)->int:
    szam=randint(a, b)
    return szam

def tipp()->int:
    szamlalo:int=0
    tipp:str=None
    atalakitott:str=None
    intTipp:int=None
    isNum:bool=None
    while(intTipp==None or intTipp>50 or intTipp<0):
        print("Tippeljen!")
        tipp=input()
        atalakitott=tipp.replace(".", "").replace("-", "")
        isNum=atalakitott.isnumeric()
        if(isNum):
            intTipp=int(tipp)
    return intTipp

def tippHelyesseg(a:int, randomszam:int)->None:
    szamlallo:int=1
    while(a!=randomszam):
        if(a>randomszam):
            print("A random szám kisebb")
        else:
            print("A random szám nagyobb")
        a=tipp()
        szamlallo+=1
    if(a==randomszam):
        print("Elatlálta")
        print(f"{szamlallo} alkalommal tippelt")