
class Processor:
    def __init__(self, gyarto:str, modell:str, szalak:int=0, magok:int=0 ):
        super().__init__()
        self.szalak:int=szalak
        self.magok:int=magok
        self.gyarto:str=gyarto
        self.modell:str=modell
    def __str__(self)->str:
        return f" Processzor: {self.gyarto} {self.modell} {self.szalak} szál {self.magok} mag\n"