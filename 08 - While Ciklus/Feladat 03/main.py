from os import system
system('cls')

import random

szam=random.randint(0, 9)
number:float=None
temp:str=None
inNumber:bool=None
truncatedString:str=None
szamlalo:int=0

while(number==None or (number<0 or number>9)):
    print("Tippeljen egy számot 0 és 9 között")
    temp=str(input())
    truncatedString=temp.replace(".", "").replace("-", "")
    isNumber=truncatedString.isnumeric()
    
    if(isNumber):
        number=(float(temp))
    else:
        print("Rossz számot adott meg")
    
    while(number!=szam):
        print("Próbálja újra")
        temp=str(input())
        szamlalo+=1
        if(szamlalo==4):
            print("Vége")
            break



