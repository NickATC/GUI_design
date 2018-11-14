import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as msg
from db_manager import DBManager_sqlite
import sqlite3

window = tk.Tk()
window.title("My Phone Book")
window.wm_iconbitmap("images/phone_book.ico")
window.geometry("350x450")
window.resizable(0,0)

db_manager_sqlite = DBManager_sqlite()   #  Instance of Data Base!  Using SQLite

def update_combos():
    """This function will update both comboboxes.  No matter what tab is used."""
    t1_user_combo1.config(values = db_manager_sqlite.words)
    t3_user_combo3.config(values = db_manager_sqlite.words)

def t1_selection_changed(event):
    """This function will display contact details when the contact is
    selected on the combobox"""
    db_manager_sqlite.show_Title_account()
    t1_full_name_value = t1_full_name_var.get()
      
    all_results_clean = db_manager_sqlite.extract_db_info(t1_full_name_value)

    #assign variables to results form db
    final_full_name = all_results_clean[0]
    final_phone_number = all_results_clean[1]
    final_email = all_results_clean[2]
    final_notes = all_results_clean[3]
	
    #insert values into the Labels in Tab1 
    t1_full_name_lbl2.configure(text = final_full_name)
    t1_phone_number_lbl2.configure(text = final_phone_number)
    t1_email_lbl2.configure(text = final_email)
    t1_notes_lbl2.configure(text = final_notes)

def t2_add_entry():
    """This function will take the 4 variables from the entries and add them to the DB.
    Corresponding alert messages will guide user"""
    save_reply = msg.askyesnocancel("Confirmation", "Are you sure you want to save the information in Database?")
    if save_reply == True:
        db_manager_sqlite.insert_data(t2_full_name_var.get(), 
                                        t2_phone_number_var.get(), 
                                        t2_email_var.get(), 
                                        t2_notes_var.get()
                                        )

        t1_user_combo1.config(values = db_manager_sqlite.words)
        
        msg.showinfo("", "Information saved!")
        update_combos()
    else:
        msg.showinfo("", "Information NOT SAVED!")

def t3_selection_changed(event):
    """This function will first delete any info on the entries.  It will then
    display contact details on the entries when the contact is selected on the combobox."""
    #delete values on entries
    t3_full_name_entry3.delete(0, "end")
    t3_phone_number_entry2.delete(0, "end")
    t3_email_entry2.delete(0, "end")
    t3_notes_entry2.delete(0, "end")

    db_manager_sqlite.show_Title_account()
    t3_user_value = t3_user_var.get()
    all_results_clean = db_manager_sqlite.extract_db_info(t3_user_value)

    #assign variables to results form db
    t3_final_full_name = all_results_clean[0]
    t3_final_phone_number = all_results_clean[1]
    t3_final_email = all_results_clean[2]
    t3_final_notes = all_results_clean[3]

    # Insert them into entries so user can edit or delete them
    t3_full_name_entry3.insert(tk.INSERT, t3_final_full_name)
    t3_phone_number_entry2.insert(tk.INSERT, t3_final_phone_number)
    t3_email_entry2.insert(tk.INSERT, t3_final_email)
    t3_notes_entry2.insert(tk.INSERT, t3_final_notes)
    
def t3_delete():
    """This function will delete the contact that is currectly on the displays
    and on the the commbobox.  Alert messages will prompt the user."""
    delete_reply = msg.askyesnocancel("Confirmation", "Are you sure you want to DELETE this user?")
    if delete_reply == True:
	#Commit changes to DB
        title_value_delete = t3_user_combo3.get()
        db_manager_sqlite.delete_data(title_value_delete)

	#open new window confirming user that the info was saved!
        msg.showinfo("", "Information deleted successfully!")
        update_combos()

def t3_save_changes():
    edit_reply = msg.askyesnocancel("Confirmation", "Are you sure you want to EDIT this entry?")
    if edit_reply == True:
        # Read values directly from GUI to read possible edits from user.
        t3_full_name_edit = t3_full_name_entry3.get()
        t3_phone_number_edit = t3_phone_number_entry2.get()
        t3_email_edit  = t3_email_entry2.get()
        t3_notes_edit = t3_notes_entry2.get()

		#Commit changes to DB
        title_value_edit = t3_user_combo3.get()
        db_manager_sqlite.update_data(title_value_edit, t3_full_name_edit, t3_phone_number_edit, t3_email_edit, t3_notes_edit)

        #open new window confirming user that the info was saved!
        msg.showinfo("", "Information edited successfully!")
        update_combos()
    

