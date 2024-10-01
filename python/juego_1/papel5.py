from turtle import *

setup(500, 500)
bgcolor("lightgray")
title("Papel Ejecutivo - Piedra, Papel o Tijera")


def dibujar_papel_ejecutivo(ancho, alto):
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

dibujar_papel_ejecutivo(300, 300)
hideturtle()
done()