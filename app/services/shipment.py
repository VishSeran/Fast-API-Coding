

from datetime import datetime,timedelta

from app.api.schemas.schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate
from sqlalchemy.ext.asyncio import AsyncSession



from app.database.model import Shipment, ShipmentStatus


class ShipmentService:
    def __init__(self, session:AsyncSession):
        self.session = session
    
    async def get(self,id:int) -> ShipmentRead:
        return await self.session.get(Shipment,id)
    
    async def add(self,shipment_create:ShipmentCreate)->Shipment:
        new_Shipment = Shipment(
            **shipment_create.model_dump(),
            status=ShipmentStatus.placed,
            estimated_delivery=  datetime.now() + timedelta(days=3)
        )
        
        self.session.add(new_Shipment)
        await self.session.commit()
        await self.session.refresh(new_Shipment)
        
        return new_Shipment
    
    async def update(self, id:int, shipment_update:ShipmentUpdate) -> dict:
        
        shipment = await self.get(id)
        shipment.sqlmodel_update(shipment_update)
        
        self.session.add(shipment)
        await self.session.commit()
        await self.session.refresh(shipment)
        
        return shipment
    
    async def delete(self, id:int) -> None:
        
        await self.session.delete(await self.get(id))
        await self.session.commit()
        
        
        
            
        