import turtle
import random

# Crear la pantalla
screen = turtle.Screen()
screen.title("Piedra, Papel o Tijera")
import turtle
import random

# Crear la pantalla
screen = turtle.Screen()
screen.title("Piedra, Papel o Tijera")
screen.bgcolor("white")

# Crear la tortuga para dibujar
drawer = turtle.Turtle()
drawer.hideturtle()

# Tortuga para dibujar el borde azul del papel
paper_drawer = turtle.Turtle()
paper_drawer.hideturtle()
paper_drawer.pensize(5)
paper_drawer.pencolor("blue")

# Opciones del juego
options = ["Piedra", "Papel", "Tijera"]

# Función para dibujar opciones en pantalla
def draw_choice(x, y, text, user_choice=None):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.write(text, align="center", font=("Arial", 16, "bold"))
    
    # Si la selección es "papel", dibujar el borde azul del papel 30 píxeles debajo del texto (20 original + 10 adicionales)
    if user_choice == 2:  # Opción 2 es "Papel"
        draw_paper(x, y +150)  # Subir el dibujo 10 píxeles más

# Función para dibujar el borde azul del papel
def draw_paper(x, y):
    paper_drawer.penup()
    paper_drawer.goto(x - 150, y - 150)  # Empezar desde la esquina superior izquierda
    paper_drawer.pendown()
    
    # Dibujar el rectángulo de 300x300 píxeles
    for _ in range(4):
        paper_drawer.forward(300)
        paper_drawer.right(90)

# Función para mostrar la selección del usuario y de la máquina
def show_choices(user_choice, machine_choice):
    drawer.clear()
    paper_drawer.clear()  # Limpiar el dibujo previo del papel
    draw_choice(-150, 200, f"Usuario: {options[user_choice - 1]}", user_choice)
    draw_choice(150, 200, f"Máquina: {options[machine_choice - 1]}", machine_choice)

# Función para determinar el ganador
def determine_winner(user_choice, machine_choice):
    if user_choice == machine_choice:
        return "Empate"
    elif (user_choice == 1 and machine_choice == 3) or (user_choice == 2 and machine_choice == 1) or (user_choice == 3 and machine_choice == 2):
        return "Usuario Gana"
    else:
        return "Máquina Gana"

# Función que controla el juego
def play_game(user_choice):
    machine_choice = random.randint(1, 3)
    show_choices(user_choice, machine_choice)
    winner = determine_winner(user_choice, machine_choice)
    
    # Verificar si el usuario o la máquina seleccionaron "papel" y si papel es el ganador
    if user_choice == 2 and winner == "Usuario Gana":
        draw_choice(-150, -130, "Resultado: Usuario Gana")  # Subir 10 píxeles más el texto debajo del papel del usuario
    elif machine_choice == 2 and winner == "Máquina Gana":
        draw_choice(200, -130,"Resultado: Máquina Gana")  # Subir 10 píxeles más el texto debajo del papel de la máquina
    else:
        draw_choice(0, -130, f"Resultado: {winner}")  # Dibujar el resultado en el centro

# Configuración para capturar la selección del usuario con Turtle
def piedra():
    play_game(1)

def papel():
    play_game(2)

def tijera():
    play_game(3)

# Configurar botones en la pantalla para las opciones
screen.listen()
screen.onkey(piedra, "1")  # Seleccionar Piedra
screen.onkey(papel, "2")   # Seleccionar Papel
screen.onkey(tijera, "3")  # Seleccionar Tijera

# Mostrar instrucciones centradas en la parte superior
drawer.penup()
drawer.goto(0, 250)
drawer.write("Presiona 1 para Piedra, 2 para Papel, 3 para Tijera", align="center", font=("Arial", 16, "bold"))

# Mantener la ventana abierta
screen.mainloop()
import turtle
import random

# Crear la pantalla
screen = turtle.Screen()
screen.title("Piedra, Papel o Tijera")
screen.bgcolor("white")

