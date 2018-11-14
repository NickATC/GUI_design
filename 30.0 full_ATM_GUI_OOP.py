# -*- coding: utf-8 -*-

#  Ejercicio completo GUI y OOP

# Requisitos:
# 1.  No habrá login.  Simplemente cree las opciones de un ATM
# 2.  Un ATM da muchos mensajes al usuario.  Agregue los mensajes a donde pertenen.
# 3.  Vamos a mantenerlo muy sencillo.  Los retiros y consignaciones serán de 10$
# 4.  Conecte los botones con las funciones correspondientes para que el ATM funcione correctamente

# Quiere reto?
# Reto 1.  Modifique su código para que no pueda retirar más de su balance.  Use el mensaje FALLO. 
# Reto 2.  Modifique su código para que tan pronto ejecutemos el ATM, veamos un mensaje de bienvenida. 
#          Use el mensaje 'welcoming_message'.


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
        pass
        
    def see_balance(self):
        pass

    def withdraw(self):
        pass
            
    def deposit(self):
        pass

    def finish_trasaction(self):
        pass


##########################
#### GUI starts here #####
##########################

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

account1 = ATM(100)  # Creating the instance.  Passing 100$ as initial amount
account1.welcoming_message()  # Will insert the welcoming message on the ScrolledText as soon
                              # as the GUI is created.

# Action buttons:
balance_button = ttk.Button(label_frame1, text = "See Balance")
balance_button.grid(column = 0, row = 2)

withdraw_button = ttk.Button(label_frame1, text = "Withdraw 10$") 
withdraw_button.grid(column = 0, row = 3)

deposit_button = ttk.Button(label_frame1, text = "Deposit 10$")
deposit_button.grid(column = 3, row = 2)

end_button = ttk.Button(label_frame1, text = "End Transaction")
end_button.grid(column = 3, row = 3)


window.mainloop()
