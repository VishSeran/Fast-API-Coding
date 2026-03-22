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
    # This schedules all three immediately — they run concurrently
    requests = [
        asyncio.create_task(endpoint(route))
        for route in test    
    ]
    
    done, pending = await asyncio.wait(requests)
    
    
    for task in done:
        print("Result:", task.result())
    end_time = time.perf_counter()
    
    print(f"Time taken: {(end_time-start_time):.2f}")
    
asyncio.run(
    server()
)