from fastapi import FastAPI
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference

from app.api.router import router
from app.database.session import create_db

@asynccontextmanager
async def lifespan_handler(app:FastAPI):
    await create_db()
    yield
    print("Server Stopped>>>")
    
app = FastAPI(lifespan= lifespan_handler)
# router connected
app.include_router(router)


@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar FastAPI")

    
