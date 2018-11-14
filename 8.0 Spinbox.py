# Simple GUI with:
    # Label
    # Spinbox with 5 options
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
label1.pack(pady = 10)

# Spinbox

#Button to continue.  It does not work... yet!


window.mainloop()
