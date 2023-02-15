from os import system
system('cls')

print('Adja meg az intervallumot')
kezdoertek=int(input())
vegertek=int(input())

osszeg=0

for i in range(kezdoertek, vegertek):
    osszeg=osszeg+i
print(f"A {kezdoertek} és a {vegertek} közti számok összege: {osszeg}")


atlagosszege=0

darab=0

for j in range(kezdoertek, vegertek):
    atlagosszege=atlagosszege+j
    darab+=1

atlag=atlagosszege/darab

print(f'A {kezdoertek} és a {vegertek} közti számok átlaga: {atlag}')

print(f'A {kezdoertek} és {vegertek} közti hárommal osztható számok:')

for k in range(kezdoertek, vegertek):
    if k%3==0:
        print(k)