from os import system
system("cls")

print("Adja meg az életkorát")
kor=int(input())

while kor<0 or kor>99:
    print("Érvényes kort adjon meg")
    kor=int(input())

if kor>=0 and kor<=6:
    print("Ön gyerek")
elif kor>=7 and kor<=18:
    print("Ön iskolás")
elif kor>=19 and kor<=65:
    print("Ön dolgozó")
else:
    print("Ön nyugdíjas")