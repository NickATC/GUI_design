# Simple GUI with:
    # Label
    # Entry
    # Button

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Personal Title")
window.geometry("400x500")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

# Label
label1 = ttk.Label(window, text = "Enter your username:")
label1.pack()

# Entry


# Button



window.mainloop()
