from fastapi import FastAPI
from src.routers.pacients import router as router_pacient

app = FastAPI()

app.include_router(router_pacient)