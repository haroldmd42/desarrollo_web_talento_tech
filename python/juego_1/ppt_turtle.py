from turtle import *

class Ppt:
    def __init__(self):
        setup(500, 500, 0, 0)
        screensize(300, 150)
        title("Juego Piedra papel o Tijera")

    def dibujar_piedra(self):
        penup()
        goto(0+x, 120)
        write("El usuario elige piedra", False, "center", ("Arial", 20, "normal"))
        color("green")
        pensize(5)
        penup()
        goto(-50, 70)
        pendown()
        goto(-60, 60)
        goto(-40, 50)
        goto(-50, 70)
        goto(50,70)
        goto(40,50)
        goto(60,60)
        goto(50,70)
        penup()
        goto(-40,50)
        pendown()
        goto(40,50)
        goto(40,-40)
        goto(50,-60)
        goto(60,-50)
        goto(40,-40)
        goto(-40,-40)
        goto(-60,-50)
        goto(-50,-60)
        goto(-40,-40)
        goto(-40,50)
        penup()
        goto(-60,60)
        pendown()
        goto(-60,-50)
        penup()
        goto(-50,-60)
        pendown()
        goto(50,-60)
        penup()
        goto(60,-50)
        pendown()
        goto(60,60)

    def dibujar_papel(self):
        penup()
        goto(0, 120)
        write("El usuario elige papel", False, "center", ("Arial", 20, "normal"))
        color("blue")
        pensize(5)
        penup()
        goto(30, 70)
        pendown()
        goto(30,40)
        goto(60, 40)
        goto(30,70)
        goto(-60,70)
        goto(-60,-60)
        goto(60,-60)
        goto(60,40)
        hideturtle()

    def dibujar_tijera(self):
        penup()
        goto(0, 120)
        write("El usuario elige tijera", False, "center", ("Arial", 20, "normal"))
        color("red")
        pensize(5)
        penup()
        goto(-30, 70)
        pendown()
        goto(30, -50)
        circle(30)
        penup()
        goto(30, 70)
        pendown()
        goto(-30,-50)
        circle(30)
        hideturtle()


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

# Configuración del input
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

