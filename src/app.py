from fastapi import FastAPI
from src.routers.pacients import router as router_pacient
from src.routers.medic import router as router_medic

app = FastAPI()

app.include_router(router_pacient)
app.include_router(router_medic)