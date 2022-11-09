from os import system
system('cls')

print("Adja meg a 2 számot")
szam1=int(input())
szam2=int(input())
if szam1<=szam2:
    print(szam2)
elif szam2<=szam1:
    print(szam1 )
else:
    print("ugyanannyi")
