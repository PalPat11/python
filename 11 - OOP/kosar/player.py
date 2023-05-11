class Player:
    def __init__(self, nev:str, szarmazas:str,  kor:int, dobasok:int):
        super().__init__()
        self.nev:str=nev
        self.szarmazas:str=szarmazas
        self.kor:int=kor
        self.dobasok:int=dobasok
    
    def __str__(self) -> str:
        return f"{self.nev}: Kor: {self.kor} Származás: {self.szarmazas} Dobások száma: {self.dobasok}"
        