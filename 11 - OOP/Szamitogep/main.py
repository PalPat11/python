from szmitogep import *
system('cls')

proci:Processor=Processor("AMD", "Ryzen 5 1600", 12, 6)
videokartya:GraphicsCard=GraphicsCard("AMD", "RX 580", 8, 2034) 
ram:Ram=Ram("Corsair", "DDR4 3000MHz Vengeance", 8, 2) 
alaplap:Alaplap=Alaplap("Asus", "TUF Gaming B550M PLUSZ", "PCI Express", 4)
tap:Tapegyseg=Tapegyseg("APPROX","APP500PSV2", 500)
hdd:Hattertar=Hattertar("Kingston", "SSD", 1024)

gep:Computer=Computer(proci, videokartya, ram, alaplap, tap, hdd)

print(gep)