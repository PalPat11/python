from os import system
system("cls")

print("Adjon meg két értéket ugy hogy az első nagyobb legyen")
nagyobbszam=int(input())
kisebbszam=int(input())

while kisebbszam>=nagyobbszam:
    print("Adjon meg helyes értékeket")
    nagyobbszam=int(input())
    kisebbszam=int(input())


if nagyobbszam>kisebbszam:
    for i in reversed(range(kisebbszam, nagyobbszam)):
        print(i)