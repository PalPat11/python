from os import system
system("cls")


n:int=0
temp:str=None
aalakitotttN:str=None
isNumber:bool=None
otososszeg:int=0
szamlalo:int=0

while(n==None or n>=100 or n<=0):
    print("Adjon meg egy max 2 jegyű számot")
    temp=input()
    aalakitotttN=n.replace(".", "").replace("-", "")
    isNumber=aalakitotttN.isnumeric()
    if(isNumber):
        n=int(temp)

print("Páros számok")

for i in range(0, n):
    if(i%2==0):
        print(i)
    if(i%5==0):
        otososszeg=otososszeg+i
    if(i%11==0):
        szamlalo+=1
    
    print("A 7-tel osztható számok maradéka 3")
    if(i%7==3):
        print(i)
print(szamlalo)
print(otososszeg)