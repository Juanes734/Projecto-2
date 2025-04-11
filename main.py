from fastapi import FastAPI
from controller.abb_controller import abb_route

app = FastAPI()
app.include_router(abb_route)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
