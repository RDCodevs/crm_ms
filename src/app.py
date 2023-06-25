from fastapi import FastAPI
from src.routers.pacients import router as router_pacient
from src.routers.cites import router as router_cites

app = FastAPI()

app.include_router(router_pacient)
app.include_router(router_cites)