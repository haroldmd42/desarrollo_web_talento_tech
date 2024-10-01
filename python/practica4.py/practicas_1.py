from turtle import *

setup(450, 200, 0, 0)
screensize(300, 300)
title('Calculadore IMC')

peso = numinput('Peso', 'Ingrese el peso en kilogramos: ',1,1,200)
estatura = numinput('Estatura', 'Ingrese la estaruta en centimetros: ',1,1,2)

imc = peso / (estatura*estatura)
hideturtle()
penup()
goto(200,10)
pendown()
if(imc <= 18.5):
    write('El peso es inferior al normal',False,'right',('Arial', 24,'normal'))
elif(imc > 18.5 and imc <= 24.9 ):
    write('El peso es normal',False,'right',('Arial', 24,'normal'))
    
done()