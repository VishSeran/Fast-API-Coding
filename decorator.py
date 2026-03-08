from typing import Callable, Any

""" def fence(func):
    def wrapper(text:str):
        print("+" * 10)
        func(text)
        print("+" * 10)
    return wrapper

@fence
def log(text:str) :
    print (text)

log("everyone") """

# we can hind the notifiy a function type using callable
# Callable[[input type], return type ]

## functions with more than one parameter
# Callable [[Inputs types using comma], return type]

def fence (style:str = "+"):
    def add_fence(func: Callable[[str], str]):
        def wrapper (text:str):
            print(style * len(text))
            func(text)
            print(style * len(text))
        return wrapper
    return add_fence

@fence("=")
def log(text:str):
    print (text)
    
log("EveryOne")
    
    
routes: dict[str, Callable[[Any], Any]] = {}

def route (path:str):
    def register_route(func):
        routes[path] = func
        return func
    return register_route

@route("/shipment")
def get_shipment():
    return "<ship001> Ready to deploy"

@
def get_shipment_by_id ()


answer :str = ""

while answer != "quit":
    req = input(">   ")
    
    if req in routes:
        res = routes[req]()
        print(res, end="\n\n")
    
    else:
        print("Not found")