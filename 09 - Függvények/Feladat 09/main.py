from funkciok import *
system('cls')


osszeg=hufBekeres()
penznem=penzNemValasztas()
eredmeny=atvaltas(osszeg, penznem)
print(f"{osszeg} huf egyenlő {eredmeny} {penznem.upper()}")