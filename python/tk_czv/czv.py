import os
from tkinter import Button, PhotoImage, Tk, Label, Entry, Frame, StringVar
from datetime import datetime

directorio_actual = os.path.dirname(__file__)
ruta_imagenes = os.path.join(directorio_actual, "ruta_imagenes")

ventana = Tk()
ventana.title("SIGNO DEL ZODIACO")
ventana.geometry("700x500")
ventana.resizable(0, 0)
ventana.iconbitmap(os.path.join(ruta_imagenes, "zodiaco.ico"))  # Ruta relativa para el icono
color_fondo = "#dfefff"
ventana.config(bg=color_fondo, relief='ridge', bd=20, cursor='arrow')

frame_principal = Frame(ventana, bg=color_fondo)
frame_principal.pack(fill='both', expand=True)

frame_formulario = Frame(frame_principal, bg=color_fondo)
frame_formulario.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

titulo = Label(
    frame_formulario,
    text="Conoce cuántos días has vivido hasta el día de hoy y cuál es tu signo zodiacal",
    bg=color_fondo,
    font=("Rockwell Extra Bold", 12),
    fg="#34495e",
    wraplength=300,
    justify="center"
)
titulo.pack(pady=10)

frame_nombre = Frame(frame_formulario, bg=color_fondo)
frame_nombre.pack(pady=10, anchor='w')

titulo_nombre = Label(
    frame_nombre,
    text="¿Cuál es tu nombre? ",
    bg=color_fondo,
    font=("Verdana", 10),
    fg="#34495e"
)
titulo_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")

dato_nombre = Entry(frame_nombre)
dato_nombre.grid(row=0, column=1, padx=5, pady=5)

frame_fecha_nacimiento = Frame(frame_formulario, bg=color_fondo)
frame_fecha_nacimiento.pack(pady=10, anchor='w')

titulo_fecha_nacimiento = Label(
    frame_fecha_nacimiento,
    text="Conozcamos tu fecha de nacimiento",
    bg=color_fondo,
    font=("Verdana", 10),
    fg="#34495e"
)
titulo_fecha_nacimiento.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

titulo_dia = Label(frame_fecha_nacimiento, text="Día: ", bg=color_fondo, font=("Verdana", 10), fg="#34495e")
titulo_dia.grid(row=1, column=0, padx=5, pady=5, sticky="e")
dato_dia = Entry(frame_fecha_nacimiento)
dato_dia.grid(row=1, column=1, padx=5, pady=5)

titulo_mes = Label(frame_fecha_nacimiento, text="Mes: ", bg=color_fondo, font=("Verdana", 10), fg="#34495e")
titulo_mes.grid(row=2, column=0, padx=5, pady=5, sticky="e")
dato_mes = Entry(frame_fecha_nacimiento)
dato_mes.grid(row=2, column=1, padx=5, pady=5)

titulo_ano = Label(frame_fecha_nacimiento, text="Año: ", bg=color_fondo, font=("Verdana", 10), fg="#34495e")
titulo_ano.grid(row=3, column=0, padx=5, pady=5, sticky="e")
dato_ano = Entry(frame_fecha_nacimiento)
dato_ano.grid(row=3, column=1, padx=5, pady=5)

frame_derecha = Frame(frame_principal, bg=color_fondo)
frame_derecha.grid(row=0, column=1, padx=20, pady=100, sticky="ne")

resultado_var = StringVar()
resultado_var.set("Resultado: ")

titulo_resultado = Label(
    frame_derecha,
    textvariable=resultado_var,
    bg=color_fondo,
    font=("Verdana", 10),
    fg="#34495e",
    wraplength=200
)
titulo_resultado.grid(row=1, column=0, pady=10)


imagen1 = PhotoImage(file=os.path.join(ruta_imagenes, 'default.gif'))
imgcuad = Label(frame_derecha, image=imagen1)
imgcuad.grid(row=2, column=0, pady=10)

imagenes_signos = {
    "Aries": os.path.join(ruta_imagenes, "aries.gif"),
    "Tauro": os.path.join(ruta_imagenes, "tauro.gif"),
    "Géminis": os.path.join(ruta_imagenes, "geminis.gif"),
    "Cáncer": os.path.join(ruta_imagenes, "cancer.gif"),
    "Leo": os.path.join(ruta_imagenes, "leo.gif"),
    "Virgo": os.path.join(ruta_imagenes, "virgo.gif"),
    "Libra": os.path.join(ruta_imagenes, "libra.gif"),
    "Escorpio": os.path.join(ruta_imagenes, "escorpio.gif"),
    "Sagitario": os.path.join(ruta_imagenes, "sagitario.gif"),
    "Capricornio": os.path.join(ruta_imagenes, "capricornio.gif"),
    "Acuario": os.path.join(ruta_imagenes, "acuario.gif"),
    "Piscis": os.path.join(ruta_imagenes, "piscis.gif")
}

def calcular():
    try:
        nombre = dato_nombre.get().strip()
        dia = int(dato_dia.get())
        mes = int(dato_mes.get())
        ano = int(dato_ano.get())
        fecha_nacimiento = datetime(ano, mes, dia)
        
        fecha_actual = datetime.now()
        dias_vividos = (fecha_actual - fecha_nacimiento).days

        signo = determinar_signo_zodiacal(dia, mes)

        resultado_var.set(f"Hola {nombre}, los resultados son los siguientes:\n\nDías vividos: {dias_vividos}\nSigno zodiacal: {signo}")

        imagen_signo_path = imagenes_signos.get(signo, os.path.join(ruta_imagenes, 'default.gif'))
        nueva_imagen = PhotoImage(file=imagen_signo_path)
        imgcuad.config(image=nueva_imagen)
        imgcuad.image = nueva_imagen

    except ValueError:
        resultado_var.set("Por favor, ingresa una fecha válida.")

def determinar_signo_zodiacal(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    else:
        return "Fecha inválida"

boton_calcular = Button(frame_derecha, text='Calcular', relief="groove", borderwidth=5, font=("Verdana", 10), bg='#34495e', fg="White", command=calcular)
boton_calcular.grid(row=0, column=0, pady=10)

ventana.mainloop()
