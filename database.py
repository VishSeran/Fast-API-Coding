import sqlite3
from typing import Any

from schemas import ShipmentCreate

class Database:
    
    def __init__(self):
        # make the conncetion
        self.connection = sqlite3.connect("ShipmentDatabase.db")
        #Cursor object for query executions
        self.cursor = self.connection.cursor()
        self.create_table("shipment")
        
    # create table
    def create_table(self,name:str):
        # 1. Create table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXIST ? (
                id INTEGER PRIMARY KEY,
                content TEXT,
                weight REAL,
                status TEXT
            )        
                """,(name,))

    # 2. Add shipment data
    def create(self, shipment:ShipmentCreate) -> int:
        self.cursor.execute("""
                SELECT MAX(id) FROM shipment            
                            """)
        new_id = (self.cursor.fetchone()) + 1
        
        self.cursor.execute("""
            INSERT INTO shipment 
            VALUES (:id, :content, :weight, :status)
                            """,
            {
                "id": new_id,
                **shipment.model_dump(),
                "status": "placed"
            })
        self.connection.commit()
        return new_id

    # get shipment
    def get(self, id:int)-> dict[str, Any]:
        
        self.cursor.execute("""
            SELECT * FROM shipment WHERE id = ?                            
                            """, (id,))
        result = self.cursor.fetchone()
        return {
            "id" : result[0],
            "content": result[1],
            "weight": result[2],
            "status": result[3]
        }

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