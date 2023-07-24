from src.config.database import Session, engine, Base
from src.models.pacients import Pacient as PacientModel
from src.schemas.pacients import Pacient, UpdatePacient
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

Base.metadata.create_all(bind= engine)

def get_pacient(pacient_id: int):
    db = Session()
    res = db.query(PacientModel).filter(PacientModel.id_pacient == pacient_id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Pacient not Found"})                        
    
    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))

def get_all_pacient():
    db = Session()
    res = db.query(PacientModel).all()

    return JSONResponse(status_code= status.HTTP_200_OK,
                        content= jsonable_encoder(res))

def create_pacient(pacient: Pacient):
    db = Session()
    new_pacient = PacientModel(**pacient.dict())

    db.add(new_pacient)
    db.commit()

    return pacient.dict()

def update_pacient(pacient):
    return

def patch_pacient(pacient: UpdatePacient):
    db = Session()
    print(pacient)
    res = db.query(PacientModel).filter(PacientModel.id_pacient == pacient.id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Pacient not Found"})

    pacient_data = pacient.dict(exclude_unset= True)

    for key, value in pacient_data.items():
        setattr(res, key, value)

    result = res

    db.add(res)
    db.commit()
    db.refresh(res)

    return JSONResponse(status_code= status.HTTP_200_OK, content=jsonable_encoder(result))

def delete_pacient(pacient_id: int):
    db = Session()
    res = db.query(PacientModel).filter(PacientModel.id_pacient == pacient_id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Pacient not Found"})
    
    result = res

    db.delete(res)
    db.commit()

    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(result))