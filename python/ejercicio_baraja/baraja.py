from carta import Cartas
import random
class Baraja:
    
    tipo = 'fransesa'
    pintas = ["♣","♠","♥","♦"]
    palos = ['2','3','4','5','6','7','8','9','10','J','Q','K','As']
    cartas = []
    
    def __init__(self):
        for pinta in self.pintas:
            for palo in self.palos:
                self.cartas.append(Cartas(pinta,palo))
    
    
#    def sacar_cartas(self):
#        cartas_sacadas = random.sample(self.cartas, 2)
#        for carta in cartas_sacadas:
#        print(f"{carta.palo}{carta.pinta}") 

    def sacar_cartas(self):
        cartas1 = random.choice(self.cartas)
        print('La carta aleatorea 1 es: ', cartas1.palo,cartas1.pinta)
        cartas2 = random.choice(self.cartas)
        while (cartas2 == cartas1):
            cartas2 = random.choice(self.cartas)
        print('La carta aleatorea 2 es: ', cartas2.palo,cartas2.pinta)
            
baraja_francesa = Baraja()
print(baraja_francesa.tipo)

for baraja in baraja_francesa.cartas:
    print(baraja.palo + baraja.pinta, end=' ')
print('\n')
print('------------------------')
print('Cartas sacadas al Azar')
baraja_francesa.sacar_cartas()