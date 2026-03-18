
from app.database.model import ShipmentStatus

from pydantic import BaseModel, Field
from random import randint

def rand_destination():
    return randint(100000,120000)


class BaseShipment(BaseModel):
    content :str 
    weight: float = Field(le=25, ge=1)
    destination: int | None = Field(default_factory=rand_destination)
class ShipmentRead(BaseShipment):
    status: ShipmentStatus
    
class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    content :str | None = Field(default=None)
    weight: float | None = Field(default=None,le=25, ge=1)
    destination: int | None = Field(default=None)
    status: ShipmentStatus 