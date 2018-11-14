# Simple GUI with:
    # Label
    # Scrolledtext
    # Button

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("My Personal Title")
window.geometry("300x300")
window.resizable(0,0)
window.wm_iconbitmap("images/ok.ico")

#Label to guide user:
label1 = ttk.Label(window, text = "Write your opinion about this workshop:")
label1.pack(pady = 10)

# Scrolledtext
scrol_text = scrolledtext.ScrolledText(window, width = 20, height = 2, wrap = tk.WORD)
scrol_text.pack()

#Button to continue.  It does not work... yet!
ok_button = ttk.Button(window, text = "Next")
ok_button.pack(pady = 50)


window.mainloop()
