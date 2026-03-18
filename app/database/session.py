
from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

engine = create_engine (
    url="sqlite:///new_sqlite_2.db",
    echo=True,
    connect_args={"check_same_thread": False}
)

from .model import Shipment
def create_db():
    
    SQLModel.metadata.create_all(bind=engine)

session = Session(bind=engine)

def session_bind():
    with Session(bind=engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(session_bind)]