from volleyIO import *

players:List[Volley]=readVolleyballPlayers()

for i in players:
    print(i)

writePuncherPlayers(players, "utok")