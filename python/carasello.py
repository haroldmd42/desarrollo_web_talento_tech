from turtle import *
import random
import tkinter as tk
from tkinter import simpledialog

class Juego_ppt:
    valores = ['Piedra', 'Papel', 'Tijera']

    def __init__(self, eleccion):
        self.eleccion = eleccion
        setup(750, 850, 0, 0)
        screensize(700, 700)
        title('Piedra papel o tijera')

    def dibujar_papel(self, ancho, alto):
        penup()
        goto(100, alto // 2)  # Ajuste de posición para dibujar papel a la derecha
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
        end_fill()

    def dibujar_piedra(self):
        pencolor("green")
        pensize(5)
        penup()
        goto(-100, 75)  # Ajuste de posición para dibujar piedra a la izquierda
        pendown()
        begin_fill()
        for _ in range(8):
            forward(100)
            right(45)
        end_fill()

    def dibujar_tijera(self):
        pensize(8)
        pencolor('red')
        penup()
        goto(100, 0)  # Ajuste de posición para dibujar tijera a la derecha
        pendown()
        circle(20, 360)
        penup()
        goto(150, 0)  # Ajuste de posición para dibujar tijera a la derecha
        pendown()
        circle(20, 360)
        penup()
        goto(100, 0)  # Ajuste de posición para dibujar tijera a la derecha
        pendown()
        goto(100, 90)
        penup()
        goto(100, 0)
        pendown()
        goto(150, 90)

    def generar_aleatorio(self):
        return random.choice(self.valores)

    def resultado(self, user_choice, machine_choice):
        if user_choice == machine_choice:
            return "Empate"
        elif (user_choice == "Piedra" and machine_choice == "Tijera") or \
             (user_choice == "Papel" and machine_choice == "Piedra") or \
             (user_choice == "Tijera" and machine_choice == "Papel"):
            return "Usuario Gana"
        else:
            return "Máquina Gana"

    def mostrar_resultado(self, user_choice, machine_choice, resultado):
        texto = Turtle()
        texto.penup()
        texto.hideturtle()

        # Mostrar elección del usuario
        texto.goto(-200, 150)
        texto.write(f"Usuario elige: {user_choice}", font=("Arial", 14, "bold"))

        # Mostrar elección de la máquina
        texto.goto(200, 150)
        texto.write(f"Máquina elige: {machine_choice}", font=("Arial", 14, "bold"))

        # Mostrar resultado
        texto.goto(0, 100)
        texto.write(f"Resultado: {resultado}", font=("Arial", 14, "bold"))

# Configuración de la ventana para el input
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Pedir la elección al usuario
eleccion = simpledialog.askstring("Entrada", 'Elige: Para Piedra escribe 1, Para Papel escribe 2 y Para Tijera escribe 3:')
opciones = ['Piedra', 'Papel', 'Tijera']
user_choice = opciones[int(eleccion) - 1] if eleccion and eleccion.isdigit() and 1 <= int(eleccion) <= 3 else None

if user_choice is None:
    print("Elección inválida. Por favor, reinicia el juego.")
else:
    juego = Juego_ppt(user_choice)
    machine_choice = juego.generar_aleatorio()
    resultado = juego.resultado(user_choice, machine_choice)

    # Imprimir en consola las elecciones y el resultado
    print(f"Usuario elige: {user_choice}")
    print(f"Máquina elige: {machine_choice}")
    print(f"Resultado: {resultado}")

    # Dibujar elección del usuario
    if user_choice == 'Piedra':
        juego.dibujar_piedra()
    elif user_choice == 'Papel':
        juego.dibujar_papel(200, 300)
    elif user_choice == 'Tijera':
        juego.dibujar_tijera()

    # Dibujar elección de la máquina
    if machine_choice == 'Piedra':
        juego.dibujar_piedra()
    elif machine_choice == 'Papel':
        juego.dibujar_papel(200, 300)  # Llamada a la misma función, pero ajustando la posición
    elif machine_choice == 'Tijera':
        juego.dibujar_tijera()

    # Mostrar el resultado en pantalla con Turtle
    juego.mostrar_resultado(user_choice, machine_choice, resultado)

done()
