from turtle import *

setup(450, 450, 0, 0)
screensize(300,150)
title("Tijeras ")

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


# Mantener la ventana abierta
done()
