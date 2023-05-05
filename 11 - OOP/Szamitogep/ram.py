
class Ram:
    def __init__(self, gyarto:str, modell:str, kapacitas:int=0, mennyiseg:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.kapacitas:int=kapacitas
        self.mennyiseg:int=mennyiseg
    def __str__(self)->str:
        return f"RAM: {self.gyarto} {self.modell} {self.kapacitas}GB {self.mennyiseg}db szlot\n"

#3 objektumot 2 egyszerű 1 összetett