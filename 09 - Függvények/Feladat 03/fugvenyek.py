def eletkorFigyelo()->int:
    intKor:int=None
    kor:str=None
    atalakitottKor:str=None
    isNum:bool=None
    while(intKor==None or intKor<0):
        print("Adja meg az életkorát")
        kor=input()
        atalakitottKor=kor.replace(".", "").replace("-", "")
        isNum=atalakitottKor.isnumeric()
        if(isNum):
            intKor=int(kor)
    return intKor




    

def readNameFromConsole()->str:
    name:str=None
    while(name==None or len(name)<2):
        print("Adja meg a nevét: ", end="")
        name=input()

        if(len(name)<2):
            print("Ne megfelelő a név")

    return name.capitalize().strip()







def writeWelcomeInConsole(kor:int, nev:str)->None:
    print(f"Kedves {nev}, ön {kor} éves")