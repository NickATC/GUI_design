

import sqlite3


class DBManager_sqlite:
    def __init__(self):
        """Attributes"""
        self.GUIDB = 'my_database.db'      #database name...name as you wish
        self.connect_db()
        self.create_db()
        self.words = ["Select a user"]
                
    def connect_db(self):
        """Connecting to SQLite"""

        con_db = sqlite3.connect(self.GUIDB)
             
        #creating the cursor to send commands to SQLite
        cursor = con_db.cursor()

        #we return the connection and the cursor.
        return con_db, cursor

    def close(self, cursor, con_db):
        """To close the SQLite connection and cursor"""
        cursor.close()
        con_db.close()
        
    def create_db(self):
        """Connecting and creating the SQLite db.  It has to be manually be executed.
        This funtion is not included in any part of the code. Add to the __init__ if
        you know what you are doing!"""
        #connect and create Data Base!!!
        con_db = sqlite3.connect(self.GUIDB)
                
        #creating the cursor to send commands to SQLite
        cursor = con_db.cursor()

        # Creating the table
        cursor.execute("CREATE TABLE IF NOT EXISTS phone_book        \
            (id INTEGER PRIMARY KEY AUTOINCREMENT,                   \
            full_name TEXT,          \
            phone_number TEXT,       \
            email TEXT,              \
            notes TEXT)")        
        
    def show_Title_account(self):
        """To show information on the Scrolledtext.
        The information to display is added to a list."""
        con_db, cursor = self.connect_db()
         
        self.words = ["Select a user"]

        # execute command
        cursor.execute("SELECT full_name FROM phone_book")
        
        #create a var to name each item in the fetchall()
        list_titles = cursor.fetchall()
        
        #add each word to a list:
        for row in list_titles:
            self.words.append(row[0])
        
        # close cursor and connection
        self.close(cursor, con_db)
       
    def extract_db_info(self, full_name):
        """Extract info from SQLite DB.  Passing the selection on the combobox as parameter
        It then cleans the data y adds it to a list"""
        
        con_db, cursor = self.connect_db()

        all_results = [] # To store values from DB.

        cursor.execute("SELECT full_name FROM phone_book WHERE full_name = (?)", [full_name])
        result_full_name = cursor.fetchall()
        all_results.append(result_full_name)

        cursor.execute("SELECT phone_number FROM phone_book WHERE full_name = (?)", [full_name])
        result_phone_number = cursor.fetchall()
        all_results.append(result_phone_number)

        cursor.execute("SELECT email FROM phone_book WHERE full_name = (?)", [full_name])
        result_email = cursor.fetchall()
        all_results.append(result_email)

        cursor.execute("SELECT notes FROM phone_book WHERE full_name = (?)", [full_name])
        result_notes = cursor.fetchall()
        all_results.append(result_notes)
        all_results_clean = [] # All results after cleaning.

        for item in all_results:
            item_clean = item[0][0]
            all_results_clean.append(item_clean)
        
        self.close(cursor, con_db)
        
        return all_results_clean
        
    def insert_data(self, t2_full_name_var, t2_phone_number_var, t2_email_var, t2_notes_var):
        """Takes info from Tab2 (Add Info) and inserts it into the SQLlite DB"""
        con_db, cursor = self.connect_db()
        
        # insert data
        cursor.execute("INSERT INTO phone_book (full_name, phone_number, email, notes) \
            VALUES (?, ?, ?, ?)", (t2_full_name_var, t2_phone_number_var, t2_email_var, t2_notes_var))
            
        # commit transaction
        con_db.commit()

        self.show_Title_account()

        # close cursor and connection
        self.close(cursor, con_db)

        

    def update_data(self, title_value_edit, t3_full_name_edit, 
                    t3_phone_number_edit, t3_email_edit, t3_notes_edit):
        """Takes info from the Tab3 (Update Info) and updates it into the SQLite db"""
        
        con_db, cursor = self.connect_db()
        
        # Get id:
        cursor.execute("SELECT id FROM phone_book WHERE full_name = (?);", [title_value_edit])
        result_pass_id = cursor.fetchall()[0][0]
     
        # Update TITLE_ACCOUNT
        cursor.execute("UPDATE phone_book SET full_name = (?) WHERE id = (?);",  
                        (t3_full_name_edit, result_pass_id))
       
        # Update USER_ACCOUNT
        cursor.execute("UPDATE phone_book SET phone_number = (?) WHERE id = (?);",  
                        (t3_phone_number_edit, result_pass_id))

        # Update PASSWORD
        cursor.execute("UPDATE phone_book SET email = (?) WHERE id = (?);",  
                        (t3_email_edit, result_pass_id))

        # Update WEB_SITE
        cursor.execute("UPDATE phone_book SET notes = (?) WHERE id = (?);",  
                        (t3_notes_edit, result_pass_id))

        
        con_db.commit()

        self.show_Title_account() #Updates changes into the GUI
        self.close(cursor, con_db)

        

    def delete_data(self, user_value_delete):
        """Deletes a row of information from the SQLite db"""
        con_db, cursor = self.connect_db()

        # Obtain ID
        cursor.execute("SELECT id FROM phone_book WHERE full_name = (?);", [user_value_delete])
        result_pass_id = cursor.fetchall()[0][0]

        # Delete records on ID
        cursor.execute("DELETE from phone_book WHERE id = (?);", [result_pass_id])
        
        con_db.commit()

        self.show_Title_account()

        self.close(cursor, con_db)

    def drop_db(self):
        """Eliminates completely the DB.  Use with caution!"""
        con_db, cursor = self.connect_db()
                
        cursor.execute("DROP DATABASE ()", (self.GUIDB))
        
        self.close(cursor, con_db)
