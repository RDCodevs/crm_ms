from pydantic import BaseModel
from datetime import date, datetime, time
from typing import List, Union

class Medic(BaseModel):
    cedula: int
    name: str
    lastname: str
    gender: str
    speciality: str
    phone: int
    email: str
    address: str
    schedule_start: time # El horario de atención del médico. ?
    schedule_end: time
    experience: int # La experiencia o años de práctica del médico.
    certifications: Union[int, None] # Una lista de las certificaciones o reconocimientos obtenidos por el médico.
    
    
    class Config:
        schema_extra = {
            "example": {
                    "cedula": 1753497047,
                    "name": "Michael",
                    "lastname": "Mendoza",
                    "gender": "Male",
                    "speciality": "Obstetricia",
                    "phone": "0963615846",
                    "email": "killthmxall@gmail.com",
                    "address": "Jesus del Gran Poder, Cojimies y Colambo", 
                    "schedule_start": "08:00:00",
                    "schedule_end": "16:00:00",
                    "experience": 3,
                    "certifications": None,
            }
        } 


class ListMedic(BaseModel):
    medics: List[Medic]
    
class UpdateMedic(BaseModel):
    id: int
    cedula: int
    name: str
    lastname: str
    gender: str
    speciality: str
    phone: int
    email: str
    address: str
    schedule_start: time # El horario de atención del médico. ?
    schedule_end: time
    experience: int # La experiencia o años de práctica del médico.
    certifications: Union[int, None]
    
    class Config:
        schema_extra = {
            "example": {
                    "id": 1,
                    "cedula": 1753497047,
                    "name": "Michael",
                    "lastname": "Torrez",
                    "gender": "Male",
                    "speciality": "Obstetricia",
                    "phone": "0963615846",
                    "email": "killthmxall@gmail.com",
                    "address": "Jesus del Gran Poder, Cojimies y Colambo", 
                    "schedule_start": "08:00:00",
                    "schedule_end": "16:00:00",
                    "experience": 3,
                    "certifications": None,
            }
        } 
