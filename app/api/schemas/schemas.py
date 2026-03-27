
from datetime import datetime
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
    estimated_delivery: datetime
    
class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus | None = Field(default=None)
    estimated_delivery: datetime | None = Field(default=None)