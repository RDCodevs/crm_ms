from src.config.database import Session, engine, Base
from src.models.pacients import Pacient as PacientModel
from src.schemas.pacients import Pacient, UpdatePacient
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

Base.metadata.create_all(bind= engine)

#----------------------------------------------------------------------------------------------------
def get_pacient(pacient_id: int):
    """
    Función que obtiene un paciente por su ID.

    Args:
        pacient_id (int): El ID del paciente.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_pacient(1)
    JSONResponse(status_code=200, content={'id_pacient': 1})
    
    >>> get_pacient(999)
    JSONResponse(status_code=404, content={'message': 'Pacient not Found'})
    """
    """
    db = Session()
    res = db.query(PacientModel).filter(PacientModel.id_pacient == pacient_id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Pacient not Found"})                        
    
    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))
    """
    
#----------------------------------------------------------------------------------------------------
def get_all_pacient():
    """
    Función que obtiene todos los pacientes.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_all_pacient()
    JSONResponse(status_code=200, content=[{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Smith'}])
    """
    """
    db = Session()
    res = db.query(PacientModel).all()

    return JSONResponse(status_code= status.HTTP_200_OK,
                        content= jsonable_encoder(res))
    """

#----------------------------------------------------------------------------------------------------
def create_pacient(pacient: Pacient):
    """
    Función que crea un nuevo paciente.

    Args:
        pacient (Pacient): Un objeto de tipo Pacient con los datos del paciente a crear.

    Returns:
        Dict: Un diccionario con los datos del paciente creado.

    >>> create_pacient(Pacient(name="John Doe", age=30))
    {'name': 'John Doe', 'age': 30}
    """
    """
    db = Session()
    new_pacient = PacientModel(**pacient.dict())

    db.add(new_pacient)
    db.commit()

    return pacient.dict()
    """

#----------------------------------------------------------------------------------------------------
def update_pacient(pacient):
    """
    Función que actualiza los datos de un paciente.

    Args:
        pacient (Pacient): Un objeto de tipo Pacient con los nuevos datos del paciente.

    Returns:
        None
    """
    #return

#----------------------------------------------------------------------------------------------------
def patch_pacient(pacient: UpdatePacient):
    """
    Función que actualiza los datos de un paciente.

    Args:
        pacient (UpdatePacient): Un objeto de tipo UpdatePacient con los datos actualizados del paciente.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la actualización.

    >>> patch_pacient(UpdatePacient(id=1, name="John Doe"))
    JSONResponse(status_code=200, content={'id': 1, 'name': 'John Doe', 'age': None})
    
    >>> patch_pacient(UpdatePacient(id=999, name="Jane Smith"))
    JSONResponse(status_code=404, content={'message': 'Pacient not Found'})
    """
    """"
    db = Session()
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
    """

#----------------------------------------------------------------------------------------------------
def delete_pacient(pacient_id: int):
    """
    Función que elimina un paciente por su ID.

    Args:
        pacient_id (int): El ID del paciente.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la eliminación.

    >>> delete_pacient(1)
    JSONResponse(status_code=200, content={'id_pacient': 1})
    
    >>> delete_pacient(999)
    JSONResponse(status_code=404, content={'message': 'Pacient not Found'})
    """
    """
    db = Session()
    res = db.query(PacientModel).filter(PacientModel.id_pacient == pacient_id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Pacient not Found"})
    
    result = res

    db.delete(res)
    db.commit()

    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(result))
    """
    
#----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    import doctest
    print("\n--- Correcto!\n")
    doctest.testmod()