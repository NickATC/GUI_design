# Excercise to extract the information from:
    #   An Entry
    #   2 radiobuttons
    #   1 checkbutton 
    #   The spinbox 
    #   The combobox 
    #   and an Scrolledtext


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Extracting Info")
window.geometry('270x400')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')


def extract_info():
    print(entry_var.get())
    print(radio_unique_var.get())
    print(check_var.get())
    print(spin_var.get())
    print(combo_var.get())
    print(scr.get(1.0, tk.END))

# Entry
entry_var = tk.StringVar()
entry1 = ttk.Entry(window, width = 20, textvariable = entry_var)
entry1.pack(pady = 10)

# 2 Radiobuttons
radio_unique_var = tk.StringVar()
radio_opt = ttk.Radiobutton(window, text = "Black?", value = "Black", variable = radio_unique_var)
radio_opt.pack()

radio_opt = ttk.Radiobutton(window, text = "Or White", value = "White", variable = radio_unique_var)
radio_opt.pack()

# 1 Checkbutton
check_var = tk.StringVar()
check_opt = ttk.Checkbutton(window, text = "Spam?", variable = check_var, onvalue = "Spam", offvalue = "No Spam")
check_opt.pack(pady = 10)

# 1 Spinbox
spin_var = tk.StringVar()
spinbox1 = ttk.Spinbox(window, width = 15, textvariable = spin_var)
spinbox1["values"] = ("Spinbox 1", "Spinbox 2", "Spinbox 3", "Spinbox 4")
spinbox1.pack(pady = 10)

# Combobox
combo_var = tk.StringVar()
combo = ttk.Combobox(window, width = 20, textvariable = combo_var)
combo['values'] = ("Select:", "Combo 1", "Combo 2", "Combo 3", "Combo 4",)
combo.current(0)
combo.pack(pady = 20)

# Scrolled Text
scr = scrolledtext.ScrolledText(window, width = 25, height = 3, wrap = tk.WORD)
scr.pack()

btn1 = ttk.Button(window, text = "Extract info", command = extract_info)
btn1.pack(pady = 30)


window.mainloop()
