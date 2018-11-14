import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("LogIn")
window.geometry('280x150')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')


label1 = ttk.Label(window, text = "User :")
label1.grid(row = 0, column = 0, pady = 10)

user_entry = ttk.Entry(window)
user_entry.grid(row = 0, column = 1)

label2 = ttk.Label(window, text = "Password :")
label2.grid(row = 1, column = 0, pady = 10)

pass_entry = ttk.Entry(window)   # Use this option:    show = "*"
pass_entry.grid(row = 1, column = 1)

login_button = ttk.Button(window, text = "Log In !")
login_button.grid(row = 3, column = 0, padx = 30, pady = 20)

cancel_button = ttk.Button(window, text = "Cancel")
cancel_button.grid(row = 3, column = 1)


window.mainloop()
