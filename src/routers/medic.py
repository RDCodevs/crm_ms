from fastapi import APIRouter, status
from src.services import medic as med
from src.schemas.medic import Medic, ListMedic, UpdateMedic

router = APIRouter(prefix="/medics")

@router.get("/get_medic/{medic_id}", tags= ["Medics"])
async def get_medic_by_id(medic_id: int):
    return med.get_medic(medic_id)

@router.get("/get_all",
            status_code= status.HTTP_200_OK,
            response_model= ListMedic,
            tags= ["Medics"])
async def get_all_medic():
    return med.get_all_medic()

@router.post("/add_medic", 
             status_code= status.HTTP_201_CREATED, 
             response_model= Medic,
             summary= "End point para agregar un nuevo medico",
             tags= ["Medics"])
async def create_medic(medic: Medic):
    return med.create_medic(medic)

@router.put("/update_medic", tags= ["Medics"])
async def update_medic(medic: Medic):
    return med.update_medic(medic)

@router.patch("/edit_medic/", 
              status_code= status.HTTP_200_OK,
              response_model= Medic,
              tags= ["Medics"])
async def patch_medic(medic: UpdateMedic):
    return med.patch_medic(medic)

@router.delete("/delete_medic/{medic_id}", tags= ["Medics"])
async def delete_medic(medic_id: int):
    return med.delete_medic(medic_id)
