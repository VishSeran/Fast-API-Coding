from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from .schemas import  ShipmentCreate, ShipmentRead, ShipmentUpdate
from .database_json import shipments,save
from .database import Database


app = FastAPI()
db = Database()


@app.get("/shipment",response_model=ShipmentRead)
def get_shipment_by_id(id: int):
    
    shipment = db.get(id)
    
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exists"
        )
    
    return shipments
    


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


digits: list[int] = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
]  # List type variable which contains int type values

number: int | float = 12.2
tuple_1: tuple[int, int, int, int] = (1, 2, 3, 4)

city = City("Sri lanka", "ja-ela")
city_temp: tuple[City, float] = (city, 20.5)

shipment: dict[str, str | int | float] = {
    "id": 1234,
    "weight": 1.43,
    "content": "wooden table",
    "status": "in transit",
}

shipmentNew: dict[str, Any] = {
    "id": 1234,
    "weight": 1.43,
    "content": "wooden table",
    "status": "in transit",
}


def root(num: int | float, exp: float | None) -> float:

    if exp is None:
        exp = 0.5
    else:
        exp = exp

    return pow(num, exp)


root_25 = root(25, 10)
root_25
