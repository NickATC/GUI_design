# Simple GUI with:
    # Label
    # Checkbutton with 4 options
    # Button

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Personal Title")
window.geometry("300x300")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

#Label to guide user:
label1 = ttk.Label(window, text = "Which OS have you used?")
label1.pack()

#Checkbuttons
option1_var = tk.StringVar()
check = ttk.Checkbutton(window, text = "Windows", variable = option1_var)
check.pack()

# Button

window.mainloop()
