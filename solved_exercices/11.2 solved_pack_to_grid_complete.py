# Solución a Convierta esta GUI de pack() a grid()
# Esta solución incluye todos los padding, columnspan, etc

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Sign In")
window.wm_iconbitmap('images/human.ico')


label1 = ttk.Label(window, text = "Ingrese Usuario:")
label1.grid(row = 0, column = 0, pady = 20)

user_entry = ttk.Entry(window)
user_entry.grid(row = 0, column = 1)


label3 = ttk.Label(window, text = "Rango de edad:")
label3.grid(row = 1, column = 0)

hom_radio = ttk.Radiobutton(window, text = "10-30 años", value = 1)
hom_radio.grid(row = 1, column = 1, sticky = "W")
muj_radio = ttk.Radiobutton(window, text = "31-45 años", value = 2)
muj_radio.grid(row = 2, column = 1, sticky = "W")
otro_radio = ttk.Radiobutton(window, text = "+46", value = 3)
otro_radio.grid(row = 3, column = 1, sticky = "W")
no_radio = ttk.Radiobutton(window, text = "No deseo especificar", value = 4)
no_radio.grid(row = 4, column = 1, sticky = "W")

label4 = ttk.Label(window, text = "Sistema operativo que más usa al programar")
label4.grid(row = 5, column = 0, columnspan = 2, pady = 10)

os_var = tk.StringVar()
os_combo = ttk.Combobox(window, textvariable = os_var)
os_combo['values'] = ("Windows", "iOS", "Linux", "Otro")
os_combo.grid(row = 6, column = 1, pady = 10)


label6 = ttk.Label(window, text = "Lenguajes que domina")
label6.grid(row = 7, column = 0)

lan1_var = tk.StringVar()
lan1 = ttk.Checkbutton(window, text = "C", variable = lan1_var)
lan1.grid(row = 7, column = 1, sticky = "W")

lan2_var = tk.StringVar()
lan2 = ttk.Checkbutton(window, text = "Python", variable = lan2_var)
lan2.grid(row = 8, column = 1, sticky = "W")

lan3_var = tk.StringVar()
lan3 = ttk.Checkbutton(window, text = "JavaScript", variable = lan3_var)
lan3.grid(row = 9, column = 1, sticky = "W")


label6 = ttk.Label(window, text = "Por que desea ingresar a nuestro programa")
label6.grid(row = 10, column = 0, columnspan = 2, pady = 20, padx = 30)

scr = scrolledtext.ScrolledText(window, width = 30, height = 2)
scr.grid(row = 11, column = 0, columnspan = 2)


btn = ttk.Button(window, text = "Enviar")
btn.grid(row = 12, column = 0, pady = 20, columnspan = 2)


window.mainloop()
