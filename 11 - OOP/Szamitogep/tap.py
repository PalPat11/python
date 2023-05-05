class Tapegyseg:
    def __init__(self, gyarto:str, modell:str, fogyasztas:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.fogyasztas:int=fogyasztas
    def __str__(self)->str:
        return f"Tapegység: {self.gyarto} {self.modell} {self.fogyasztas} Watt\n"