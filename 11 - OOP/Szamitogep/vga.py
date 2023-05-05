class GraphicsCard:
    def __init__(self, gyarto:str, modell:str, vram:int=0, cores:int=0):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.vram:int=vram
        self.cores:int=cores
    def __str__(self)->str:
        return f"Videókártya: {self.gyarto} {self.modell} {self.vram}GB {self.cores} Core\n"