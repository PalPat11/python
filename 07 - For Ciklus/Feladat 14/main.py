from os import system
system('cls')

print("Adja meg a két intervallumot")
kezdo=int(input())
veg=int(input())

otos=0
hetes=0

for i in range(kezdo, veg):
    if i%5==0:
        otos=otos+i
    elif i%7==0:
        hetes=hetes+i

if hetes>otos:
    print('A hetesekkel osztható szémok a nagyobbak')
elif hetes<otos:
    print('Az ötösökkel osztható számok a nagyobbak')
else:
    print('Egyenlő a két érték')