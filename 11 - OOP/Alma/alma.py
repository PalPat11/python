class Alma:
    def __init__(self, szarmazasiHely:str, fajta:str, ch:int):
        super().__init__()
        self.szarmazasiHely:str=szarmazasiHely
        self.fajta:str=fajta
        self.ch:int=ch
    def __str__(self) -> str:
        return f""