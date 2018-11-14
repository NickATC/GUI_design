

import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Connecting GUI")
window.geometry('220x150')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')


lbl = ttk.Label(window, text = "Enter something here:")
lbl.pack(pady = 10)

entry1 = ttk.Entry(window)
entry1.pack()

btn1 = ttk.Button(window, text = "Get info!")
btn1.pack(pady = 20)


window.mainloop()