#######################
######### GUI #########
# Adding an image to our GUI
header1 = tk.PhotoImage(file = 'images/big_header.gif')  # create the variable.  Use .gif format
header1_gif = tk.Label(window, image = header1)          # Add a label, instead of text, use image
header1_gif.pack()                                       # Place the label (use pack, grid or place)

#Create the Notebook where all widgets will be:
main_notebook = ttk.Notebook(window)    # I create a NoteBook (this is the parent)
window_tab1 = ttk.Frame(main_notebook)   # Now I create a Frame INSIDE the NoteBook (Now the parent is 'window_tab1')

# My phone Book tab:
main_notebook.add(window_tab1, text = "My Phone Book")   # I add the tab, and name it
main_notebook.pack(expand = 1, fill = "both", pady = 15, padx = 20)   # I make it visible and fill the window
                       
select_lbl1 = ttk.Label(window_tab1, text = "Select a name to display details:")
select_lbl1.grid(column = 0, row = 0, pady = 10)

db_manager_sqlite.show_Title_account()

t1_full_name_var = tk.StringVar()
t1_user_combo1 = ttk.Combobox(window_tab1, width = 25, textvariable = t1_full_name_var)
t1_user_combo1["values"] = db_manager_sqlite.words
t1_user_combo1.grid(column = 0, row = 1, columnspan = 2, padx = 70, pady = 15)
t1_user_combo1.bind("<<ComboboxSelected>>", t1_selection_changed)

t1_full_name_lbl1 = ttk.Label(window_tab1, text = "Full name: ")
t1_full_name_lbl1.grid(column = 0, row = 2, pady = 15)

t1_full_name_lbl2 = ttk.Label(window_tab1, text = " ", background = "white", width = 28)
t1_full_name_lbl2.grid(column = 1, row = 2)

t1_phone_number_lbl1 = ttk.Label(window_tab1, text = "Phone Number: ")
t1_phone_number_lbl1.grid(column = 0, row = 3, pady = 15)

t1_phone_number_lbl2 = ttk.Label(window_tab1, text = " ", background = "white", width = 28)
t1_phone_number_lbl2.grid(column = 1, row = 3)

t1_email_lbl1 = ttk.Label(window_tab1, text = "E-mail: ")
t1_email_lbl1.grid(column = 0, row = 4, pady = 15)

t1_email_lbl2 = ttk.Label(window_tab1, text = " ", background = "white", width = 28)
t1_email_lbl2.grid(column = 1, row = 4)

t1_notes_lbl1 = ttk.Label(window_tab1, text = "Notes: ")
t1_notes_lbl1.grid(column = 0, row = 5, pady = 15)

t1_notes_lbl2 = ttk.Label(window_tab1, text = " ", background = "white", width = 28)
t1_notes_lbl2.grid(column = 1, row = 5)


# Add info tab:
window_tab2 = ttk.Frame(main_notebook)
main_notebook.add(window_tab2, text = "Add info")
main_notebook.pack(expand = 1, fill = "both")

header2 = tk.PhotoImage(file = 'images/header2.gif')
header2_gif = tk.Label(window_tab2, image = header2)
header2_gif.grid(column = 0, row = 0, columnspan = 2)

t2_select_lbl2 = ttk.Label(window_tab2, text = "Enter information to create a new contact :")
t2_select_lbl2.grid(column = 0, row = 1, columnspan = 2, pady = 20, sticky = 'w')

t2_full_name_lbl2 = ttk.Label(window_tab2, text = "Full name: ")
t2_full_name_lbl2.grid(column = 0, row = 2)

t2_full_name_var = tk.StringVar()
t2_full_name_entry2 = ttk.Entry(window_tab2, width = 25, textvariable = t2_full_name_var)
t2_full_name_entry2.grid(column = 1, row = 2, pady = 10)

t2_phone_number_lbl2 = ttk.Label(window_tab2, text = "Phone Number: ")
t2_phone_number_lbl2.grid(column = 0, row = 3)

