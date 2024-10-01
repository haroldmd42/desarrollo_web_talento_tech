#Integrantes
#Alexander Arroyo Ceballos
#Juan Felipe Córdoba 
#Kevin Carrillo
#Yan Harold Muñoz Dominguez
#Juan Fernandez

from turtle import *
import random

class Juego_ppt:
    valores = ['Piedra', 'Papel', 'Tijera']
    lanzamiento = ""

    def __init__(self):
        setup(750, 450, 0, 0)
        screensize(700, 350)
        title('Piedra, Papel o Tijera')

    def dibujar_papel(self, x, y):
        penup()
        goto(x, y)
        pendown()
        fillcolor("white")
        pencolor("blue")
        begin_fill()
        for _ in range(2):
            forward(100)
            right(90)
            forward(150)
            right(90)
        end_fill()
        penup()
        goto(x + 15, y + 30)
        write("Papel", False, "left", ("Arial", 16, "normal"))

    def dibujar_piedra(self, x, y):
        penup()
        goto(x, y + 120)
        write("Piedra", font=("Arial", 14, "bold"))
        pencolor("green")
        pensize(5)
        penup()
        goto(x - 50, y + 75)
        pendown()
        goto(x + 50, y + 75)
        goto(x + 75, y + 50)
        goto(x + 75, y - 50)
        goto(x + 50, y - 75)
        goto(x - 50, y - 75)
        goto(x - 75, y - 50)
        goto(x - 75, y + 50)
        goto(x - 50, y + 75)
        penup()
        goto(x - 50, y + 75)
        pendown()
        goto(x - 50, y - 75)
        penup()
        goto(x + 40, y + 60)
        pendown()
        goto(x - 40, y + 60)
        penup()
        goto(x + 60, y + 60)
        pendown()
        goto(x - 60, y + 60)
        penup()
        goto(x + 50, y + 75)
        pendown()
        goto(x + 50, y - 75)
        penup() 
    def dibujar_tijera(self, x, y):
        penup()
        goto(x, y)
        pendown()
        pencolor("red")
        pensize(5)
        circle(20, 360)
        penup()
        goto(x + 50, y)
        pendown()
        circle(20, 360)
        penup()
        goto(x + 25, y)
        pendown()
        goto(x + 25, y + 90)
        penup()
        goto(x + 25, y)
        pendown()
        goto(x + 75, y + 90)
        penup()
        goto(x + 25, y + 90)
        write("Tijera", False, "left", ("Arial", 16, "normal"))

    def generar_aleatorio(self):
        val = random.choice(self.valores)
        self.lanzamiento = val
        return val

    def resultado(self, eleccion):
        goto(0, -200)
        if eleccion == self.lanzamiento:
            write("¡Empate!", False, "center", ("Arial", 24, "normal"))
        elif (eleccion == "Piedra" and self.lanzamiento == "Tijera") or \
             (eleccion == "Papel" and self.lanzamiento == "Piedra") or \
             (eleccion == "Tijera" and self.lanzamiento == "Papel"):
            write("¡Usuario Gana!", False, "center", ("Arial", 24, "normal"))
        else:
            write("¡Máquina Gana!", False, "center", ("Arial", 24, "normal"))


eleccion = textinput("Elige", "Elige: Piedra, Papel o Tijera").capitalize()

if eleccion in ['Piedra', 'Papel', 'Tijera']:
    juego = Juego_ppt()
    juego.dibujar_piedra(-200, 0) if eleccion == 'Piedra' else \
    juego.dibujar_papel(-200, 0) if eleccion == 'Papel' else \
    juego.dibujar_tijera(-200, -100)

    maquina = juego.generar_aleatorio()
    juego.dibujar_piedra(200, 0) if maquina == 'Piedra' else \
    juego.dibujar_papel(200, 0) if maquina == 'Papel' else \
    juego.dibujar_tijera(200, -100)

    juego.resultado(eleccion)
else:
    print("Elección inválida. Por favor, reinicia el juego.")

done()
