import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(3)

# Función para dibujar un triángulo equilátero
def draw_triangle(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

# Dibujar el triángulo grande
side_length = 200
t.penup()
t.goto(-side_length / 2, -side_length / (2 * (3**0.5)))
t.pendown()
draw_triangle(side_length, "white")

# Dibujar los triángulos pequeños
small_side = side_length / 2

# Triángulo inferior izquierdo
t.penup()
t.goto(-side_length / 2, -side_length / (2 * (3**0.5)))
t.pendown()
draw_triangle(small_side, "green")

# Triángulo inferior derecho
t.penup()
t.goto(0, -side_length / (2 * (3**0.5)))
t.pendown()
draw_triangle(small_side, "green")

# Triángulo superior
t.penup()
t.goto(-small_side / 2, small_side / (2 * (3**0.5)))
t.pendown()
draw_triangle(small_side, "green")

# Ocultar la tortuga y mostrar la ventana
t.hideturtle()
turtle.done()
