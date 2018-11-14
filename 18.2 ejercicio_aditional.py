# Agregue la funcionalidad para que el texto ingresado en el entry
# se copie en el ScrolledText

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


window = tk.Tk()
window.title("Connecting GUI")
window.geometry('220x300')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')


lbl = ttk.Label(window, text = "Enter something here:")
lbl.pack(pady = 10)

entry1_value = tk.StringVar()
entry1 = ttk.Entry(window, textvariable = entry1_value)
entry1.pack()

btn1 = tk.Button(window, text = "Click to insert text :")
btn1.pack(pady = 20)

lbl2 = ttk.Label(window, text = "Your text here:")
lbl2.pack()

scrol = scrolledtext.ScrolledText(window, width = 20, height = 3)
scrol.pack()

btn2 = tk.Button(window, text = "Delete text!")
btn2.pack(pady = 20)


window.mainloop()
