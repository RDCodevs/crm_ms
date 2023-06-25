from pydantic import BaseModel
from datetime import date, datetime

class Medic(BaseModel):
    id: int
    gender: str
    name: str
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
    