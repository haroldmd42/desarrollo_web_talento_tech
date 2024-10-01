from turtle import *
import random

class Juego_ppt:
    valores = ['Piedra','Papel', 'Tijera']
    
    def __init__(self, eleccion):
        self.eleccion = eleccion
        setup(750, 850, 0, 0)
        screensize(700, 700)
        title('Piedra papel o tijera')
    
    def dibujar_papel(self,ancho, alto):
        penup()
        goto(-ancho//2, alto//2)  
        pendown()
        pencolor("blue")
        fillcolor("white")
        pensize(3)
        begin_fill()
        for _ in range(2):
            forward(ancho)
            right(90)
            forward(alto)
            right(90)
            pencolor("blue")
        end_fill()

        penup()
        goto(-ancho//2 + 10, alto//2 - 40)  
        pencolor("gray")
        pensize(1)
        
        for i in range(10):  
            pendown()
            forward(ancho - 20)
            penup()
            backward(ancho - 20)
            right(90)
            forward(20) 
            left(90)
    
    def dibujar_piedra(self):
        texto = Turtle()
        texto.penup()
        texto.hideturtle()
        texto.goto(-100, 120)
        texto.write("El usuario elige piedra", font=("Arial", 14, "bold"))
        piedra = Turtle()
        piedra.color("green")
        piedra.pensize(5)
        piedra.penup()
        piedra.goto(-50, 75)
        piedra.pendown()
        piedra.goto(50, 75)
        piedra.goto(75, 50)
        piedra.goto(75, -50)
        piedra.goto(50, -75)
        piedra.goto(-50, -75)
        piedra.goto(-75, -50)
        piedra.goto(-75, 50)
        piedra.goto(-50, 75)
        piedra.penup()
        piedra.goto(-50, 75)
        piedra.pendown()
        piedra.goto(-50, -75)
        piedra.penup()
        piedra.goto(40, 60)
        piedra.pendown()
        piedra.goto(-40, 60) 
        piedra.penup()
        piedra.goto(60, 60)  # Movemos el punto inicial hacia abajo (y = 40)
        piedra.pendown()
        piedra.goto(-60, 60) 
        piedra.penup()
        piedra.goto(50, 75)
        piedra.pendown()
        piedra.goto(50, -75)
        piedra.hideturtle()
        pantalla.mainloop()

    def dibujar_tijera(self):
        pensize(8)
        pencolor('red')

        circle(20, 360)
        penup()
        goto(50, 0)
        pendown()
        circle(20, 360)
        goto(0, 90)
        penup()
        goto(0,0)
        pendown()
        goto(50,90)
        hideturtle()
    
    def generar_aleatorio(self):   
        return random.choice(self.valores)
    
    
    
    def resultado(self):
        user_choice = self.eleccion
        machine_choice = self.generar_aleatorio
        if user_choice == machine_choice:
            return "Empate"
        elif (user_choice == 1 and machine_choice == 3) or (user_choice == 2 and machine_choice == 1) or (user_choice == 3 and machine_choice == 2):
            return "Usuario Gana"
        else:
            return "Máquina Gana"
            
    

juego_1 = Juego_ppt('Papel')
eleccion = input('Elige','Para Piedra escribe 1,Para Papel escribe 2 y para Tijera escribe 3')
##juego_1.dibujar_papel(300,300)
#juego_1.dibujar_piedra()
juego_1.dibujar_tijera()
done()