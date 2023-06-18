from fastapi import FastAPI
from routers.pacients import router as router_pacient

app = FastAPI()

app.include_router(router_pacient)

@app.get("/")
async def root():
    return {"message": "Hello World!"}