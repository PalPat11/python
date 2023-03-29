from colored import * # Terminálon futtatni való      | pip install colored |

def greeting(text:str) -> None:
    text = text.title()
    color = len(text)
    print(f'%sÜdvözlöm {text}%s' % (fg(color), attr(0)))
    


def nevBeolvasas()->str:
    name:str=None
    while(name==None or len(name)<2):
        print("Adja meg a nevét: ", end="")
        name=input()

        if(len(name)<2):
            print("Nem jó nevet adott meg")
    return name.capitalize().strip()
        
