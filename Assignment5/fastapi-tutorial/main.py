import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def base_get_route():
    return {"message": "Hello World"}

@app.post("/")
async def root():
    return {"message": "Hello from the post route"}

@app.put("/")
async def root():
    return {"message": "Hello from the put route"}