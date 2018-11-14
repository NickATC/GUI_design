# Simple GUI with:
    # Label
    # Combobox with 5 options
    # Button

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Personal Title")
window.geometry("300x200")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

def get_combo_info():
    print(combo_var.get())

#Label to guide user:
label1 = ttk.Label(window, text = "Select your OS:")
label1.pack(pady = 10)

# Combobox
combo_var = tk.StringVar()
combo = ttk.Combobox(window, textvariable = combo_var) # (state = 'readonly') if user not allowed to write
combo["values"] = ("Windows", "iOS", "Linux", "Android", "Other")
combo.current(0)  # Selects the first item from the list
combo.pack()

# Button to extract information
ok_button = ttk.Button(window, text = "Get info!", command = get_combo_info)
ok_button.pack(pady = 50)


window.mainloop()
