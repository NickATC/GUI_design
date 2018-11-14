import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox as msg

window = tk.Tk()
window.title("Personal Information")
window.resizable(0,0)
window.geometry("280x200")
window.wm_iconbitmap("images/human.ico")


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
    value = user_var.get()
    print("Data entered!")
    if len(value) > 7:
        user_var.set(value[:7])
        #user_var.set("Too long!") # Uncomment to set a specific value.  Comment line above first!

def check_data():
    if len(user_entry.get()) > 7:
        msg.showerror("Error", "Your username is too long.  Use maximum 7 characters.")
    else:
        print("Username ok")
        #Continue with the rest of entries!


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

id_entry = ttk.Entry(window, width = 20)
id_entry.grid(column = 1, row = 1)

tel_lbl = ttk.Label(window, text = "Telephone Number:")
tel_lbl.grid(column = 0, row = 2, pady = 10, padx = 10)

tel_entry = ttk.Entry(window, width = 20)
tel_entry.grid(column = 1, row = 2)

save_btn = tk.Button(window, text = "Save Info", bg = "red", fg = "white", command = check_data)
save_btn.place(x = 110, y = 140)
###   END OF GUI   ###
######################

# Adding help/tooltips:
create_ToolTip(user_entry, 'Use maximum 7 characters.')


window.mainloop()
