

class Hattertar:
    def __init__(self, gyarto:str, modell:str, kapacitas:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.kapacitas:int=kapacitas
    def __str__(self)->str:
        return f"Háttértár: {self.gyarto} {self.modell} {self.kapacitas}GB \n"