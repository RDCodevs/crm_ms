
from pydantic import BaseModel

class Medic(BaseModel):
    id: int
    gender: str
    name: str
    specialty: str
    phone: int
    email: str
    medical_history: str

