# Notebooks can be confusing and tricky, but add a professional look, don't you think so?
# Analize the notes and read the hierarchy map.
# Play with options... try changing the parent in the label and the button.
# option expland = 1 will expand to fill the whole window
# option fill = 'both' will fill the window

import tkinter as tk
from tkinter import ttk

window = tk.Tk()                     # This is the only parent so far...  The whole window!
window.geometry("300x400")
window.title("NoteBook example")
window.resizable(width = False, height = False)

#Create a Notebook
main_notebook = ttk.Notebook(window)    # I create a NoteBook (this is the parent)
window_tab1 = ttk.Frame(main_notebook)   # Now I create a Frame INSIDE the NoteBook (Now the parent is 'window_tab1')
main_notebook.add(window_tab1, text = "Tab 1")   # I add the tab, and name it
main_notebook.pack(expand = 1, fill = "both", padx = 30, pady = 30)   # I make it visible and fill the window
                                  
#A label inside tab1
label1 = ttk.Label(window_tab1, text = "I'm a LABEL inside Tab 1")
label1.pack(pady = 20)


#Create another Notebook
window_tab2 = ttk.Frame(main_notebook)
main_notebook.add(window_tab2, text = "Tab 2")
main_notebook.pack(expand = 1, fill = "both")

#A button inside tab1
button = ttk.Button(window_tab2, text = "I'm a BUTTON inside Tab 2")
button.pack(pady = 20)


# This is the Hierarchy.  I bit complicated, I know!
# window
#     main_notebook
#         window_tab1
#               INSIDE window_tab1 I can put any widgets I need!                
#         window_tab2
#               INSIDE window_tab2 I can put any widgets I need!

#   If I need, I can add widgets INSIDE 'window', but outside 'main_notebook'

window.mainloop()
