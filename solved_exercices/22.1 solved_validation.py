import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox as msg

window = tk.Tk()
window.title("Personal Information")
window.resizable(0,0)
window.geometry("280x200")
window.wm_iconbitmap("images/human.ico")

valid_numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

class ToolTip(object):
    """Class to create tooltips to help users"""
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")      # get size of widget
        x = x + self.widget.winfo_rootx() + 25          # calculate to display tooltip 
        y = y + cy + self.widget.winfo_rooty() - 25     # above and to the right
        self.tip_window = tw = tk.Toplevel(self.widget) # create new tooltip window
        tw.wm_overrideredirect(True)                    # remove all Window Manager (wm) decorations
        #tw.wm_overrideredirect(False)                  # uncomment to see the effect
        tw.wm_geometry("+%d+%d" % (x, y))               # create window size

        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)       # create instance of class
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)   # bind mouse events
    widget.bind('<Leave>', leave)

def user_validation(*args): # validation of user_var
    user_value = user_var.get()
    if len(user_value) > 7:
        user_var.set(user_value[:7])

def id_validation(*args):
    id_value = id_var.get()[-1] #Checks last character on user entry
    print(id_value) # Just to check last character on user entry
    if id_value not in valid_numbers: #if last item is not a number (line 11):
        id_var.set(id_var.get()[:-1])  #delete last character from the full entry
   
def tel_validation(*args):
    tel_value = tel_var.get()[-1]
    print(tel_value) # Just to check last character on telephone entry
    if tel_value not in valid_numbers or len(tel_var.get()) > 10 :
        tel_var.set(tel_var.get()[:-1])
        
def check_data():
    if len(user_entry.get()) <= 1 or len(id_entry.get()) <= 1 or len(tel_entry.get()) <= 1:
        msg.showerror("Error", "There are errors in your data.  One or more entries are empty.")
    else:
        msg.showinfo("Success", "Information is correct...something will happen now...")


###############
###   GUI   ###
user_lbl = ttk.Label(window, text = "Username:")
user_lbl.grid(column = 0, row = 0, pady = 10, padx = 10)

user_var = tk.StringVar()
user_entry = ttk.Entry(window, width = 20, textvariable = user_var)
user_entry.grid(column = 1, row = 0)
user_var.trace('w', user_validation) # To monitor/trace changes to the entry widget!

id_lbl = ttk.Label(window, text = "ID Number:")
id_lbl.grid(column = 0, row = 1, pady = 10, padx = 10)

id_var = tk.StringVar()
id_entry = ttk.Entry(window, width = 20, textvariable = id_var)
id_entry.grid(column = 1, row = 1)
id_var.trace("w", id_validation)

tel_lbl = ttk.Label(window, text = "Telephone Number:")
tel_lbl.grid(column = 0, row = 2, pady = 10, padx = 10)

tel_var= tk.StringVar()
tel_entry = ttk.Entry(window, width = 20, textvariable = tel_var)
tel_entry.grid(column = 1, row = 2)
tel_var.trace("w", tel_validation)

save_btn = tk.Button(window, text = "Save Info", bg = "red", fg = "white", command = check_data)
save_btn.place(x = 110, y = 140)
###   END OF GUI   ###
######################

# Adding help/tooltips:
create_ToolTip(user_entry, 'Use maximum 7 characters.')
create_ToolTip(id_entry, 'Insert only numbers')
create_ToolTip(tel_entry, 'Use maximum 10 characters and insert only numbers.')

window.mainloop()
