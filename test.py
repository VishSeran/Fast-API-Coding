from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan_handler(app:FastAPI):
    print("Sever start>>>>")
    yield
    print("Server Stopped<<<<<")

app = FastAPI(lifespan= lifespan_handler)

@app.get("/")
def get_all():
    return {"Details": "Server is running"}