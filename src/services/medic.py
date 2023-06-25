from src.config.database import Session, engine, Base
from src.models.medic import Medic as MedicModel
from src.schemas.medic import Medic, UpdateMedic
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

Base.metadata.create_all(bind= engine)

def get_medic(medic_id: int):
    db = Session()
    res = db.query(MedicModel).filter(MedicModel.id_medic == medic_id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Medic not Found"})                        
    
    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))

def get_all_medic():
    db = Session()
    res = db.query(MedicModel).all()

    return JSONResponse(status_code= status.HTTP_200_OK,
                        content= jsonable_encoder(res))
    
def create_medic(medic: Medic):
    db = Session()
    new_medic = MedicModel(**medic.dict())

    db.add(new_medic)
    db.commit()

    return medic.dict()

def update_medic(medic):
    return

def patch_medic(medic: UpdateMedic):
    db = Session()
    res = db.query(MedicModel).filter(MedicModel.id_medic == medic.id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Medic not Found"})

    medic_data = medic.dict(exclude_unset= True)

    for key, value in medic_data.items():
        setattr(res, key, value)

    result = res

    db.add(res)
    db.commit()
    db.refresh(res)

    return JSONResponse(status_code= status.HTTP_200_OK, content=jsonable_encoder(result))


def delete_medic(medic_id: int):
    db = Session()
    res = db.query(MedicModel).filter(MedicModel.id_medic == medic_id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Medic not Found"})
    
    result = res

    db.delete(res)
    db.commit()

    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(result))
