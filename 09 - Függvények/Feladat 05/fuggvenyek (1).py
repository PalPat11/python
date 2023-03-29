from os import system

def meghatarozas(a:str, b:int)->int:
    szamlalo:int=0
    temp:bool=None
    for i in a:
        if(a.count(i)>0):
            temp=True
        if(temp==True):
            szamlalo+=1

    return szamlalo

def szovegbekeres()->str:
    szoveg:str=None
    print("Adjon meg egy szöveget")
    szoveg=input()
    return szoveg