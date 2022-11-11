from os import system
system('cls')


print("Adja meg a aszám,ot")
szam=int(input())

if (szam>10 and szam<20):
    print("A szám 10 és 20 között van")
elif (szam<-10 and szam>-20): 
    print("Ez a szám -10 és -20 között van")
else:
    print("Semmi")