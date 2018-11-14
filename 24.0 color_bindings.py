
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Bindings Excercise")
window.geometry('250x200')
window.resizable(0,0)
window.wm_iconbitmap('images/ok.ico')



lbl = ttk.Label(window, text = "Use left, middle or right click:")
lbl.pack(pady = 10)

btn = tk.Button(window, text = "Click here (Left/Middle/Right)")
btn.pack(pady = 20)

lbl2 = ttk.Label(window, text = "Click you are using!")
lbl2.pack()


window.mainloop()
