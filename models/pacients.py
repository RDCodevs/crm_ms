from datetime import date, datetime
from pydantic import BaseModel

class Pacient(BaseModel):
    id: int
    gender: str
    name: str
    lastname: str
    weight: int
    height: int
    ethnicity: str
    allergies: str
    HTA: int # Hipertensión Arterial
    cie_code: int
    birthday: date     
    blood_type: str
    address: str
    phone: int

    

    











