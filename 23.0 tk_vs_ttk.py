import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext


window = tk.Tk()
window.title("Widget Look")
window.geometry("400x570")
window.wm_iconbitmap("images/ok.ico")



####  A LabelFrame with only tk widgets <-- observe!  is tk.... just one 't': tk
tk_lbl_frame = tk.LabelFrame(window, text = "only tk widgets :")
tk_lbl_frame.grid(row = 0, column = 0, padx = 20, pady = 25)

tk_lbl1 = tk.Label(tk_lbl_frame, text = "This is a tk Label")
tk_lbl1.pack(pady = 10)

tk_btn = tk.Button(tk_lbl_frame, text = "This is a tk Button")
tk_btn.pack(pady = 20, padx = 20)

tk_entry = tk.Entry(tk_lbl_frame, width = 15)
tk_entry.pack(pady = 25)

tk_lbl2 = tk.Label(tk_lbl_frame, text = "Here goes the ListBox widget")
tk_lbl2.pack(pady = 20)

tk_spin = tk.Spinbox(tk_lbl_frame, width = 15)
tk_spin.pack(pady = 20)

tk_text = tk.Text(tk_lbl_frame, width = 15, height = 2)
tk_text.pack(pady = 30)

tk_check1 = tk.Checkbutton(tk_lbl_frame, text = "tk Checkbutton")
tk_check1.pack()
tk_check2 = tk.Checkbutton(tk_lbl_frame, text = "another tk Check")
tk_check2.pack()

tk_radio = tk.Radiobutton(tk_lbl_frame, text = "tk Radiobutton")
tk_radio.pack(pady = 20)



####  A LabelFrame with only ttk widgets <-- observe!  is ttk... double 't':  ttk
ttk_lbl_frame = ttk.LabelFrame(window, text = "only ttk widgets :")
ttk_lbl_frame.grid(row = 0, column = 1, padx = 20, pady = 20)

ttk_lbl1 = ttk.Label(ttk_lbl_frame, text = "This is a ttk Label")
ttk_lbl1.pack(pady = 10)

ttk_btn = ttk.Button(ttk_lbl_frame, text = "This is a ttk Button")
ttk_btn.pack(pady = 25, padx = 20)

ttk_entry = ttk.Entry(ttk_lbl_frame, width = 15)
ttk_entry.pack(pady = 20)

ttk_combo = ttk.Combobox(ttk_lbl_frame, width = 15)
ttk_combo.pack(pady = 20)

ttk_spin = ttk.Spinbox(ttk_lbl_frame, width = 15)
ttk_spin.pack(pady = 20)

ttk_scrtxt = scrolledtext.ScrolledText(ttk_lbl_frame, width = 15, height = 1)
ttk_scrtxt.pack(pady = 20)

option1_var = tk.StringVar()
ttk_check1 = ttk.Checkbutton(ttk_lbl_frame, text = "ttk Checkbutton", variable = option1_var)
ttk_check1.pack()

option2_var = tk.StringVar()
ttk_check2 = ttk.Checkbutton(ttk_lbl_frame, text = "another ttk Check", variable = option2_var)
ttk_check2.pack()

ttk_radio = ttk.Radiobutton(ttk_lbl_frame, text = "ttk Radiobutton")
ttk_radio.pack(pady = 20)



window.mainloop()
