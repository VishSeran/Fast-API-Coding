from fastapi import APIRouter

router = APIRouter()


@router.get("/shipment",response_model=ShipmentRead)
def get_shipment_by_id(id: int, session:SessionDep):
    
    shipment = session.get(Shipment, id)
    
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exists"
        )
    
    return shipment
    

@router.post("/shipment")
def add_shipment(shipment: ShipmentCreate,session:SessionDep) -> dict[str, Any]:

    new_shipment = Shipment(
        **shipment.model_dump(),
        status = ShipmentStatus.placed,
        estimated_delivery= datetime.now() + timedelta(days = 3)
    )
    
    session.add(new_shipment)
    session.commit()
    session.refresh(new_shipment)
    
    new_id = new_shipment.id
    return {"id": new_id}



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

@router.patch("/shipment",response_model=ShipmentRead)
def patch_shipment(id:int, body: ShipmentUpdate, session: SessionDep):
    
    update_data = body.model_dump(exclude_none=True)
    
    if not update_data:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Empty request"
        )
    
    update_shipment = session.get(Shipment, id)
    
    if update_shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    update_shipment.sqlmodel_update(update_data)
    
    session.add(update_shipment)
    session.commit()
    session.refresh(update_shipment)
    
    return update_shipment

@router.delete("/shipment")
def delete_shipment(id:int, session:SessionDep) -> dict[str,str]:
    session.delete(
        session.get(Shipment,id)
    )
    session.commit()
    return {"Details": "shipment with id {} is deleted".format(id)}