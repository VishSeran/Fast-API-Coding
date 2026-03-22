import asyncio
import time

from rich import print

async def endpoint(route:str) -> str:
    print(f">> handling {route}")
    await asyncio.sleep(1)
    print(f"<< reponse {route}")
    return route

# endpoint function now converted to coroutine, so we have to follow
# asyncio or await for run coroutine function
#endpoint("")

async def server():
    
    test = (
        "GET /shipment?id=1",
        "Patch /shipment?id=4",
        "GET /shipment?id=3"
    )
    
    start_time = time.perf_counter()
    for route in test:
        result = await endpoint(route)
        print("Result back: ", result)
    end_time = time.perf_counter()
    
    print(f"Time taken: {(end_time-start_time):.2f}")
    
asyncio.run(
    server()
)