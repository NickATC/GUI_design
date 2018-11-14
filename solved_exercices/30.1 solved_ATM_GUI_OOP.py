# -*- coding: utf-8 -*-

# Ejercicio 30   ATM SOLUCIONADO

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


class ATM:
    def __init__(self, amount):
        self.__amount = amount    
        self.balance = "Your current balance is: "
        self.success = "Trasanction was successfull !"
        self.fail = "Insufficient Funds !"
        self.welcome_msg = "Welcome to your ATM !"
        self.end_session = "Closing session. \n     Wait a moment... "
        
    def welcoming_message(self):
        atm_screen.insert(tk.INSERT, self.welcome_msg)
      
    def see_balance(self):
        atm_screen.delete(1.0,"end")
        atm_screen.insert(tk.INSERT, self.balance)
        atm_screen.insert(tk.INSERT, self.__amount)

    def withdraw(self):
        if self.__amount - 10 >= 0:
            self.__amount = self.__amount - 10
            atm_screen.delete(1.0,"end")
            atm_screen.insert(tk.INSERT, self.success)
        else:
            atm_screen.delete(1.0,"end")
            atm_screen.insert(tk.INSERT, self.fail)
            
    def deposit(self):
        self.__amount = self.__amount + 10 
        atm_screen.delete(1.0,"end")
        atm_screen.insert(tk.INSERT, self.success)

    def finish_trasaction(self):
        atm_screen.delete(1.0,"end")
        atm_screen.insert(tk.INSERT, self.end_session)
        quit()


##########################
#### GUI starts here #####

window = tk.Tk()
window.title("Simple ATM")
window.geometry("530x200")
window.resizable(False, False)

#Label-Frame for the ATM:
label_frame1 = ttk.LabelFrame(window, text = "Python ATM")
label_frame1.grid(column = 0, row = 1, padx = 25, pady = 30)

# ATM Screen
atm_screen = scrolledtext.ScrolledText(label_frame1, width = 30, height = 3, wrap = tk.WORD)
atm_screen.grid(column = 2, row = 2, padx = 20, pady = 10)

account1 = ATM(100)
account1.welcoming_message()

# Action buttons:
balance_button = ttk.Button(label_frame1, text = "See Balance", command = account1.see_balance)
balance_button.grid(column = 0, row = 2)

withdraw_button = ttk.Button(label_frame1, text = "Withdraw 10$", command = account1.withdraw) 
withdraw_button.grid(column = 0, row = 3)

deposit_button = ttk.Button(label_frame1, text = "Deposit 10$", command = account1.deposit)
deposit_button.grid(column = 3, row = 2)

end_button = ttk.Button(label_frame1, text = "End Transaction", command = account1.finish_trasaction)
end_button.grid(column = 3, row = 3)


window.mainloop()
