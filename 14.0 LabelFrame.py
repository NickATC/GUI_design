# Simple GUI to explain LabelFrame

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("LabelFrame Example")
window.geometry("300x250")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")


label1 = ttk.Label(window, text = "This is label is IN window")
label1.pack(pady = 20)

lab_frame = ttk.LabelFrame(window, text = "This is a LABELFRAME.  I'm in window")
lab_frame.pack()

btn1 = ttk.Button(lab_frame, text = "I'm inside LabelFrame :)")
btn1.pack(pady = 30)

label2 = tk.Label(window, text = "I'm inside window, packed after the LabelFrame", 
                        font = ('arial', '10', 'italic'), foreground = 'red')
label2.pack(pady = 30)


window.mainloop()
