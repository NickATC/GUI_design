# Ejercicio práctico 10. Use PACK():

# Hacer un formulario para que usuario haga un Sign In a nuestro programa:

# Usuario
# Rango de edad: ‘10-30’, ‘31-45’, ‘+46’, ‘No desea especificar’ (Solo uno)
# Sistema operativo más usado al programar (solo uno)
# Lenguajes de programación que domina (se pueden seleccionar varios)
# Una casilla donde se pueda escribir el motivo por el que desea ingresar a nuestro programa.
# Un botón para enviar la información


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()

label1 = ttk.Label(window, text = "Ingrese Usuario:")
label1.pack()

# Casilla de entrada

# Rango de edad

# Sistema operativo más usado

# Lenguajes que domina

# Casilla para escribir

# Botón en 'Enviar'


window.mainloop()
