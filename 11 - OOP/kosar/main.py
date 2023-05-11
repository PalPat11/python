from csapat import *
system('cls')

player1:Player=Player("Józsi", "Uganda", 21, 293)
player2:Player=Player("Peti", "Budapest", 23, 243)
player3:Player=Player("Béla", "Litvánia", 19, 213)
player4:Player=Player("Karcsi", "Oroszország", 21, 197)
player5:Player=Player("Pisti", "Budapest", 21, 41)

csapat=Team=Team(player1, player2, player3, player4, player5)
print(csapat)