from os import system
system('cls')

<<<<<<< HEAD
=======
print('Adja meg az intervallumot')
kezdo=int(input())
veg=int(input())

paros=0
paratlan=0

for i in range(kezdo, veg):
    if i%2==0:
        paros+=1
    else:
        paratlan+=1

if paros<paratlan:
    print("A páratlanok nagyobbak")
elif paros>paratlan:
    print('A párosak nagyobbak')    
else:
    print("Egyenléőek")
>>>>>>> f16ed382cb88802681740f20118d9adad8861573
