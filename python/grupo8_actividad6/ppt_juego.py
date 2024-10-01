
#Integrantes
#Alexander Arroyo Ceballos
#Juan Felipe Córdoba 
#Kevin Carrillo
#Yan Harold Muñoz Dominguez
#Juan Fernandez
from turtle import *
import random

class Juego_ppt:
    def __init__(self):
        setup(800, 600, 0, 0)
        screensize(500, 400)
        title("Juego Piedra Papel o Tijera")
        self.valores = ['Piedra', 'Papel', 'Tijera']
        self.tortuga_usuario = Turtle()
        self.tortuga_maquina = Turtle()
        self.tortuga_resultado = Turtle()

    def dibujar_piedra(self, turtle, x, y):
        turtle.clear()
        turtle.penup()
        turtle.goto(x, y + 120)
        turtle.write("Elige Piedra", False, "center", ("Arial", 20, "normal"))
        turtle.color("green")
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(x - 50, y + 70)
        turtle.pendown()
        turtle.goto(x - 60, y + 60)
        turtle.goto(x - 40, y + 50)
        turtle.goto(x - 50, y + 70)
        turtle.goto(x + 50, y + 70)
        turtle.goto(x + 40, y + 50)
        turtle.goto(x + 60, y + 60)
        turtle.goto(x + 50, y + 70)
        turtle.penup()
        turtle.goto(x - 40, y + 50)
        turtle.pendown()
        turtle.goto(x + 40, y + 50)
        turtle.goto(x + 40, y - 40)
        turtle.goto(x + 50, y - 60)
        turtle.goto(x + 60, y - 50)
        turtle.goto(x + 40, y - 40)
        turtle.goto(x - 40, y - 40)
        turtle.goto(x - 60, y - 50)
        turtle.goto(x - 50, y - 60)
        turtle.goto(x - 40, y - 40)
        turtle.goto(x - 40, y + 50)
        turtle.penup()
        turtle.goto(x - 60, y + 60)
        turtle.pendown()
        turtle.goto(x - 60, y - 50)
        turtle.penup()
        turtle.goto(x - 50, y - 60)
        turtle.pendown()
        turtle.goto(x + 50, y - 60)
        turtle.penup()
        turtle.goto(x + 60, y - 50)
        turtle.pendown()
        turtle.goto(x + 60, y + 60)
        turtle.hideturtle()

    def dibujar_papel(self, turtle, x, y):
        turtle.clear()
        turtle.penup()
        turtle.goto(x, y + 120)
        turtle.write("Elige Papel", False, "center", ("Arial", 20, "normal"))
        turtle.color("blue")
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(x + 30, y + 70)
        turtle.pendown()
        turtle.goto(x + 30, y + 40)
        turtle.goto(x + 60, y + 40)
        turtle.goto(x + 30, y + 70)
        turtle.goto(x - 60, y + 70)
        turtle.goto(x - 60, y - 60)
        turtle.goto(x + 60, y - 60)
        turtle.goto(x + 60, y + 40)
        turtle.hideturtle()

    def dibujar_tijera(self, turtle, x, y):
        turtle.clear()
        turtle.penup()
        turtle.goto(x, y + 120)
        turtle.write("Elige Tijera", False, "center", ("Arial", 20, "normal"))
        turtle.color("red")
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(x - 30, y + 70)
        turtle.pendown()
        turtle.goto(x + 30, y - 50)
        turtle.circle(30)
        turtle.penup()
        turtle.goto(x + 30, y + 70)
        turtle.pendown()
        turtle.goto(x - 30, y - 50)
        turtle.circle(30)
        turtle.hideturtle()

    def generar_aleatorio(self):
        val = random.choice(self.valores)
        self.lanzamiento = val
        return val

    def resultado(self, eleccion):
        self.tortuga_resultado.clear()
        self.tortuga_resultado.penup()
        self.tortuga_resultado.goto(0, -200)
        self.tortuga_resultado.pendown()
        if eleccion == self.lanzamiento:
            self.tortuga_resultado.write("¡Empate!", False, "center", ("Arial", 24, "normal"))
        elif (eleccion == "Piedra" and self.lanzamiento == "Tijera") or \
             (eleccion == "Papel" and self.lanzamiento == "Piedra") or \
             (eleccion == "Tijera" and self.lanzamiento == "Papel"):
            self.tortuga_resultado.write("¡Usuario Gana!", False, "center", ("Arial", 24, "normal"))
        else:
            self.tortuga_resultado.write("¡Máquina Gana!", False, "center", ("Arial", 24, "normal"))


eleccion = textinput("Elige", "Elige: Piedra, Papel o Tijera").capitalize()

if eleccion in ['Piedra', 'Papel', 'Tijera']:
    juego = Juego_ppt()
    if eleccion == 'Piedra':
        juego.dibujar_piedra(juego.tortuga_usuario, -200, 0)
    elif eleccion == 'Papel':
        juego.dibujar_papel(juego.tortuga_usuario, -200, 0)
    else:
        juego.dibujar_tijera(juego.tortuga_usuario, -200, 0)
    maquina = juego.generar_aleatorio()
    if maquina == 'Piedra':
        juego.dibujar_piedra(juego.tortuga_maquina, 200, 0)
    elif maquina == 'Papel':
        juego.dibujar_papel(juego.tortuga_maquina, 200, 0)
    else:
        juego.dibujar_tijera(juego.tortuga_maquina, 200, 0)
    juego.resultado(eleccion)
else:
    print("Elección inválida. Por favor, reinicia el juego.")

done()
