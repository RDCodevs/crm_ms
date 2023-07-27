from src.config.database import Session, engine, Base
from src.models.cites import Cites as CiteModel
from src.schemas.cites import Cites, ListCites, UpdateCite
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

Base.metadata.create_all(bind= engine)


def get_all_cites():
   db = Session()
   res = db.query(CiteModel).all()

   return JSONResponse(status_code= status.HTTP_200_OK,
                       content= jsonable_encoder(res))

def get_cite_by_id(id_cite: int):
   db = Session()
   res = db.query(CiteModel).filter(CiteModel.id_cite == id_cite).first()

   if not res:
      return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Cite not Found"})         

   return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))

def get_cite_by_patient_id(id_pacient: int):
   db = Session()
   res = db.query(CiteModel).filter(CiteModel.id_pacient == id_pacient).all()

   if not res:
      return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Cite not Found"})  
   
   return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))

def get_cites_by_medic_id(id_medic: int):
   db = Session()
   res = db.query(CiteModel).filter(CiteModel.id_medic == id_medic).all()

   if not res:
      return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Cite not Found"})  
   
   return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))


def create_cite(cite: Cites):
   db = Session()
   new_cite = CiteModel(**cite.dict())

   db.add(new_cite)
   db.commit()

   return cite.dict()

def patch_cite(cite: UpdateCite):
   db = Session()
   res = db.query(CiteModel).filter(CiteModel.id_cite == cite.id_cite).first()

   if not res:
      return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Cite not Found"})  

   cite_data = cite.dict(exclude_unset= True)

   for key, value in cite_data.items():
      setattr(res, key, value)

   result = res
   
   db.add(res)
   db.commit()
   db.refresh(res)

   return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(result))

def update_cite():
   pass

def delete_cite(id_cite: int):
   db = Session()
   res = db.query(CiteModel).filter(CiteModel.id_cite == id_cite).first()

   if not res:
      return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Cite not Found"}) 
   
   result = res

   db.delete(res)
   db.commit()

   return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(result))


