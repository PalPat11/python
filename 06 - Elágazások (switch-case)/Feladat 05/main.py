from os import system
system('cls')

print("Adja meg az ellenállásokat")
ohm1=int(input())
ohm2=int(input())

print("Adja meg hogyan van kapcsova (soros,párhuzamos)\n Soros: [1]\n Párhuzamos: [2]")
kapcsolas=int(input())

eredmeny:int=None


match kapcsolas:
    case 1:
        eredmeny=ohm1+ohm2
        print(eredmeny)
    case 2:
        eredmeny=(ohm1+ohm2)/(ohm1*ohm2)
        print(eredmeny)