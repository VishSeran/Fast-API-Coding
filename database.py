import sqlite3

#Make connection
connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()# make the cursor object

# execute the sql queries by cursor object 
# 1. Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER PRIMARY KEY,
        content TEXT,
        weight REAL,
        status TEXT
    )
               """)

# cursor.execute("DROP TABLE shipment")
# connection.commit()

# 2. Add shipment data
# cursor.execute("""
#         INSERT INTO shipment 
#         VALUES (3, 'plam tree', 12.5, 'in_transit')           
#     """)
# connection.commit()

# 3. Fetch data from database
# cursor.execute("""
#          SELECT * FROM shipment
#          WHERE status = 'placed'      
#                """)
# result = cursor.fetchmany(2)
# print(result)

# 4. update a shipment

id = 0
status = 'placed'
cursor.execute("""
    UPDATE shipment SET status = :status
    WHERE id > :id
               """,
               {
                   "status" : status,
                   "id": id
               })
connection.commit()

#5. Delete a shipment by id

# cursor.execute("""
#          DELETE FROM shipment
#          WHERE id =  12752
#                """)
# connection.commit()
# Close Connection when done
connection.close()