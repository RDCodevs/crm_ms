from src.config.database import Session, engine, Base
from src.models.cites import Cites as CiteModel
from src.schemas.cites import Cites, ListCites, UpdateCite
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

Base.metadata.create_all(bind= engine)

#----------------------------------------------------------------------------------------------------
def get_cite_by_id(id_cite: int):
    """
    Función que obtiene una cita por su ID.

    Args:
        id_cite (int): El ID de la cita.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_cite_by_id(1)
    JSONResponse(status_code=200, content={'id_cite': 1})
    
    >>> get_cite_by_id(999)
    JSONResponse(status_code=404, content={'message': 'Cite not Found'})
    """
    """
    db = Session()
    res = db.query(CiteModel).filter(CiteModel.id_cite == id_cite).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                    content= {"message": "Cite not Found"})         

    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))
    """

#----------------------------------------------------------------------------------------------------
def get_cite_by_patient_id(id_pacient: int):
    """
    Función que obtiene una cita por el ID del paciente.

    Args:
        id_pacient (int): El ID del paciente.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_cite_by_patient_id(1)
    JSONResponse(status_code=200, content={'id_pacient': 1})
    
    >>> get_cite_by_patient_id(999)
    JSONResponse(status_code=404, content={'message': 'Cite not Found'})
    """
    """
    db = Session()
    res = db.query(CiteModel).filter(CiteModel.id_pacient == id_pacient).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                    content= {"message": "Cite not Found"})  
    
    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))
    """

#----------------------------------------------------------------------------------------------------
def get_cites_by_medic_id(id_medic: int):
    """
    Función que obtiene todas las citas asociadas a un ID de médico.

    Args:
        id_medic (int): El ID del médico.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_cites_by_medic_id(1)
    JSONResponse(status_code=200, content=[{'id_medic': 1}, {'id_medic': 1}])
    
    >>> get_cites_by_medic_id(999)
    JSONResponse(status_code=404, content={'message': 'Cite not Found'})
    """
    """
    db = Session()
    res = db.query(CiteModel).filter(CiteModel.id_medic == id_medic).all()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                    content= {"message": "Cite not Found"})  
    
    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))
    """

#----------------------------------------------------------------------------------------------------
def create_cite(cite: Cites):
    """
    Función que crea una nueva cita en la base de datos.

    Args:
        cite (Cites): Objeto Cites con los datos de la cita a crear.

    Returns:
        Dict: Un diccionario con los datos de la cita creada.

    >>> create_cite(Cites())
    {'field1': 'value1', 'field2': 'value2'}
    """
    """
    db = Session()
    new_cite = CiteModel(**cite.dict())

    db.add(new_cite)
    db.commit()

    return cite.dict()
    """

#----------------------------------------------------------------------------------------------------
def patch_cite(cite: UpdateCite):
    """
    Función que actualiza una cita existente.

    Args:
        cite (UpdateCite): Objeto UpdateCite con los datos de la cita a actualizar.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la operación.

    >>> patch_cite(UpdateCite(id_cite=1, field1='value1', field2='value2'))
    JSONResponse(status_code=200, content={'id_cite': 1, 'field1': 'value1', 'field2': 'value2'})
    
    >>> patch_cite(UpdateCite(id_cite=999, field1='value1', field2='value2'))
    JSONResponse(status_code=404, content={'message': 'Cite not Found'})
    """
    """
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
    """

#----------------------------------------------------------------------------------------------------
def update_cite():
    """
    Función para actualizar una cita.

    >>> update_cite()
    'Cita actualizada correctamente'
    """
    #pass

#----------------------------------------------------------------------------------------------------
def delete_cite(id_cite: int):
    """
    Función que elimina una cita por su ID.

    Args:
        id_cite (int): El ID de la cita.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la eliminación.

    >>> delete_cite(1)
    JSONResponse(status_code=200, content={'id_cite': 1})
    
    >>> delete_cite(999)
    JSONResponse(status_code=404, content={'message': 'Cite not Found'})
    """
    """
    db = Session()
    res = db.query(CiteModel).filter(CiteModel.id_cite == id_cite).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                    content= {"message": "Cite not Found"}) 
    
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