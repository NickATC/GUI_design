import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg


window = tk.Tk()
window.title("LogIn")
window.geometry('280x150')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')


def log_in():
    reply = msg.askquestion("Question", "Your data will be saved.  Do you want to continue?")
    if reply == "yes":
        print(user_entry_var.get())
        print(pass_entry_var.get())
    else:
        msg.showinfo("Important!", "Your data WILL NOT be saved!")
        window.destroy()


label1 = ttk.Label(window, text = "User :")
label1.grid(row = 0, column = 0, pady = 10)

user_entry_var = tk.StringVar()
user_entry = ttk.Entry(window, textvariable = user_entry_var)
user_entry.grid(row = 0, column = 1)

label2 = ttk.Label(window, text = "Password :")
label2.grid(row = 1, column = 0, pady = 10)

pass_entry_var = tk.StringVar()
pass_entry = ttk.Entry(window, show = '*', textvariable = pass_entry_var)
pass_entry.grid(row = 1, column = 1)

login_button = ttk.Button(window, text = "Log In !", command = log_in)
login_button.grid(row = 3, column = 0, padx = 30, pady = 20)

cancel_button = ttk.Button(window, text = "Cancel")
cancel_button.grid(row = 3, column = 1)


window.mainloop()
