import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Sign In")
window.geometry('300x150')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')

name_label = ttk.Label(window, text = "Username")
name_label.place(x = 10, y = 20)

# Entry


# Button



window.mainloop()
