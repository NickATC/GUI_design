
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

lbl_frame = ttk.LabelFrame(window, text = "Rango de edad")
lbl_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

hom_radio = ttk.Radiobutton(lbl_frame, text = "10-30 años", value = 1)
hom_radio.grid(row = 1, column = 1, sticky = "W")
muj_radio = ttk.Radiobutton(lbl_frame, text = "31-45 años", value = 2)
muj_radio.grid(row = 2, column = 1, sticky = "W")
otro_radio = ttk.Radiobutton(lbl_frame, text = "+46", value = 3)
otro_radio.grid(row = 3, column = 1, sticky = "W")
no_radio = ttk.Radiobutton(lbl_frame, text = "No deseo especificar", value = 4)
no_radio.grid(row = 4, column = 1, sticky = "W")

lbl_frame2 = ttk.LabelFrame(window, text = "OS más usado:")
lbl_frame2.grid(row = 1, column = 1, padx = 20, pady = 10)

os_var = tk.StringVar()
os_combo = ttk.Combobox(lbl_frame2, textvariable = os_var, width = 15)
os_combo['values'] = ("Windows", "iOS", "Linux", "Otro")
os_combo.grid(row = 0, column = 0, padx = 20, pady = 10)

label2 = ttk.Label(lbl_frame2, text = "Otro:")
label2.grid(row = 1, column = 0, sticky = "w")

otro_entry = ttk.Entry(lbl_frame2, width = 15)
otro_entry.grid(row = 2, column = 0, pady = 5)


btn = ttk.Button(window, text = "Enviar")
btn.grid(row = 12, column = 0, pady = 20, columnspan = 2)


window.mainloop()
