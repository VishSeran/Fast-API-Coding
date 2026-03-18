from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from contextlib import asynccontextmanager
from typing import Any
from .schemas import  ShipmentCreate, ShipmentRead, ShipmentUpdate
from .database import Database
from app.database.session import create_db

@asynccontextmanager
def lifespan_handler(app:FastAPI):
    create_db()
    yield
    print("Server Stopped>>>")

app = FastAPI(lifespan= lifespan_handler)



db = Database()


@app.get("/shipment",response_model=ShipmentRead)
def get_shipment_by_id(id: int):
    
    shipment = db.get(id)
    
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exists"
        )
    
    return shipment
    


@app.post("/shipment")
def add_shipment(shipment: ShipmentCreate) -> dict[str, Any]:

    new_id = db.create(shipment)
    return {"id": new_id}



# # we ca use path and query parameters together
# @app.get("/shipment/{field}")
# def get_shipments(field: str, id: int) -> dict[str, Any]:
#     return {field: shipments[id][field]}

# we can use put method to update whole fields
# @app.put("/shipment",response_model=ShipmentUpdate)
# def shipment_update(id: int, content: str, weight:float, status: str 
#                     ) ->  dict[str, Any]:
    
#     shipments[id] = {
#         "content" : content,
#         "weight": weight,
#         "status": status
#     }
    
#     return shipments[id]

@app.patch("/shipment",response_model=ShipmentRead)
def patch_shipment(id:int, body: ShipmentUpdate):
    
    shipment = db.update(id,body)
    return shipment

@app.delete("/shipment")
def delete_shipment(id:int) -> dict[str,str]:
    db.delete(id)
    return {"Details": "shipment with id {} is deleted".format(id)}
    

@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar FastAPI")

