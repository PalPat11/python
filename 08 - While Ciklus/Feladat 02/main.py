from os import system
system('cls')

nev:str=None
while(nev==None or len(nev)<2):
    print("Adja meg a nevét")
    nev=input()
print(f"Üdvözöljük {nev}!")