import time

from rich import print

def endpoint(route):
    print(f">> handling {route}")
    time.sleep(1)
    print(f"<< reponse {route}")
    return route


def server():
    
    test = (
        "GET /shipment?id=1",
        "Patch /shipment?id=4",
        "GET /shipment?id=3"
    )
    
    start_time = time.perf_counter()
    for route in test:
        endpoint(route)
    end_time = time.perf_counter()
    
    print(f"Time taken: {(end_time-start_time):.2f}")
    
server() 