#Small program showing all the 11 Widgets:
#   3 Containers:   
		# Frame
		# LabelFrame
		# Notebook
#	8 widgets:
		# Label
		# Button
		# Entry
		# RadioButton
		# Checkbox
		# Combobox
		# Spinbox
		# Scrolledtext

# Also showing Menu and a popup message box on the ABOUT option.

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg


def about_msg():
	"""Function to show the 'about' pop up""" # Don't forget to import MESSAGEBOX to use it
	msg.showinfo("Python message info Box", "All 11 Widgets By Nicolás Táutiva ")


win = tk.Tk()
win.geometry("500x660")
win.title("See all the 11 Widgets")
win.wm_iconbitmap('images/ok.ico')
win.resizable(width = False, height = False)

#Create a Notebook
tab_control = ttk.Notebook(win)
window = ttk.Frame(tab_control)
tab_control.add(window, text = "Tab 1")
tab_control.pack(expand = 1, fill = "both")

label1 = ttk.Label(window, text = "I'm a LABEL inside Tab 1, but out of LabelFrame")
label1.grid(row = 0, column = 0, pady = "15")

#Let's create a LabelFrame inside window, that is, inside Tab 1
label_frame = ttk.LabelFrame(window, text = "I'm a LABELFRAME")
label_frame.grid(row = 1, column = 0, padx = 30)

#Let's put something inside LabelFrame in Tab 1:

#########  8 Widgets  #########
#1 Label
label2 = ttk.Label(label_frame, text = "Check the 8 widgets:          I'm a LABEL inside the LabelFrame.")
label2.grid(row = 0, column = 0, pady = 30, columnspan = 2)

label_button = ttk.Label(label_frame, text = "To my right there is a BUTTON:  -->")
label_button.grid(row = 1, column = 0)

#2 Button
button1 = ttk.Button(label_frame, text = "I'm a BUTTON")
button1.grid(row = 1, column = 1, sticky = "W")

label_entry = ttk.Label(label_frame, text = "To my right there is an ENTRY:  -->")
label_entry.grid(row = 2, column = 0, pady = 20)

#3 Entry
entry1 = ttk.Entry(label_frame, width = 20)
entry1.grid(row = 2, column = 1, sticky = "W")

radio_label = ttk.Label(label_frame, text = "To my right there is a RADIOBUTTON:  -->")
radio_label.grid(row = 3, column = 0)

#4 Radiobutton
radio_variable = tk.IntVar()
option1 = ttk.Radiobutton(label_frame, text = "You pick me...", variable = radio_variable, value = 1)
option1.grid(row = 3, column = 1, pady = 10, sticky = "W")

option2 = ttk.Radiobutton(label_frame, text = "...or me...But not both!", variable = radio_variable, value = 2)
option2.grid(row = 4, column = 1, pady = 10, sticky = "W")

check_label = ttk.Label(label_frame, text = "CHECKBUTTON. Select as many as you want -->")
check_label.grid(row = 5, column = 0)

#5 Checkbutton
option1_var = tk.StringVar()
check = ttk.Checkbutton(label_frame, text = "Select me !", variable = option1_var)
check.grid(row = 5, column = 1, sticky = "W")

option2_var = tk.StringVar()
check2 = ttk.Checkbutton(label_frame, text = "Select me too!", variable = option2_var)
check2.grid(row = 6, column = 1, sticky = "W")

option3_var = tk.StringVar()
check3 = ttk.Checkbutton(label_frame, text = "I also want to participate !!", variable = option3_var)
check3.grid(row = 7, column = 1, sticky = "W")

option4_var = tk.StringVar()
check4 = ttk.Checkbutton(label_frame, text = "Check us all at the same time!", variable = option4_var)
check4.grid(row = 8, column = 1, sticky = "W")

combo_label = ttk.Label(label_frame, text = "To the right you'll find a COMBOBOX -->")
combo_label.grid(row = 9, column = 0, pady = 20)

#6 Combobox
combo_value = tk.StringVar()
combo = ttk.Combobox(label_frame)
combo["values"] = ("One option here", "Another one", "Yet another", "You get the idea, right?")
combo.grid(row = 9, column = 1, sticky = "W")

spin_label = ttk.Label(label_frame, text = "Now a nice looking SPINBOX :) -->")
spin_label.grid(row = 10, column = 0, pady = 20)

#7 Spinbox
spinbox1 = ttk.Spinbox(label_frame, width = 15)
spinbox1["values"] = (1, 2, "Also letters", 3, "More letters", "Cool, ha?")
spinbox1.grid(row = 10, column = 1, sticky = "W")

scrol_label = ttk.Label(label_frame, text = "Please write on the SCROLLEDTEXT -->")
scrol_label.grid(row = 11, column = 0, pady = 20)

#8 ScrolledText...DON'T forget to import 
scrol_text = scrolledtext.ScrolledText(label_frame, width = 20, height = 2, wrap = tk.WORD)
scrol_text.grid(row = 11, column = 1)


#Create a manu and add items
menu_bar = Menu(win)
win.config(menu = menu_bar)

file_menu = Menu(menu_bar, tearoff = 0)  
menu_bar.add_cascade(label = "A menu", menu = file_menu)
file_menu.add_command(label = "One option here")
file_menu.add_command(label = "yeah... another one")

help_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Another menu", menu = help_menu)
help_menu.add_command(label = "Option 1")
help_menu.add_command(label = "Option 2")
help_menu.add_command(label = "About.  Click here!", command = about_msg) # Function about_msg


#Create another Notebook
window2 = ttk.Frame(tab_control)
tab_control.add(window2, text = "Tab 2")
tab_control.pack(expand = 1, fill = "both")

#Let's practice.  Here is a label.
label1 = ttk.Label(window2, text = "A sad and lonely LABEL on Tab 2...")
label1.pack()

# Add another Label ... label5

# Add a Button ... button5 using ttk

# Add a Button ... button6 using tk  See the difference?

# Add an Entry ... entry5



win.mainloop()