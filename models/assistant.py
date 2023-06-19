from pydantic import BaseModel

class Assistant(BaseModel):
    id: int
    gender: str
    name: str
    lastname: str
    phone: int
    supervisor_name: str
    email: str