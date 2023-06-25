from pydantic import BaseModel
from datetime import date, datetime
from typing import List

class Medic(BaseModel):
    cedula: int
    name: str
    lastname: str
    gender: str
    specialty: str
    phone: int
    email: str
    medical_history: str
    address: str
    schedule: date # El horario de atención del médico. ?
    experience: str # La experiencia o años de práctica del médico.
    education: str # La información sobre la educación y formación académica del médico.
    certifications: str # Una lista de las certificaciones o reconocimientos obtenidos por el médico.
    consultation: str # Una lista de las consultas o citas asociadas al médico.
    
    
    class Config:
        schema_extra = {
            "example": {
                    "cedula": 1753497047,
                    "name": "Michael",
                    "lastname": "Mendoza",
                    "gender": "Male",
                    "specialty": "Obstetricia",
                    "phone": "0963615846",
                    "email": "killthmxall@gmail.com",
                    "medical_history": "None",
                    "address": "Jesus del Gran Poder, Cojimies y Colambo", 
                    "schedule": "None",
                    "experience": "None",    
                    "education": "Universidad Politecnica Salesiana",
                    "certifications": "None",
                    "consultation": "None"
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
    specialty: str
    phone: int
    email: str
    medical_history: str
    address: str
    schedule: date # El horario de atención del médico.
    experience: str # La experiencia o años de práctica del médico.
    education: str # La información sobre la educación y formación académica del médico.
    certifications: str # Una lista de las certificaciones o reconocimientos obtenidos por el médico.
    consultation: str # Una lista de las consultas o citas asociadas al médico.
    
    class Config:
        schema_extra = {
            "example": {
                    "id": 1,
                    "cedula": 1753497047,
                    "name": "Michael",
                    "lastname": "Mendoza",
                    "gender": "Male",
                    "specialty": "Obstetricia",
                    "phone": "0963615846",
                    "email": "killthmxall@gmail.com",
                    "medical_history": "None",
                    "address": "Jesus del Gran Poder, Cojimies y Colambo", 
                    "schedule": "None",
                    "experience": "None",    
                    "education": "Universidad Politecnica Salesiana",
                    "certifications": "None",
                    "consultation": "None"
            }
        } 
