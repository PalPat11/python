from gepezet import *
system('cls')

coke:Udito=Udito("Coca Cola", "190 KJ/ 45 kcal", 0, 11.2, 0, 0)
fanta:Udito=Udito("Fanta", "121 KJ/ 28 kcal", 0, 6.9, 0, 0.02)
sprite:Udito=Udito("Sprite", "40 KJ/ 9kcal", 0, 2, 0, 0.01)
pepsi:Udito=Udito("Pepsi", "120 KJ/ 28 kcal", 0, 7, 0, 0.01)
siobarack:Udito=Udito("Sió-Barack", "167 KJ/ 39 kcal", 0.5, 9.1, 0.5, 0.01)

automata:Automata=Automata(coke, fanta, sprite, pepsi, siobarack)

print(automata)