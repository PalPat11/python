
def getNumberFromConsole()->float:

    intSzam:int=None
    szam:str=None
    isNUmber:bool=False
    atalakitott:str=None

    while(intSzam==None):
        print("Adjon meg egy számot", end=" ")
        szam=str(input())
        atalakitott=szam.replace(".", "").replace("-", "")
        isNUmber=atalakitott.isnumeric()
        if(isNUmber):
            intSzam=int(szam)
            
        else:
            print("Rossz számot adott meg")
            
    return intSzam

def printToConsole(a:float, b:float, result:float, operator:str)->None:
    print(f"{a} {operator} {b} = {result}")
