# This code still needs improvement, it only shows the advantages
# of using a GUI

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("250x300")
win.title("Tips Calculator")
win.resizable(0,0)


def show_total():
    """Calculates and displays into the GUI the total value to pay"""
    if tip_cost.get() == "No tip":
        total_label.configure(text= "The total bill is {}".format(entry_value.get()))
    else:
        entry1_value = int(entry_value.get()) # turn entry into an integer
        tip_value = int(tip_cost.get()) / 100
        
        def show_total_calc():
            total = entry1_value + (entry1_value * tip_value)
            total_label.configure(text= "The total bill is {}".format(total))
        
        if tip_value == 0.05:
            show_total_calc()

        elif tip_value == 0.10:
            show_total_calc()

        elif tip_value == 0.15:
            show_total_calc()

    
label1 = ttk.Label(win, text = "Tip Calculator", font = ("arial", "15", "bold"))
label1.pack(padx= "20", pady = "20")

label2 = ttk.Label(win, text= "Enter the cost of the bill:")
label2.pack()

entry_value = tk.StringVar()
entry = ttk.Entry(win, width = "8", textvariable = entry_value)
entry.pack()

label3 = ttk.Label(win, text ="Select percentage of tip:")
label3.pack(pady = 10)

tip_cost = tk.StringVar()
tip_value = ttk.Combobox(win, state = "readonly", textvariable = tip_cost)
tip_value['values'] = ("No tip", "5", "10", "15")
tip_value.current(1)
tip_value.pack()

calc_button = tk.Button(win, text = "CALCULATE BILL", width = "20", 
                        bg = "red", fg = "white", command = show_total)
calc_button.pack(padx = "20", pady = "20")

total_label = ttk.Label(win, text = "", font = ("arial", "14"))
total_label.pack()


win.mainloop()
