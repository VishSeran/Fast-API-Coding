from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from .schemas import  ShipmentCreate, ShipmentRead, ShipmentStatus, ShipmentUpdate
from enum import Enum
from .database import shipments,save


app = FastAPI()


# shipments = {
#     12732: {"weight": 1.9, "content": "Glass table", "status": "placed"},
#     12733: {"weight": 3.9, "content": "Glass box", "status": "received"},
#     12735: {"weight": 4.9, "content": "Plastic bin", "status": "In transit"},
#     12742: {"weight": 0.9, "content": "Glass door", "status": "In transit"},
#     12746: {"weight": 4.3, "content": "Laptop cover", "status": "In packing"},
# }


## when define a class
class City:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location


##get latest shipments
## order is matter in API decleration.


@app.get("/shipment/latest")
def get_latest_shipments() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]


""" @app.get("/shipments/{id}")
def get_shipment_by_id(id:int) -> dict[str, Any]:
    
    
    return shipments[id]
 """
# we can use query parameter to pass id to functio "get_shipment_by_id"


@app.get("/shipment",response_model=ShipmentRead)
def get_shipment_by_id(id: int):
    
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exists"
        )
    
    return shipments[id]
    


@app.post("/shipment")
def add_shipment(shipment: ShipmentCreate) -> dict[str, Any]:

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        **shipment.model_dump(),
        "id":new_id,
        "status": "Placed"}
    save()

    return {"id": new_id}


# if we want to get data from the request body we have to initiate a dict type paramter

""" @app.post("/shipment") 
def add_shipment(data: dict):
    return data """

# we ca use path and query parameters together
@app.get("/shipment/{field}")
def get_shipments(field: str, id: int) -> dict[str, Any]:
    return {field: shipments[id][field]}

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
    
    print("="*30)
    print(body)
    print("="*30)
    print("="*30)
    print(body.model_dump(exclude_none=True))
    
    #shipment = shipments[id]
    # if content:
    #     shipment["content"] = content
    # if weight:
    #     shipment["weight"] = weight
    # if status:
    #     shipment["status"] = status
    
    shipments[id].update(body.model_dump(exclude_none=True))
    return shipments[id]

@app.delete("/shipment")
def delete_shipment(id:int) -> dict[str,str]:
    shipments.pop(id)
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
