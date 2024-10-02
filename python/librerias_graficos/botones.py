import turtle

# Función que se llamará al hacer clic en el botón
def on_button_click(x, y):
    if button_x - button_width / 2 < x < button_x + button_width / 2 and button_y - button_height / 2 < y < button_y + button_height / 2:
        turtle.clear()  # Limpia la pantalla
        turtle.write("¡Botón presionado!", align="center", font=("Arial", 16, "normal"))

# Configuración de la ventana
turtle.setup(400, 400)
turtle.title("Botón con Turtle")

# Configuración del botón
button_x = -100
button_y = 50
button_width = 150
button_height = 50

# Dibuja el botón
turtle.penup()
turtle.goto(button_x, button_y - button_height / 2)
turtle.pendown()
turtle.color("lightblue")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(button_width)
    turtle.left(90)
    turtle.forward(button_height)
    turtle.left(90)
turtle.end_fill()

# Escribe el texto del botón
turtle.penup()
turtle.goto(button_x, button_y - 15)  # Ajusta la posición del texto
turtle.pendown()
turtle.color("black")
turtle.write("Presiona aquí", align="center", font=("Arial", 12, "normal"))

# Asocia el evento de clic con la función
turtle.onscreenclick(on_button_click)

# Muestra la ventana
turtle.done()
