from src.config.database import Session, engine, Base
from src.models.cites import Cites as CiteModel
from src.schemas.cites import Cites
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

Base.metadata.create_all(bind= engine)


def get_all_cites():
    pass

def get_cite_by_id(id_cite):
  pass

def get_cite_by_patient_id(id_pacient):
  pass

def get_cites_by_medic_id(id_medic):
   pass

def create_cite(cite: Cites):
   db = Session()
   new_cite = CiteModel(**cite.dict())

   db.add(new_cite)
   db.commit()

   return cite.dict()

def patch_cite():
   pass

def update_cite():
   pass

def delete_cite(id_cite):
   pass
