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


# Radiobuttons
radio_var = tk.StringVar()
option1 = ttk.Radiobutton(window, text = "Windows", value = "Windows")
option1.pack(anchor = 'w')

option2 = ttk.Radiobutton(window, text = "iOS", value = 2)
option2.pack(anchor = 'w')

option3 = ttk.Radiobutton(window, text = "Linux", value = 3)
option3.pack(anchor = 'w')

option4 = ttk.Radiobutton(window, text = "Other", value = 4)
option4.pack(anchor = 'w')


#Button to continue.  It does not work... yet!
ok_button = ttk.Button(window, text = "Next")
ok_button.pack(pady = 10)




window.mainloop()
