import random
from bingo import Bingo

class Balota(Bingo):
    def __init__(self):
        self.balotas = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
        self.generar_balotas()
        
    def generar_balotas(self):
        for i in range(1, 16):
            self.balotas['B'].append(Bingo('B', i))
        for i in range(16, 31):
            self.balotas['I'].append(Bingo('I', i))
        for i in range(31, 46):
            self.balotas['N'].append(Bingo('N', i))
        for i in range(46, 61):
            self.balotas['G'].append(Bingo('G', i))
        for i in range(61, 76):
            self.balotas['O'].append(Bingo('O', i))

    def imprimir_balotas(self):
        for fila in range(15):
            print(f"{self.balotas['B'][fila]}\t{self.balotas['I'][fila]}\t{self.balotas['N'][fila]}\t{self.balotas['G'][fila]}\t{self.balotas['O'][fila]}")

    def sacar_balota(self):
        todas_las_balotas = [balota for columna in self.balotas.values() for balota in columna]
        
        if todas_las_balotas:
            balota = random.choice(todas_las_balotas)
            for columna in self.balotas.values():
                if balota in columna:
                    columna.remove(balota)
                    break
            return balota
        else:
            return None

primer_balota = Balota()
primer_balota.imprimir_balotas()

while True:
    balota_salida = primer_balota.sacar_balota()
    if balota_salida:
        print(f'Acaba de salir la balota: {balota_salida}')
    else:
        print('Ya no quedan más balotas. NADIE GANO?')
        break
