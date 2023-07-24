from fastapi import FastAPI
from src.routers.pacients import router as router_pacient
from src.routers.cites import router as router_cites
from src.routers.medic import router as router_medic
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_pacient)
app.include_router(router_cites)
app.include_router(router_medic)
