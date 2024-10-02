from turtle import *

setup(450, 450, 0, 0)
title("Ventana de ejemplo")
screensize(300, 300)
colormode(255)

pensize(5)
fillcolor('red')
begin_fill()


goto(100, 50)
dot(10, 255, 0 ,0)
goto(100, -50)
dot(10, 0, 255,0)
goto(50, -50)
dot(10, 0, 0 ,255)
goto(0, 0)
done()