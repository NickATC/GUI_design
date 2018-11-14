
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Bindings")
window.geometry('220x200')
window.resizable(0,0)
window.wm_iconbitmap('images/ok.ico')
     

lbl = ttk.Label(window, text = "Enter something here:")
lbl.pack(pady = 10)

entry1_value = tk.StringVar()
entry1 = ttk.Entry(window, textvariable = entry1_value)
entry1.pack()

btn1 = tk.Button(window, text = "Click to copy / Right click to delete", background = "red")
btn1.pack(pady = 20)

lbl2 = ttk.Label(window, text = "Your text here!")
lbl2.pack()


window.mainloop()
