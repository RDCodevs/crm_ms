from fastapi import APIRouter
from services import pacients as pac
from models.pacients import Pacient

router = APIRouter(prefix="/pacients")

@router.get("/{pacient_id}")
async def get_pacient_by_id(pacient_id):
    return pac.get_pacient(pacient_id)