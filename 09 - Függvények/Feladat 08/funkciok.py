import math
def xBekerese()->float:
    x:str=None
    intX:float=None
    xAtalakit:str=None
    isNum:bool=None
    while(intX==None):
        print("Adja meg az X koordinátát")
        x=input()
        xAtalakit=x.replace(".", "").replace("-", "")
        isNum=xAtalakit.isnumeric()
        if(isNum):
            intX=float(x)
        return intX

def yBekerese()->float:
    y:str=None
    intY:float=None
    yAtalakit:str=None
    isNum:bool=None
    while(intY==None):
        print("Adja meg az Y koordinátát")
        y=input()
        yAtalakit=y.replace(".", "").replace("-", "")
        isNum=yAtalakit.isnumeric()
        if(isNum):
            intY=float(y)
        return intY

def pitagorasz(a:float, b:float)->float:
    tav=math.sqrt((a*a+b*b))
    return tav