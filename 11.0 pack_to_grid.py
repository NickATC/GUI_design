# Change the display method from pack() to grid()

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Sign In")
window.geometry('300x400')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')


label1 = ttk.Label(window, text = "Ingrese Usuario:")
label1.pack()

# Casilla de entrada
user_entry = ttk.Entry(window)
user_entry.pack()

# Rango de edad
label3 = ttk.Label(window, text = "Indique su rango de edad:")
label3.pack()

hom_radio = ttk.Radiobutton(window, text = "10-30 años", value = 1)
hom_radio.pack()
muj_radio = ttk.Radiobutton(window, text = "31-45 años", value = 2)
muj_radio.pack()
otro_radio = ttk.Radiobutton(window, text = "+46", value = 3)
otro_radio.pack()
no_radio = ttk.Radiobutton(window, text = "No deseo especificar", value = 4)
no_radio.pack()

# Sistema operativo más usado
label4 = ttk.Label(window, text = "Elija el sistema operativo que más usa al programar")
label4.pack()

os_var = tk.StringVar()
os_combo = ttk.Combobox(window, textvariable = os_var)
os_combo['values'] = ("Windows", "iOS", "Linux", "Otro")
os_combo.pack()

# Lenguajes que domina
label6 = ttk.Label(window, text = "Elija los lenguajes que más domina")
label6.pack()

lan1_var = tk.StringVar()
lan1 = ttk.Checkbutton(window, text = "C", variable = lan1_var)
lan1.pack()

lan2_var = tk.StringVar()
lan2 = ttk.Checkbutton(window, text = "Python", variable = lan2_var)
lan2.pack()

lan3_var = tk.StringVar()
lan3 = ttk.Checkbutton(window, text = "JavaScript", variable = lan3_var)
lan3.pack()

# Casilla para escribir
label6 = ttk.Label(window, text = "Por que desea ingresar a nuestro programa")
label6.pack()

scr = scrolledtext.ScrolledText(window, width = 30, height = 2)
scr.pack()

# Botón en 'Enviar'
btn = ttk.Button(window, text = "Enviar")
btn.pack()


window.mainloop()
