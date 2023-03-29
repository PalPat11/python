from os import system
from random import randint

def randomSzamGeneralas(a:int, b:int)->int:
    szam:int=None
    szam=randint(a, b)
    return szam

def randomSzamTipp(a:int, b:int)->int:
    tipp:str=None
    atalakitotttipp:str=None
    intTipp:int=None
    isNum:bool=None
    while(intTipp==None or intTipp>b or intTipp<a):
        print(f"Tippeljen {a} és {b} között")
        tipp=input()
        atalakitotttipp=tipp.replace(".", "").replace("-", "")
        isNum=atalakitotttipp.isnumeric()
        if(isNum):
            intTipp=int(tipp)
    return intTipp

def checking(tipp:int, randomszam:int, a:int, b:int)->int:
    szamlalo:int=1
    while(tipp!=randomszam):
        tipp=randomSzamTipp(a, b)
        szamlalo+=1
    return szamlalo

