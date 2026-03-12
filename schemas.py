from enum import Enum

from pydantic import BaseModel, Field
from random import randint

def rand_destination():
    return randint(100000,120000)

class ShipmentStatus(str,Enum):
    placed = "placed"
    in_transit = "in_transit"
    delivered = "delievered"

class BaseShipment(BaseModel):
    content :str 
    weight: float = Field(le=25, ge=1)
    destination: int | None = Field(default_factory=rand_destination)
class ShipmentRead(BaseShipment):
    status: ShipmentStatus
    
class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus 