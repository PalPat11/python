from random import randint

def tizRandomSzamListaba()->list:
    lista=[]
    szamlalo:int=0
    while(szamlalo<10):
        randomszam:int=randint()
        lista.append(randomszam)
    return lista

def forditvaOlvasottLista(a:list)->None:
    print(a.reverse())