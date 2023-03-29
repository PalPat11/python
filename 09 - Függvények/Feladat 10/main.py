from fuggvenyek import *
system('cls')

randomszam=randomSzamGeneralas(0, 9)
tipp=randomSzamTipp(0, 9)
szamlalo=checking(tipp, randomszam, 0, 9)
print(f"Ennyiszer probálkoztál: {szamlalo}")

randomszam2=randomSzamGeneralas(40, 50)
tipp2=randomSzamTipp(40, 50)
szamlalo2=checking(tipp2, randomszam2, 40, 50)
print(f"Ennyiszer probálkoztál: {szamlalo2}")
