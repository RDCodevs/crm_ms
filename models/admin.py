from pydantic import BaseModel

class Admin(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    phone: int
