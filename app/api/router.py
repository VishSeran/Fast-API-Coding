import datetime
from typing import Any
from fastapi import APIRouter, HTTPException,status

from app.api.dependencies import Shipment_Session_Dep
from app.database.model import Shipment, ShipmentStatus
from app.database.session import SessionDep
from app.api.schemas.schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate
from app.services.shipment import ShipmentService

router = APIRouter()


@router.get("/shipment",response_model=ShipmentRead)
async def get_shipment_by_id(id: int, service:Shipment_Session_Dep):
    
    shipment = await service.get(id)
    
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exists"
        )
    
    return shipment
    

@router.post("/shipment")
async def add_shipment(shipment: ShipmentCreate, service:Shipment_Session_Dep) -> Shipment:  
    return await service.add(shipment)



# # we ca use path and query parameters together
# @router.get("/shipment/{field}")
# def get_shipments(field: str, id: int) -> dict[str, Any]:
#     return {field: shipments[id][field]}

# we can use put method to update whole fields
# @router.put("/shipment",response_model=ShipmentUpdate)
# def shipment_update(id: int, content: str, weight:float, status: str 
#                     ) ->  dict[str, Any]:
    
#     shipments[id] = {
#         "content" : content,
#         "weight": weight,
#         "status": status
#     }
    
#     return shipments[id]

@router.patch("/shipment")
async def patch_shipment(id:int, body: ShipmentUpdate, service:Shipment_Session_Dep) -> dict[str,Any]:
    
    update_data = body.model_dump(exclude_none=True)
    
    if not update_data:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Empty request"
        )
    
    update_shipment = await service.update(id, update_data)
    
    if update_shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    return update_shipment

@router.delete("/shipment")
async def delete_shipment(id:int, service:Shipment_Session_Dep) -> dict[str,str]:
    await service.delete(id)
    return {"Details": "shipment with id {} is deleted".format(id)}