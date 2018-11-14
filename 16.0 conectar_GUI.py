# Excercise to connect 
    #   The 2 buttons
    #   The radiobutton
    #   The checkbutton 
    #   The spinbox 
    #   and the combobox to the corresponding function:

# To do this, use:  'command = function_name'  <-- NO PARENTHESIS in the function!
# For the combobox you need a BIND.



import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Connecting GUI")
window.geometry('220x300')
window.resizable(0,0)
window.wm_iconbitmap('images/human.ico')

def button1():
    print("You pushed button 1")
    print('\a')

def button2():
    print("yeaaaayy... this is button 2!")
    print("This is fun!")

def radio_black():
    print("You selected BLACK")

def radio_white():
    print("You selected WHITE")

def checkbutton_ok():
    print("You changed the option in the Checkbutton.")

def spin_changed():
    print("Now you are changing the spinbox!")

def combo_changed(event):
    print("You selected an option in the Combobox")


# 2 Buttons
btn1 = ttk.Button(window, text = "Button 1", command = button1)
btn1.pack(pady = 20)

btn2 = ttk.Button(window, text = "Now Button 2")
btn2.pack(pady = 10)

# 1 Radiobutton
radio_var1 = tk.StringVar()
radio_opt = ttk.Radiobutton(window, text = "Black?", value = radio_var1)
radio_opt.pack()

radio_var2 = tk.StringVar()
radio_opt = ttk.Radiobutton(window, text = "Or White", value = radio_var2)
radio_opt.pack()

# 1 Checkbutton
check_var = tk.IntVar()
check_opt = ttk.Checkbutton(window, text = "Tick me!", variable = check_var)
check_opt.pack(pady = 20)

# 1 Spinbox
spinbox1 = ttk.Spinbox(window, width = 15)
spinbox1["values"] = ("Spinbox", 2, 3, "Also letters", 4, 5, "More letters", "Cool, ha?")
spinbox1.pack()

# Combobox
combo_var = tk.StringVar()
combo = ttk.Combobox(window, width = 20)
combo['values'] = ("Select:", "Another one", "Yet another", "You get the idea, right?")
combo.current(0)
combo.pack(pady = 20)
#combo.bind("<<ComboboxSelected>>", ## Funtion_Here!! No parenthesis ##)

window.mainloop()