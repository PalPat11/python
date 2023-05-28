class Chips:
    def __init__(self, marka:str, fajta:str, kaloria:int, zsirok:int):
        super().__init__()
        self.marka:str=marka
        self.fajta:str=fajta
        self.kaloria:int=kaloria
        self.zsirok:int=zsirok

    def __str__(self) -> str:
        return f"{self.marka} {self.fajta}:\n Kalória: {self.kaloria}\n Zsírok: {self.zsirok}"

        