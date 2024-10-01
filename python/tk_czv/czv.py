from tkinter import Tk, Label, Entry, Frame

ventana = Tk()
ventana.title("SIGNO DEL ZODIACO")
ventana.geometry("600x500")
ventana.resizable(0, 0)
ventana.iconbitmap("tk_czv/zodiaco.ico")
color_fondo = "#dfefff"
ventana.config(bg=color_fondo, relief='ridge', bd=20, cursor='arrow')

# Título principal
titulo = Label(
    ventana,
    text="Conoce cuántos días has vivido hasta el día de hoy y cuál es tu signo zodiacal",
    bg=color_fondo,
    font=("Rockwell Extra Bold", 12),
    fg="#34495e",
    wraplength=510,
    justify="center"
)
titulo.pack()

# Subtítulo
titulo2 = Label(
    ventana,
    text="Conozcamos tu fecha de nacimiento",
    bg=color_fondo,
    font=("Verdana", 10),
    fg="#34495e",
    wraplength=510,
    justify="left",
    anchor='w'
)
titulo2.pack(fill='x', padx=10, pady=10)

# Frame para contener las etiquetas y los campos de entrada organizados con grid()
frame_fecha = Frame(ventana, bg=color_fondo)
frame_fecha.pack(anchor='w', padx=10, pady=10)

# Etiqueta "Día"
titulo3 = Label(
    frame_fecha,
    text="Día: ",
    bg=color_fondo,
    font=("Verdana", 10),
    fg="#34495e"
)
titulo3.grid(row=0, column=0, padx=5, pady=5, sticky="e")

# Campo de entrada para "Día"
dato1 = Entry(frame_fecha)
dato1.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta "Mes"
titulo4 = Label(
    frame_fecha,
    text="Mes: ",
    bg=color_fondo,
    font=("Verdana", 10),
    fg="#34495e"
)
titulo4.grid(row=1, column=0, padx=5, pady=5, sticky="e")

# Campo de entrada para "Mes"
dato2 = Entry(frame_fecha)
dato2.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta "Año"
titulo5 = Label(
    frame_fecha,
    text="Año: ",
    bg=color_fondo,
    font=("Verdana", 10),
    fg="#34495e"
)
titulo5.grid(row=2, column=0, padx=5, pady=5, sticky="e")

# Campo de entrada para "Año"
dato3 = Entry(frame_fecha)
dato3.grid(row=2, column=1, padx=5, pady=5)

ventana.mainloop()
