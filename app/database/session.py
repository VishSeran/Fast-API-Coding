from sqlalchemy import create_engine
from sqlmodel import SQLModel


engine = create_engine(
    url = "sqlit:///new_sqlite.db",
    echo=True,
    connect_args={"check_same_thread": False}
)

def create_db():
    from .model import Shipment
    SQLModel.metadata.create_all(bind=engine)



