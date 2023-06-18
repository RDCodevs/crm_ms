from pydantic import BaseModel

class Pacient(BaseModel):
    id: int
    name: str