
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Bindings Excercise")
window.geometry('250x200')
window.resizable(0,0)
window.wm_iconbitmap('images/ok.ico')

def color_yellow():
    btn.configure(background = "yellow")
    lbl2.configure(text = "Left click")

def color_blue(event):
    btn.configure(background = "blue")
    lbl2.configure(text = "Middle click")

def color_red(event):
    btn.configure(background = "red")
    lbl2.configure(text = "Right click")


lbl = ttk.Label(window, text = "Use left, middle or right click:")
lbl.pack(pady = 10)

btn = tk.Button(window, text = "Click here (Left/Middle/Right)", command = color_yellow)
btn.bind("<Button-2>", color_blue)
btn.bind("<Button-3>", color_red)
btn.pack(pady = 20)

lbl2 = ttk.Label(window, text = "Click you are using!")
lbl2.pack()


window.mainloop()
