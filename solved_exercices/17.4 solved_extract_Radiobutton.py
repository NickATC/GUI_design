# Simple GUI with:
    # Label
    # Radiobutton with 4 options
    # Button

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Personal Title")
window.geometry("300x300")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

#Label to guide user:
label1 = ttk.Label(window, text = "Select your OS:")
label1.pack(pady = 10, anchor = 'w')


def get_radio_info():
    print(radio_var.get())


# Radiobuttons
radio_var = tk.StringVar()
option1 = ttk.Radiobutton(window, text = "Windows", value = "Windows", variable = radio_var)
option1.pack(anchor = 'w')

option2 = ttk.Radiobutton(window, text = "iOS", value = "iOS", variable = radio_var)
option2.pack(anchor = 'w')

option3 = ttk.Radiobutton(window, text = "Linux", value = "Linux", variable = radio_var)
option3.pack(anchor = 'w')

option4 = ttk.Radiobutton(window, text = "Other", value = "Other", variable = radio_var)
option4.pack(anchor = 'w')


#Button to continue.
ok_button = ttk.Button(window, text = "Next", command = get_radio_info)
ok_button.pack(pady = 10)



window.mainloop()
