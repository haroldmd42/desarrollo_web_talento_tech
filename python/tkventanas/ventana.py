#Yan Harold Muñoz Dominguez - 1087647650
from tkinter import *

ventana = Tk()
ventana.title("CLASE LUNES")
ventana.geometry("500x300")
ventana.resizable(0,0)
ventana.iconbitmap("tkventanas/icono.ico")
color_fondo = "#fcf3cf"
ventana.config(bg= color_fondo,relief='groove',bd = 10, cursor='dotbox')

def suma():
    num1 = int(dato1.get())
    num2 = int(dato2.get())
    resultado = num1+num2
    return variables.set(resultado)
def multiplicar():
    num1 = int(dato1.get())
    num2 = int(dato2.get())
    resultado = num1*num2
    return variables.set(resultado)
def dividir():
    num1 = int(dato1.get())
    num2 = int(dato2.get())
    resultado = num1/num2
    return variables.set(resultado)
def restar():
    num1 = int(dato1.get())
    num2 = int(dato2.get())
    resultado = num1-num2
    return variables.set(resultado)

variables = StringVar()
titulo = Label(ventana, text ="Súper calculadora científica", bg=color_fondo, font=("Rockwell Extra Bold",12),fg="#34495e")
titulo1 = Label(ventana, text ="Número 1", bg=color_fondo, font=("Verdana",12),fg="#34495e")
titulo3 = Label(ventana, text ="Número 2", bg=color_fondo, font=("Verdana",12),fg="#34495e")
boton = Button(ventana,text='Sum', command=suma)
boton1 = Button(ventana,text='Mul', command=multiplicar)
boton2 = Button(ventana,text='Res', command=restar)
boton3 = Button(ventana,text='Div', command=dividir)
dato1 = Entry(ventana)
dato2 = Entry(ventana)
resultado = Entry(ventana, textvariable=variables)
titulo.grid(row=0,column=0)
titulo1.grid(row=1,column=0)
dato1.grid(row=1, column=1)
titulo3.grid(row=2,column=0)
dato2.grid(row=2,column=1)
boton.grid(row=3, column=1)
boton1.grid(row=3, column=2)
boton2.grid(row=4, column=1)
boton3.grid(row=4, column=2)
resultado.grid(row=5, column=1)

imagen1 = PhotoImage(file='tkventanas/tierra.gif')
imgcuad = Label(ventana, image=imagen1)
imgcuad.grid(row=8, column=0)
ventana.mainloop()