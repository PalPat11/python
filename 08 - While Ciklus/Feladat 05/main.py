from os import system
system('cls')

print("Adjon meg határértéket (legalább 100)")
hatar=int(input())



while hatar<100:
    print("Adjon meg érvényes határértéket")
    hatar=int(input())

print("Kezdje el összeadni a számokat")
szamok=int(input())

szamlalo=1

osszeg=szamok

while osszeg<hatar:
    szamlalo+=1
    szamok=int(input())
    osszeg=osszeg+szamok

print(szamlalo)
print(osszeg)



