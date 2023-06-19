from pydantic import BaseModel
from datetime import date, datetime

class Cites(BaseModel):
    id: int
    query_type: str
    query description: str
    site: str
    number_cite: int
    consulting_room: str
    horary: datetime
    date: date
    

    
