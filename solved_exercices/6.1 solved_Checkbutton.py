# Simple GUI with:
    # Label
    # Checkbutton with 4 options
    # Button

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Personal Title")
window.geometry("300x300")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

#Label to guide user:
label1 = ttk.Label(window, text = "Which OS have you used?")
label1.pack(pady = 10, anchor = 'w')

#Checkbuttons
option1_var = tk.StringVar()
check = ttk.Checkbutton(window, text = "Windows", variable = option1_var)
check.pack(anchor = 'w')

option2_var = tk.StringVar()
check2 = ttk.Checkbutton(window, text = "iOS", variable = option2_var)
check2.pack(anchor = 'w')

option3_var = tk.StringVar()
check3 = ttk.Checkbutton(window, text = "Linux", variable = option3_var)
check3.pack(anchor = 'w')

option4_var = tk.StringVar()
check4 = ttk.Checkbutton(window, text = "Android", variable = option4_var)
check4.pack(anchor = 'w')

option5_var = tk.StringVar()
check5 = ttk.Checkbutton(window, text = "Other", variable = option5_var)
check5.pack(anchor = 'w')


#Button to continue.  It does not work... yet!
ok_button = ttk.Button(window, text = "Next")
ok_button.pack(pady = 10)


window.mainloop()
