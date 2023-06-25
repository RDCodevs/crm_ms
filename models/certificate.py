from pydantic import BaseModel
from datetime import date, datetime

class Certificate(BaseModel):
    id: int
    code : int # El código único del certificado.
    broadcast_date: date # La fecha de emisión del certificado.
    autoridad_emisora: str # La autoridad o entidad responsable de emitir el certificado.
    type: str # El tipo de certificado (por ejemplo, médico, laboratorio, vacunación).
    description: str # Una descripción o información adicional sobre el certificado.
    valid_until: date # La fecha de vencimiento o validez del certificado.
    created_by: str # El usuario que creó el certificado.
    state: str # El estado actual del certificado (por ejemplo, activo, expirado, revocado).
    
    
    