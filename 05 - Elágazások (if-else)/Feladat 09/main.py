from os import system
system('cls')

print('Adja meg a két száméot')
x=int(input())
y=int(input())

if x%y==0:
    print("Osztója")
else:
    print("nem osztoja")