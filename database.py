import sqlite3
from typing import Any

from schemas import ShipmentCreate, ShipmentUpdate

class Database:
    
    def __init__(self):
        # make the conncetion
        self.connection = sqlite3.connect("ShipmentDatabase.db")
        #Cursor object for query executions
        self.cursor = self.connection.cursor()
        self.create_table()
        
    # create table
    def create_table(self):
        # 1. Create table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXIST shipment (
                id INTEGER PRIMARY KEY,
                content TEXT,
                weight REAL,
                status TEXT
            )        
                """)

    # 2. Add shipment data
    def create(self, shipment:ShipmentCreate) -> int:
        self.cursor.execute("""
                SELECT MAX(id) FROM shipment            
                            """)
        result = (self.cursor.fetchone()) + 1
        new_id = result[0] + 1
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
    def get(self, id:int)-> dict[str, Any] | None:
        
        self.cursor.execute("""
            SELECT * FROM shipment WHERE id = ?                            
                            """, (id,))
        result = self.cursor.fetchone()
        
        if result is None:
            return None
             
        return {
            "id" : result[0],
            "content": result[1],
            "weight": result[2],
            "status": result[3]
        }
        
    # update a shipment
    def update(self, id:int, shipment: ShipmentUpdate)-> dict[str, Any] | None:
        self.cursor.execute("""
            UPDATE shipment SET status = :status
            WHERE id = :id                
            """,{
                "id": id,
                **shipment.model_dump()
            })
        self.connection.commit()
        return self.get(id)

    # delete a shipment
    def delete(self, id:int):
        self.cursor.execute("""
            DELETE FROM shipment 
            WHERE id = ?                
            """,(id,))
        self.connection.commit()
    
    # close the database connection
    def close(self):
        self.connection.close()