t2_phone_number_var = tk.StringVar()
t2_phone_number_entry2 = ttk.Entry(window_tab2, width = 25, textvariable = t2_phone_number_var)
t2_phone_number_entry2.grid(column = 1, row = 3, pady = 10)

t2_email_lbl2 = ttk.Label(window_tab2, text = "E-mail: ")
t2_email_lbl2.grid(column = 0, row = 4)

t2_email_var = tk.StringVar()
t2_email_entry2 = ttk.Entry(window_tab2, width = 25, textvariable = t2_email_var)
t2_email_entry2.grid(column = 1, row = 4, pady = 10)

t2_notes_lbl2 = ttk.Label(window_tab2, text = "Notes: ")
t2_notes_lbl2.grid(column = 0, row = 5, pady = 10)

t2_notes_var = tk.StringVar()
t2_notes_entry2 = ttk.Entry(window_tab2, width = 25, textvariable = t2_notes_var)
t2_notes_entry2.grid(column = 1, row = 5)

t2_save_btn = tk.Button(window_tab2, text = "Save!", 
        bg = "red", fg = "white", font = ("arial", "12"), command = t2_add_entry)
t2_save_btn.grid(column = 0, row = 6, pady = 20, columnspan = 2)


# Edit/Delete info tab:
window_tab3 = ttk.Frame(main_notebook)
main_notebook.add(window_tab3, text = "Edit/Delete info")
main_notebook.pack(expand = 1, fill = "both")

t3_select_lbl3 = ttk.Label(window_tab3, text = "Select a name to edit or delete:")
t3_select_lbl3.grid(column = 0, row = 0, pady = 15)

t3_user_var = tk.StringVar()
t3_user_combo3 = ttk.Combobox(window_tab3, width = 25, textvariable = t3_user_var)
t3_user_combo3.grid(column = 0, row = 1, columnspan = 2, pady = 10)
t3_user_combo3["values"] = db_manager_sqlite.words
t3_user_combo3.bind("<<ComboboxSelected>>", t3_selection_changed)

t3_full_name_lbl3 = ttk.Label(window_tab3, text = "Full name: ")
t3_full_name_lbl3.grid(column = 0, row = 2, pady = 10)

t3_full_name_var = tk.StringVar()
t3_full_name_entry3 = ttk.Entry(window_tab3, width = 25, textvariable = t3_full_name_var)
t3_full_name_entry3.grid(column = 1, row = 2, pady = 10)

t3_phone_number_lbl2 = ttk.Label(window_tab3, text = "Phone Number: ")
t3_phone_number_lbl2.grid(column = 0, row = 3)

t3_phone_number_var = tk.StringVar()
t3_phone_number_entry2 = ttk.Entry(window_tab3, width = 25, textvariable = t3_phone_number_var)
t3_phone_number_entry2.grid(column = 1, row = 3, pady = 10)

t3_email_lbl2 = ttk.Label(window_tab3, text = "E-mail: ")
t3_email_lbl2.grid(column = 0, row = 4)

t3_email_var = tk.StringVar()
t3_email_entry2 = ttk.Entry(window_tab3, width = 25, textvariable = t3_email_var)
t3_email_entry2.grid(column = 1, row = 4, pady = 10)

t3_notes_lbl2 = ttk.Label(window_tab3, text = "Notes: ")
t3_notes_lbl2.grid(column = 0, row = 5, pady = 10)

t3_notes_var = tk.StringVar()
t3_notes_entry2 = ttk.Entry(window_tab3, width = 25, textvariable = t3_notes_var)
t3_notes_entry2.grid(column = 1, row = 5)

t3_save_btn = tk.Button(window_tab3, text = "Save Changes!",
        bg = "red", fg = "white", font = ("arial", "12"), command = t3_save_changes)
t3_save_btn.grid(column = 0, row = 6, pady = 20)

t3_delete_btn = tk.Button(window_tab3, text = "Delete!", 
        bg = "red", fg = "white", font = ("arial", "12"), command = t3_delete)
t3_delete_btn.grid(column = 1, row = 6, pady = 30)
#####  END OF GUI  ####
#######################


window.mainloop()
