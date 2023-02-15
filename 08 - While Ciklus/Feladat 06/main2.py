from os import system
system("cls")

beolvasott:str=None
intBeolvasott:int=-1
isNumber:bool=None
atalakitottBeolvasott:str=None

while(intBeolvasott<0 or intBeolvasott>99):
    print("Adja meg az életkorát")
    beolvasott=str(input())
    atalakitottBeolvasott=beolvasott.replace("-", "").replace(".", "")
    isNumber=atalakitottBeolvasott.isnumeric()
    if(isNumber):
        intBeolvasott=int(beolvasott)


if(intBeolvasott<=6):
    print("Gyrek")
elif(intBeolvasott>=7 and intBeolvasott<=18):
    print("Iskolás")
elif(intBeolvasott>=19 and intBeolvasott<=65):
    print("dolgozó")
elif(intBeolvasott>=65):
    print("Nyugdíjas")