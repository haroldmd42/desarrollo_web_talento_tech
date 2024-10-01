class Bingo:
    
    def __init__(self,letra_balota, numero_balota):
        self.letra_balota = letra_balota
        self.numero_balota = numero_balota
    
    def __str__(self):
        return f'{self.letra_balota}-{self.numero_balota}'