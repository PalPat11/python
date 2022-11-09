from os import system
system('cls')

print("Adja meg a számot")
szam=int(input())
if szam<=0:
    print("A számod negativ")
elif szam==0:
    print("ez nulla bratysz")
else:
    print("Pozitiv")