from os import system

def countSameLetter(text1:str, text2:str)->int:
    sameLetter:int=None
    intersection:str=""
    for i in text1:
        if(text2.fint(1)>0 and intersection.find(i)==-1):
            intersection=intersection+i
    sameLetter=len(intersection)

    return sameLetter

def szovegbekeres()->str:
    szoveg:str=None
    print("Adjon meg egy szöveget")
    szoveg=input()
    return szoveg