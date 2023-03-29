
def readNameFromConsole()->str:
    name:str=None
    while(name==None or len(name)<2):
        print("Nev: ", end="")
        name=input()

        if(len(name)<2):
            print("Ne megfelelő a név")

    return name.capitalize().strip()

def printWElcomeMeassage(name:str)->None:
    print(f"Welcome {name}")