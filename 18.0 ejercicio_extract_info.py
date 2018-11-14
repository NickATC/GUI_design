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


# Entry
entry1 = ttk.Entry(window, width = 20)
entry1.pack(pady = 10)

# 2 Radiobuttons
radio_unique_var = tk.StringVar()
radio_opt = ttk.Radiobutton(window, text = "Black?", value = 1, variable = radio_unique_var)
radio_opt.pack()

radio_opt = ttk.Radiobutton(window, text = "Or White", value = 2, variable = radio_unique_var)
radio_opt.pack()

# 1 Checkbutton
check_var = tk.StringVar()
check_opt = ttk.Checkbutton(window, text = "Spam?", variable = check_var)
check_opt.pack(pady = 10)

# 1 Spinbox
spinbox1 = ttk.Spinbox(window, width = 15)
spinbox1["values"] = ("Spinbox 1", "Spinbox 2", "Spinbox 3", "Spinbox 4")
spinbox1.pack(pady = 10)

# Combobox
combo_var = tk.StringVar()
combo = ttk.Combobox(window, width = 20)
combo['values'] = ("Select:", "Combo 1", "Combo 2", "Combo 3", "Combo 4",)
combo.current(0)
combo.pack(pady = 20)

# Scrolled Text
scr = scrolledtext.ScrolledText(window, width = 25, height = 3, wrap = tk.WORD)
scr.pack()


btn1 = ttk.Button(window, text = "Extract info")
btn1.pack(pady = 30)


window.mainloop()
