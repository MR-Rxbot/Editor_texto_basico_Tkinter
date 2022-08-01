from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from turtle import bgcolor


#Configuracion de la raiz

ventana = Tk()
ventana.title("El editor sublime")


#logica de las funciones

#La utilizaremos para almacenar la ruta de los ficheros
ruta = ""

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta = ""
    texto.delete(1.0, "end")
    ventana.title(ruta + " - El editor sublime")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
    initialdir = ".",
    filetypes = (("Ficheros de texto", "*.txt"),),
    title = "Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        ventana.title(ruta + " - El editor sublime")


def guardar():
    mensaje.set("Guardar Fichero")
    if ruta != "":
        contenido = texto.get(1.0,"end-1c")    
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set(" Guardar Fichero como ")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:    
        ruta = fichero.name
        contenido = texto.get(1.0,"end-1c")    
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


#Menu superior
menubar = Menu(ventana)
filmenu = Menu(menubar, tearoff=0)
filmenu.add_command(label="Nuevo",command=nuevo)
filmenu.add_command(label="Abrir",command=abrir)
filmenu.add_command(label="Guardar",command=guardar)
filmenu.add_command(label="Guardar como",command=guardar_como)
filmenu.add_separator()
filmenu.add_command(label="Salir",command=ventana.quit)
menubar.add_cascade(menu=filmenu, label="Archivo")

#Caja de texto
texto = Text(ventana)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4,font=("Arial",12))


#Ayuda inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(ventana,textvariable=mensaje, justify="left")
monitor.pack(side="left")



ventana.config(menu=menubar)
#Bucle de la aplicacion
ventana.mainloop()