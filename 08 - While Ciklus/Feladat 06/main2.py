from os import system
system("cls")

beolvasott:str=None
intBeolvasott:int=None
isNumber:bool=None
atalakitottBeolvasott:str=None

while(beolvasott==None or intBeolvasott==None):
    print("Adja meg az életkorát")
    beolvasott=str(input())
    atalakitottBeolvasott=beolvasott.replace("-", "").replace(".", "")
    isNumber=atalakitottBeolvasott.isnumeric()
    if(isNumber):
        intBeolvasott=int(beolvasott)
    else:
        continue

if(intBeolvasott<=6):
    print("Gyrek")
elif(intBeolvasott>=7 and intBeolvasott<=18):
    print("Iskolás")
elif(intBeolvasott>=19 and intBeolvasott<=65):
    print("dolgozó")
elif(intBeolvasott>=65):
    print("Nyugdíjas")