from datetime import date, datetime
from pydantic import BaseModel
from typing import List

class Pacient(BaseModel):
    name: str
    lastname: str
    gender: str
    weight: float
    height: float
    ethnicity: str
    allergies: str
    HTA: int # Hipertensión Arterial
    cie_code: int
    birthday: date     
    blood_type: str
    address: str
    phone: int

    class Config:
        schema_extra = {
            "example": {
                    "name": "Stalin",
                    "lastname": "Pillajo",
                    "gender": "Male",
                    "weight": 17.05,
                    "height": 1.72,
                    "ethnicity": "Indigena",
                    "allergies": "None",
                    "HTA": 110, 
                    "cie_code": 123456,
                    "birthday": "2001-12-07",    
                    "blood_type": "O+",
                    "address": "Jesus del Gran Poder, Cojimies y Colambo",
                    "phone": "0961800096"
            }
        }

class ListPacient(BaseModel):
    pacients: List[Pacient]
    
class UpdatePacient(BaseModel):
    id: int
    gender: str
    name: str
    lastname: str
    weight: float
    height: float
    ethnicity: str
    allergies: str
    HTA: int # Hipertensión Arterial
    cie_code: int
    birthday: date     
    blood_type: str
    address: str
    phone: int

    class Config:
        schema_extra = {
            "example": {
                    "id": 1,
                    "name": "Stalin",
                    "lastname": "Pillajo",
                    "gender": "Male",
                    "weight": 17.05,
                    "height": 1.72,
                    "ethnicity": "Indigena",
                    "allergies": "None",
                    "HTA": 110, 
                    "cie_code": 123456,
                    "birthday": "2001-12-07" ,    
                    "blood_type": "O+",
                    "address": "Jesus del Gran Poder, Cojimies y Colambo",
                    "phone": "0961800096"
            }
        }