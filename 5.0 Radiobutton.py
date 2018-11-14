# Simple GUI with:
    # Label
    # Radiobutton with 4 options
    # Button

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Personal Title")
window.geometry("300x300")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

#Label to guide user:
label1 = ttk.Label(window, text = "Select your current OS:")
label1.pack()

# Radiobuttons
option1 = ttk.Radiobutton(window, text = "Windows", value = 1)
option1.pack()


# Button

window.mainloop()