# Crear la tortuga para dibujar
drawer = turtle.Turtle()
drawer.hideturtle()

# Tortuga para dibujar el borde azul del papel
paper_drawer = turtle.Turtle()
paper_drawer.hideturtle()
paper_drawer.pensize(5)
paper_drawer.pencolor("blue")

# Opciones del juego
options = ["Piedra", "Papel", "Tijera"]

# Función para dibujar opciones en pantalla
def draw_choice(x, y, text, user_choice=None):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.write(text, align="center", font=("Arial", 16, "bold"))
    
    # Si la selección es "papel", dibujar el borde azul del papel 30 píxeles debajo del texto (20 original + 10 adicionales)
    if user_choice == 2:  # Opción 2 es "Papel"
        draw_paper(x, y + 150)  # Subir el dibujo 10 píxeles más

# Función para dibujar el borde azul del papel con pliegue
def draw_paper(x, y):
    paper_drawer.penup()
    paper_drawer.goto(x - 150, y - 150)  # Empezar desde la esquina superior izquierda
    paper_drawer.pendown()
    
    # Dibujar el rectángulo de 300x300 píxeles
    for _ in range(3):
        paper_drawer.forward(300)
        paper_drawer.right(90)
    
    # Dibujar la parte inferior con pliegue
    paper_drawer.forward(250)  # Línea hasta el comienzo del pliegue
    paper_drawer.goto(x + 150, y + 150)  # Dibujar el pliegue (triángulo interno)
    paper_drawer.goto(x + 150, y)  # Volver al borde

# Función para mostrar la selección del usuario y de la máquina
def show_choices(user_choice, machine_choice):
    drawer.clear()
    paper_drawer.clear()  # Limpiar el dibujo previo del papel
    draw_choice(-150, 200, f"Usuario: {options[user_choice - 1]}", user_choice)
    draw_choice(150, 200, f"Máquina: {options[machine_choice - 1]}", machine_choice)

# Función para determinar el ganador
def determine_winner(user_choice, machine_choice):
    if user_choice == machine_choice:
        return "Empate"
    elif (user_choice == 1 and machine_choice == 3) or (user_choice == 2 and machine_choice == 1) or (user_choice == 3 and machine_choice == 2):
        return "Usuario Gana"
    else:
        return "Máquina Gana"

# Función que controla el juego
def play_game(user_choice):
    machine_choice = random.randint(1, 3)
    show_choices(user_choice, machine_choice)
    winner = determine_winner(user_choice, machine_choice)
    
    # Verificar si el usuario o la máquina seleccionaron "papel" y si papel es el ganador
    if user_choice == 2 and winner == "Usuario Gana":
        draw_choice(-150, -130, "Resultado: Usuario Gana")  # Subir 10 píxeles más el texto debajo del papel del usuario
    elif machine_choice == 2 and winner == "Máquina Gana":
        draw_choice(200, -130,"Resultado: Máquina Gana")  # Subir 10 píxeles más el texto debajo del papel de la máquina
    else:
        draw_choice(0, -130, f"Resultado: {winner}")  # Dibujar el resultado en el centro

# Configuración para capturar la selección del usuario con Turtle
def piedra():
    play_game(1)

def papel():
    play_game(2)

def tijera():
    play_game(3)

# Configurar botones en la pantalla para las opciones
screen.listen()
screen.onkey(piedra, "1")  # Seleccionar Piedra
screen.onkey(papel, "2")   # Seleccionar Papel
screen.onkey(tijera, "3")  # Seleccionar Tijera

# Mostrar instrucciones centradas en la parte superior
drawer.penup()
drawer.goto(0, 250)
drawer.write("Presiona 1 para Piedra, 2 para Papel, 3 para Tijera", align="center", font=("Arial", 16, "bold"))

# Mantener la ventana abierta
screen.mainloop()
