from fastapi import APIRouter, status
from src.schemas.cites import Cites, ListCites, UpdateCite
from src.services import cites as cts

router = APIRouter(prefix= "/cites")

@router.get("/get_cite/{id_cite}", 
            tags=["Cites"],
            status_code= status.HTTP_200_OK,
            response_model= Cites)
async def get_cite_by_id(id_cite: int):
    """
      ## ARGS
        - id_cite: int
      ## RESPONSE
        - cite: Cite
    """
    return cts.get_cite_by_id(id_cite)

@router.get("/get_all", 
            tags=["Cites"],
            response_model= ListCites,
            status_code= status.HTTP_200_OK
            )
async def get_all_cite():
    """    
    ## RESPONSE
      - cites: List(Cites)
    """
    return cts.get_all_cites()

@router.get("/get_cite_pacient/{id_patient}",
            tags=["Cites"],
            response_model= Cites, 
            status_code= status.HTTP_200_OK)
async def get_cite_by_id_patient(id_patient: int):
    """
      ### ARGS
        -id_patient: int

      ### RESPONSE
        -cite: List(Cite)
    """
    return cts.get_cite_by_patient_id(id_patient)

@router.get("/get_cite_medic/{id_medic}",
            tags=["Cites"],
            response_model= Cites,
            status_code= status.HTTP_200_OK)
async def get_cite_by_medic_id(id_medic: int):
    """
      ## ARGS
        - id_medic: int
      ## RESPONSE
        - cite: List(Cite)
    """
    return cts.get_cites_by_medic_id(id_medic)

@router.post("/add_cite", 
             tags=["Cites"],
             status_code=status.HTTP_201_CREATED,
             response_model=Cites)
async def create_cite(cite: Cites):
    """
      ## ARGS
        - cite: Cites
      ## RESPONSE
        - cite: Cites
    """
    return cts.create_cite(cite)

@router.put("/update_cite", 
            tags=["Cites"],
            status_code= status.HTTP_200_OK,
            response_model= UpdateCite)
async def update_cite(cite: Cites):
    """
      ## ARGS
        - cite: Cites
      ## RESPONSE
        - cite: Cites
    """
    return cts.update_cite(cite)

@router.patch("/edit_cite", 
              tags=["Cites"],
              status_code= status.HTTP_200_OK,
              response_model= UpdateCite)
async def patch_cite(cite: UpdateCite):
    """
      ## ARGS
        - cite: UpdateCites
      ## RESPONSE
        - cite: Cites
    """
    return cts.patch_cite(cite)

@router.delete("/delete_cite/{cite_id}", 
               tags=["Cites"],
               status_code= status.HTTP_200_OK,
               response_model= Cites)
async def delete_cite(cite_id: int):
    """
      ## ARGS
        - cite: Cites
      ## RESPONSE
        - status: Http Status
    """
    return cts.delete_cite(cite_id)