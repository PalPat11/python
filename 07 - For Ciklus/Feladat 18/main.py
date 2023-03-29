from os import system
system('cls')

print('Adja meg az intervalumot')
kezdo=int(input())
veg=int(input())

ossz=0



for i in range(kezdo, veg):
    if ossz<=0:
        ossz=ossz+i
    elif ossz>=0:
        ossz=ossz-i
    

print(ossz)
