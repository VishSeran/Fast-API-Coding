import sqlite3

#Make connection
connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()# make the cursor object

# execute the sql queries by cursor object 
# 1. Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER,
        content TEXT,
        weight REAL,
        status TEXT
    )
               """)

# 2. Add shipment data
cursor.execute("""
        INSERT INTO shipment 
        VALUES (12751, 'Olive tree', 19.5, 'in_transit')           
    """)
connection.commit()

# Close Connection when done
connection.close()