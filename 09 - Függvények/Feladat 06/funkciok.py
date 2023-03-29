def atvaltoCToKelvin(ertek:float)->float:
    kelvin=ertek+273.15
    return kelvin

def atvaltCToFarentheit(ertek:float)->float:
    farentheit=9/5*ertek+32
    return farentheit

def printToConsole()->float:
    co:str=None
    floatco:int=None
    atalakitottCo:str=None
    isNum:bool=None
    while(floatco==None):
        print("Adja meg Celsiusban")
        co=input()
        atalakitottCo=co.replace(".", "").replace("-", "")
        isNum=atalakitottCo.isnumeric()
        if(isNum):
            floatco=float(co)
    return floatco

def kVagyF()->str:
    klevin:str=None
    print("Adja meg mibe váltsak K vagy F")
    klevin=input()
    klevin=klevin.lower()
    return klevin
