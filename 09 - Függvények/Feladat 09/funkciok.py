from os import system

def hufBekeres()->float:
    floatSzam:float=None
    szam:str=None
    atalakitott:str=None
    inNum:bool=None
    while(floatSzam==None):
        print("Adja meg az összeget Forintban")
        szam=input()
        atalakitott=szam.lower().replace(".", "").replace("-", "").replace(" ", "").replace("ft", "")
        inNum=atalakitott.isnumeric()
        if(inNum):
            szam=szam.lower().replace(" ", "").replace("ft", "")
            floatSzam=float(szam)
    return floatSzam

def penzNemValasztas()->str:
    penzNem:str=None
    while(penzNem!="jpy" and penzNem!="usd" and penzNem!="chf" or penzNem==None):
        print("Adja meg mibe szeretné váltaani JPY, USD, CHF")
        penzNem=input()
        penzNem=penzNem.lower()
    return penzNem
    
def atvaltas(penz:float, fajta:str)->float:
    euro:float=None
    euro=penz*0.0026
    atvaltott:float=None
    if(fajta=="jpy"):
        atvaltott=euro/0.75
    elif(fajta=="usd"):
        atvaltott=euro/0.8
    elif(fajta=="chf"):
        atvaltott=euro/0.55
    return atvaltott


