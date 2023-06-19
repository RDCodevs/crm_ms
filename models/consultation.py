from pydantic import BaseModel

class consultation(BaseModel):
    register : str
    prescription: str
    