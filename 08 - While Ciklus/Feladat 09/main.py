from os import system
system('cls')

szam:int=None

print("Adjon meg egy 3 jegyű számot")
szam=int(input())

while(szam<100 or szam>999):
    print("Adjon meg érvényes számot")
    szam=int(input())

if(szam%7==0):
    print("Osztható")
else:
    print("Nem osztható")