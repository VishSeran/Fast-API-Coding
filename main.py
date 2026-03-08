from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Any 

app = FastAPI()

## when define a class
class City:
    
    def __init__(self, name:str, location:str):
        self.name = name
        self.location = location

@app.get("/shipments")
def get_shipments():
    return {
        "content": "RTX ",
        "status": "In trasmit"
    }

##get latest shipments
## order is matter in API decleration. 

@app.get("/shipments/latest")
def get_latest_shipments():
    return {
        "id": 4354,
        "weight": 1.9,
        "content": "Glass table",
        "status" : "In transit"
    }
    
@app.get("/shipments/{id}")
def get_shipment_by_id(id: int) -> dict[str, str | int |  float]:
    return {
        "id": id,
        "weight": 1.2,
        "content": "Supervised Box",
        "status" : "Delivered"
    }
    

    
@app.get("/scalar", include_in_schema= False)    
def get_scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar FastAPI"
    )
    
digits: list[int] = [1,2,3,4,5,6,7,8,9] # List type variable which contains int type values

number: int | float =12.2
tuple_1: tuple[int, int, int,int] = (1,2,3,4)

city = City("Sri lanka", "ja-ela")
city_temp: tuple[City,float] = (city, 20.5)

shipment: dict[str,str | int |float] = {
    "id": 1234,
    "weight" : 1.43,
    "content": "wooden table",
    "status": "in transit"
}

shipmentNew: dict[str,Any] = {
    "id": 1234,
    "weight" : 1.43,
    "content": "wooden table",
    "status": "in transit"
}

def root(num:int | float, exp: float | None) -> float:
    
    if exp is None:
        exp = 0.5
    else: exp = exp
    
    return pow(num, exp)
    
root_25 = root(25,10)
root_25
