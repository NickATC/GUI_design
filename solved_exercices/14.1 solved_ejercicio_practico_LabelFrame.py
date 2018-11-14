# Simple GUI to explain LabelFrame

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("LabelFrame Example")
window.geometry("300x250")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")


lab_frame = ttk.LabelFrame(window, text = "Personal information:")
lab_frame.pack(pady = 20)

name = ttk.Label(lab_frame, text = "Full name:")
name.grid(column = 0, row = 0, padx = 10, pady = 20)

entry_name = ttk.Entry(lab_frame)
entry_name.grid(column = 1, row = 0, padx = 20)

etc = ttk.Label(lab_frame, text = "Other widgets here...")
etc.grid(column = 0, row = 2)

btn = ttk.Button(window, text = "Send info")
btn.pack(pady = 30)

window.mainloop()
