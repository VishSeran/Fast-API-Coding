
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_engine, create_async_engine
from sqlmodel import SQLModel, Session

from app.config import DatabaseSettings

# engine = create_engine (
#     url="sqlite:///new_sqlite_2.db",
#     echo=True,
#     connect_args={"check_same_thread": False}
# )

# from .model import Shipment
# def create_db():
#     SQLModel.metadata.create_all(bind=engine)


# def session_bind():
#     with Session(bind=engine) as session:
#         yield session

# SessionDep = Annotated[Session, Depends(session_bind)]
settings = DatabaseSettings()

engine = create_async_engine(
    url= settings.POSTGRES_URL,
    echo = True
)

async def create_db():
    # context manager
    async with engine.begin() as conncetion:
        await conncetion.run_sync(SQLModel.metadata.create_all())
        