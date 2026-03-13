import sqlite3

#Make connection
connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()# make the cursor object

# execute the sql queries by cursor object 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER,
        content TEXT,
        weight REAL,
        status TEXT
    )
               """)

# Close Connection when done
connection.close()