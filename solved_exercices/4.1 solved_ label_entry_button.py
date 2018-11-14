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


label1 = ttk.Label(window, text = "Enter your username:")
label1.pack(pady = 10)

name_entry = ttk.Entry(window)
name_entry.pack(pady = 10)

label2 = ttk.Label(window, text = "Enter your Password:")
label2.pack(pady = 10)

pass_entry = ttk.Entry(window)
pass_entry.pack(pady = 10)

ok_button = ttk.Button(window, text = "Enter")
ok_button.pack(pady = 10)




window.mainloop()
