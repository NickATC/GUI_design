import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as msg 

window = tk.Tk()
window.title("MessageBox Examples")
window.geometry("300x400")
window.wm_iconbitmap("images/ok.ico")


#### Ask questions ####
def ask_ok_cancel():
    ok_cancel = msg.askokcancel("askokcancel", "This is an askokcancel")
    print(ok_cancel)

def ask_question():
    question = msg.askquestion("askquestion", "This is an askquestion")
    print(question)

def ask_retry_cancel():
    retry = msg.askretrycancel("askretrycancel", "This is an askretrycancel")
    print(retry)

def ask_yes_no():
    yes_no = msg.askyesno("askyesno", "This is an askyesno")
    print(yes_no)

#### Show messages ####
def show_error():
    error = msg.showerror("Error!", "This is a showerror")
    print(error)

def show_info():
    msg.showinfo("Info!", "This is a showinfo")
 
def show_warning():
    msg.showwarning("Warning!", "This is a showwarning")
    

################
####  GUI ######
label1 = ttk.Label(window, text = "Click to see the 4 Ask MessageBoxes:")
label1.pack(pady = 20)

btn1 = ttk.Button(window, text = ".askokcancel", command = ask_ok_cancel)
btn1.pack(pady = 5)

btn2 = ttk.Button(window, text = ".askquestion", command = ask_question)
btn2.pack(pady = 5)

btn3 = ttk.Button(window, text = ".askretrycancel", command = ask_retry_cancel)
btn3.pack(pady = 5)

btn4 = ttk.Button(window, text = ".askyesno", command = ask_yes_no)
btn4.pack(pady = 5)

lbl2 = ttk.Label(window, text = "Click to see the 3 Show MessageBoxes")
lbl2.pack(pady = 20)

btn5 = ttk.Button(window, text = ".showerror", command = show_error)
btn5.pack(pady = 5)

btn6 = ttk.Button(window, text = ".showinfo", command = show_info)
btn6.pack(pady = 5)

btn7 = ttk.Button(window, text = ".showwarning", command = show_warning)
btn7.pack(pady = 5)


window.mainloop()
