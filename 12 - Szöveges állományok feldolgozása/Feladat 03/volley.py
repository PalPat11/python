class Volley:
    def __init__(self):
        super().__init__()
        self.name:str=None
        self.height:int=0
        self.position:str=None
        self.nationality:str=None
        self.team:str=None
        self.country:str=None

    def __str__(self) -> str:
        return f"{self.name} {self.height} {self.position} {self.nationality} {self.team} {self.country}"
