from os import system
system('cls')

print("Adja meg a két számot")
szam1=int(input())
szam2=int(input())

print("Adja meg a matematikai műveletet (+,-,*,/)")
muvelet=str(input())

eredmen:int=None

match muvelet:
    case "+":
        eredmen=szam1+szam2
        print(eredmen)
    case "-":
        eredmen=szam1-szam2
        print(eredmen)
    case "*":
        eredmen=szam1*szam2
        print(eredmen)
    case "/":
        eredmen=szam1/szam2
        print(eredmen)