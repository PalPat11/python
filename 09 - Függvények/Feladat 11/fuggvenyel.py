from os import system

def nevBekeres()->str:
    nev:str=None

    print("Adjon meg egy nevet")
    nev=input()
    return nev

def ledolgozottOrakSzama()->int:
    ora:str=None
    talakitottora:str=None
    intOra:int=None
    isNum:bool=None
    while(intOra==None or intOra>112 or intOra<0):
        print("Adja meg hány órát dolgozott")
        ora=input()
        talakitottora=ora.replace(".", "").replace("-", "")
        isNum=talakitottora.isnumeric()
        if(isNum):
            intOra=int(ora)
    return intOra

def berKiszamitasa(a:int)->int:
    ber:int=None
    if(a<=40):
        ber=a*1000
    else:
        a=a-40
        ber=(a*1500)+40000
    return ber