

import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Editing Info")
window.geometry('220x200')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')

def button_action():
    lbl1.configure(text = "Button pressed!")
    lbl2.configure(text = entry1_value.get())
    btn.configure(bg = "yellow")
    

lbl1 = ttk.Label(window, text = "Enter something here:")
lbl1.pack(pady = 10)

entry1_value = tk.StringVar()
entry1 = ttk.Entry(window, textvariable = entry1_value)
entry1.pack()

btn = tk.Button(window, text = "Click to do some magic!", command = button_action)
btn.pack(pady = 20)

lbl2 = ttk.Label(window, text = "Your text here!")
lbl2.pack()


window.mainloop()
