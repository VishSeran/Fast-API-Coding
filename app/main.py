from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from .app.database.model import Shipment, ShipmentStatus
from .app.database.session import SessionDep, create_db
from .database import Database
from .schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate


@asynccontextmanager
async def lifespan_handler(app:FastAPI):
    create_db()
    yield
    print("Server Stopped>>>")

app = FastAPI(lifespan= lifespan_handler)

db = Database()



    

@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar FastAPI")

    
