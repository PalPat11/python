from os import system
system("cls")

szam:int=None
otteloszt:int=0
tizenegy:int=0

print("Adjon meg egy 2 jegyű poitív számot")
szam=int(input())

while(szam<10 or szam>99):
    print("Érvényes számot adjon meg")
    szam=int(input())

for i in range(0, szam):
    if(i%2==0):

        print(i)
    if(i%5==0):
        otteloszt=otteloszt+i

    if(i%11==0):
        tizenegy+=1

    if(i%7==3):
        print("Héttel osztva 3 a maradék")
        print(i)

print(f"Öttel osztható számok öszege: {otteloszt}")
print(f"{tizenegy} tizenegyel osztható szám van")