from os import system
system("cls")

n:str=None
intN:int=0
aalakitotttN:str=None
isNumber:bool=None
otososszeg:int=0
szamlalo:int=0

while(n==None or intN>=100 or intN<=0):
    print("Adjon meg egy max 2 jegyű számot")
    n=str(input())
    aalakitotttN=n.replace(".", "").replace("-", "")
    isNumber=aalakitotttN.isnumeric()
    if(isNumber):
        intN=int(n)
    else:
        continue

for i in range(0, intN):
    if(i%2==0):
        print(i)
    if(i%5==0):
        otososszeg=otososszeg+i
    if(i%11==0):
        szamlalo+=1
        
    if(i%7==3):
        print(i)
print(szamlalo)
print(otososszeg)