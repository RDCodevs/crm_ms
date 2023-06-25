from fastapi import APIRouter, status
from src.services import medic as med
from src.schemas.medic import Medic, ListMedics, UpdateMedic

router = APIRouter(prefix= "/medics")

@router.get()
async def get_all_medics():
    pass
