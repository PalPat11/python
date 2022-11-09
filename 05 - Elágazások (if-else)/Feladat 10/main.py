from os import system
system('cls')
print("Adja meg a számot")
szam=int(input())

if szam%3==0 and szam%2==0:
    print("ZIZI")
elif szam%2==0:
    print("BIZ")
elif szam%3==0:
    print("BAZ")
else:
    print("nem jou")
