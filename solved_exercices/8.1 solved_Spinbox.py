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
spin_value = tk.StringVar()
spinbox1 = ttk.Spinbox(window, width = 15, textvariable = spin_value)
spinbox1["values"] = ("Windows", "iOS", "Linux", "Android", "Other")
spinbox1.pack()

#Button to continue.  It does not work... yet!
ok_button = ttk.Button(window, text = "Next")
ok_button.pack(pady = 50)


window.mainloop()
