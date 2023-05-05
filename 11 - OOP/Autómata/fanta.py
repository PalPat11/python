class Fanta:
    def __init__(self, energy:str, zsir:float, ch:float, feherje:float, salt:float):
        super().__init__()
        self.energy:str=energy
        self.zsir:float=zsir
        self.ch:float=ch
        self.feherje:float=feherje
        self.salt:float=salt
    def __str__(self) -> str:
        return f"Fanta: \n    Energia :{self.energy}\n    Zsírok: {self.zsir}g\n    Szénhidrát: {self.ch}g\n    Fehérje: {self.feherje}g"
    

        