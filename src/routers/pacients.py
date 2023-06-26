from fastapi import APIRouter, status
from src.services import pacients as pac
from src.schemas.pacients import Pacient, ListPacient, UpdatePacient

router = APIRouter(prefix="/pacients")

@router.get("/get_pacient/{pacient_id}", tags= ["Pacients"])
async def get_pacient_by_id(pacient_id: int):
    """
    ## ARGS
        - pacient: Pacient
    ## REPONSE
        - pacient: Pacient
    
    """
    return pac.get_pacient(pacient_id)

@router.get("/get_all",
            status_code= status.HTTP_200_OK,
            response_model= ListPacient,
            tags= ["Pacients"])
async def get_all_pacient():
    """
    ## REPONSE
        - pacient: List(Pacient)    
    """
    return pac.get_all_pacient()

@router.post("/add_pacient", 
             status_code= status.HTTP_201_CREATED, 
             response_model= Pacient,
             summary= "End point para agregar un nuevo paciente",
             tags= ["Pacients"])
async def create_pacient(pacient: Pacient):
    """
    ## ARGS
        - pacient: Pacient
    ## REPONSE
        - pacient: Pacient
    
    """
    return pac.create_pacient(pacient)

@router.put("/update_pacient", tags= ["Pacients"])
async def update_pacient(pacient: Pacient):
    """
    ## ARGS
        - pacient: Pacient
    ## REPONSE
        - pacient: Pacient
    
    """
    return pac.update_pacient(pacient)

@router.patch("/edit_pacient/", 
              status_code= status.HTTP_200_OK,
              response_model= Pacient,
              tags= ["Pacients"])
async def patch_pacient(pacient: UpdatePacient):
    """
    ## ARGS
        - pacient: Pacient
    ## REPONSE
        - pacient: Pacient
    
    """
    return pac.patch_pacient(pacient)

@router.delete("/delete_pacient/{pacient_id}", tags= ["Pacients"])
async def delete_pacient(pacient_id: int):
    """
    ## ARGS
        - pacient_id: int
    ## REPONSE
        - status: Http Status
    
    """
    return pac.delete_pacient(pacient_id)