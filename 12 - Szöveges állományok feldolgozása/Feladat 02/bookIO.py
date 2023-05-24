from book import  Book
from typing import *
import os

def readBooksFromFile(fileName:str)-> List[Book]:
    books:List[Book]=[]
    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)
    
    oneLine:str = None
    data:List[str] = []
    books:List[Book]=[]
    book: Book = None

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() #Antalfai Martin	3,53
                data = oneLine.split('\t') #tabulátorral elválasztva
        
        return books
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []


