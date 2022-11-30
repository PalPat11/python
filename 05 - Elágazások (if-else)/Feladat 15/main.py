from os import system
system('cls')





print("Válasszon előételt")
print("Zöldségleves [1]")
print("Húsleves [2]")
print("Gyümölcsleves [3]")
print("Nem kérek előételt [0]")



valasztas=int(input())

zoldsegleves:bool=False
husleves:bool=False
gyumolcsleves:bool=False


if (valasztas==1):
    zoldsegleves=True
elif (valasztas==2):
    husleves=True
elif (valasztas==3):
    gyumolcsleves=True
elif(valasztas==0):
    eloetel:int=0


if (zoldsegleves==True):
    eloetel:int=1
elif (husleves==True):
    eloetel:int=2
elif (gyumolcsleves==True):
    eloetel:int=3


print("Válasszon Főételt")
print("Sültcsirkecomb [1]")
print("Sült csirkemell [2]")
print("Rakottzöldség [3]")
print("Spagetti [4]")
print("Pizza [5]")
print("Nem kérek főételt [0]")

valasztas=int(input())

csirkecomb:bool=False
csirkemell:bool=False
rakottzoldseg:bool=False
spagetti:bool=False
pizza:bool=False


if (valasztas==1):
    csirkecomb=True
elif (valasztas==2):
    csirkemell=True
elif (valasztas==3):
    rakottzoldseg=True
elif (valasztas==4):
    spagetti=True
elif (valasztas==5):
    pizza=True
elif(valasztas==0):
    foetel:int=0



if (csirkecomb==True):
    foetel:int=1
elif(csirkemell==True):
    foetel:int=2
elif(rakottzoldseg==True):
    foetel:int=3
elif(spagetti==True):
    foetel:int=4
elif(pizza==True):
    foetel:int=5

print("Válasszon köretet")
print("Rizs [1]")
print("Pároltzöldség [2]")
print("Gyümölcs [3]")
print("Sültkrumpli [4]")
print("Saláta [5]")
print("Kóla [6]")
print("Nem kérek köretet [0]")


valasztas=int(input())

rizs:bool=False
paroltzoldseg:bool=False
gyumolcs:bool=False
sultkrumpli:bool=False
salata:bool=False
kola:bool=False


if (valasztas==1):
    rizs=True
elif (valasztas==2):
    paroltzoldseg=True
elif (valasztas==3):
    gyumolcs=True
elif (valasztas==4):
    sultkrumpli=True
elif (valasztas==5):
    salata=True
elif (valasztas==6):
    kola=True
elif(valasztas==0):
    koret:int=0


if (rizs==True):
    koret:int=1
elif(paroltzoldseg==True):
    koret:int=2
elif(gyumolcs==True):
    koret:int=3
elif(sultkrumpli==True):
    koret:int=4
elif(salata==True):
    koret:int=5
elif(kola==True):
    koret:int=6

if(zoldsegleves==True and csirkemell==True and sultkrumpli==False and rizs==True):
    print("Fitnesz menü")
elif(husleves==True and csirkecomb==True and (sultkrumpli or salata)==True and (pizza and rakottzoldseg)==False):
    print("Vasárnapi menü")
elif((pizza or spagetti)==True and (gyumolcs or kola==True) and (rakottzoldseg and paroltzoldseg)==False):
    print("Napi menü")


if(eloetel>0 and foetel>0 and koret>0 or (zoldsegleves==True and spagetti==True and (gyumolcs or salata)==True and pizza==False and rakottzoldseg==True)):
    print("Kiváló értékelés")
else:
    print("Szerény étkezés")