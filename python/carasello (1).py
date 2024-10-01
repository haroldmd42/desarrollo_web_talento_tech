from turtle import *
import random 

class CaraSello:
    valores=["C","S"]
    lanzamiento=""

    def __init__(self):
        setup(450, 350, 0, 0)
        screensize(300,150)
        title("Cara y sello")

    def dibujar_moneda(self, radio, x, y, eleccion):
        color('red', 'yellow')
        hideturtle()
        penup()
        goto(x, y)
        pendown()
        begin_fill()
        circle(radio)
        end_fill()
        penup()
        goto(x+14, y+30)
        if eleccion:
            write(eleccion, False, "right", ("Arial", 24, "normal"))
        else:
            att=self.generar_aleatorio()
            self.lanzamiento=att
            write(att, False, "right", ("Arial", 24, "normal"))


    def generar_aleatorio(self):
        val=random.choice(self.valores)
        return(val)
    
    def resultado(self, eleccion):
        goto(80,-100)
        if (eleccion==self.lanzamiento):
            write("Ganaste", False, "right", ("Arial", 24, "normal"))
        else:
            write("Perdiste", False, "right", ("Arial", 24, "normal"))


juego=CaraSello()
eleccion=textinput("Elige","Elegir Cara: C o Sello:S")
juego.dibujar_moneda(50, -50, -50, eleccion)
juego.dibujar_moneda(50, 80, -50, None)
juego.resultado(eleccion)
done()