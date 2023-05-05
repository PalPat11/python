class Alaplap:
    def __init__(self, gyarto:str, modell:str, vidikartyahely:str, ramszlotokSzama:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.ramszlotokSzama:int=ramszlotokSzama
        self.vidikartyahely:int=vidikartyahely
    def __str__(self)->str:
        return f"Alaplap: {self.gyarto} {self.modell} {self.ramszlotokSzama}db, videokártya szlot típusa: {self.vidikartyahely}\n"