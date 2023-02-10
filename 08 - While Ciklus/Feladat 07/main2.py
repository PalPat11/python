from os import system
system('cls')

kisebb:str=None
atalakitottKisebb:str=None
intKisebb:int=None
nagyobb:str=None
atalakitottNagyobb:str=None
intNagyobb:int=0
isNumber:bool=None

while (kisebb==None):
    print("Adjon meg egy számot")
    kisebb=str(input())
    atalakitottKisebb=kisebb.replace(".", "").replace("-", "")
    isNumber=atalakitottKisebb.isnumeric()
    if(isNumber):
        intKisebb=int(kisebb)
    else:
        continue

while (nagyobb==None or intNagyobb<=intKisebb):
    print("Adjon meg egycghghg számot")
    nagyobb=str(input())
    atalakitottNagyobb=nagyobb.replace(".", "").replace("-", "")
    isNumber=atalakitottNagyobb.isnumeric()
    if(isNumber):
        intNagyobb=int(nagyobb)
    else:
        continue

if intNagyobb>intKisebb:
    for i in reversed(range(intKisebb, intNagyobb)):
        print(i)