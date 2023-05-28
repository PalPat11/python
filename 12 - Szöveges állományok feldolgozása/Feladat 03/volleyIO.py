from volley import *
from typing import *
from io import open
import os


def readVolleyballPlayers()->List[Volley]:
    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    oneLine:str = None
    data:List[str] = []
    players:List[Volley]=[]
    player: Volley = None

    try:
        with open(fileFullPath, mode="r") as file:
            for line in file:
                oneLine=line.strip()
                data=oneLine.split('\t')

                player=Volley()
                player.name=data[0]
                player.height=data[1]
                player.position=data[2]
                player.nationality=data[3]
                player.team=data[4]
                player.country=data[5]

                players.append(player)
        return players
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []


def writePuncherPlayers(players:List[Volley], fileName:str)->None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath+="/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for i in players:
                if(i.position=="ütő"):
                    file.write(f"{i.name} {i.position} {i.team} {i.country}\n")
    except FileNotFoundError as ex:
        print(f"{ex.fileName} Nem található")
