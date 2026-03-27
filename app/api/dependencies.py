
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.database.session import  session_bind
from app.services.shipment import ShipmentService

SessionDep = Annotated[AsyncSession, Depends(session_bind)]

def ShipmentSession(session: SessionDep):
    return  ShipmentService(session)

Shipment_Session_Dep = Annotated[AsyncSession,Depends(ShipmentSession)]

