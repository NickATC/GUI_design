# Simple GUI with:
    # Label
    # Spinbox with 5 options
    # Button

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Personal Title")
window.geometry("300x200")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

def get_spinbox_info():
    print(spin_var.get())

#Label to guide user:
label1 = ttk.Label(window, text = "Select your current OS:")
label1.pack(pady = 10)

# Spinbox
spin_var = tk.StringVar()
spinbox1 = ttk.Spinbox(window, width = 15, textvariable = spin_var)
spinbox1["values"] = ("Windows", "iOS", "Linux", "Android", "Other")
spinbox1.pack()

# Button to extract information
ok_button = ttk.Button(window, text = "Get info!", command = get_spinbox_info)
ok_button.pack(pady = 50)


window.mainloop()
