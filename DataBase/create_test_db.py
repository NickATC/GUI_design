# Execute this file to create a database.  It also adds information for testing purposes.
# Execute only once!  

# A file called 'my_database.db' should be created on this same folder
# 
# This script doesn't do anything else.  


import sqlite3

con_db = sqlite3.connect("my_database.db")
cursor = con_db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS phone_book        \
            (id INTEGER PRIMARY KEY AUTOINCREMENT,           \
            full_name TEXT,          \
            phone_number TEXT,       \
            email TEXT,              \
            notes TEXT)") 
      
# insert data
cursor.execute("INSERT INTO phone_book (full_name, phone_number, email, notes) \
                VALUES (?, ?, ?, ?)", ("Nicolas Tautiva", "123-456789", "nicolas_tautiva@mail.com", "Not his real email."))
            
cursor.execute("INSERT INTO phone_book (full_name, phone_number, email, notes) \
                VALUES (?, ?, ?, ?)", ("Pedro Jimenez", "987-654310", "pedro_jimenez@mail.com", "Fake person."))

cursor.execute("INSERT INTO phone_book (full_name, phone_number, email, notes) \
                VALUES (?, ?, ?, ?)", ("Juan Perez", "456-789123", "juan_perez@mail.com", "Nothing here"))

cursor.execute("INSERT INTO phone_book (full_name, phone_number, email, notes) \
                VALUES (?, ?, ?, ?)", ("Maria Ramirez", "369-258147", "maria_ramirez@mail.com", ""))

 # commit transaction
con_db.commit()

# close cursor and connection
cursor.close()
con_db.close()

print("...")
print("Database created")
print("information added successfully!")
