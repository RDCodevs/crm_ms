from pydantic import BaseModel
from datetime import date, datetime, time
from typing import List, Union
class Cites(BaseModel):
    query_type: str
    query_description: str
    site: str
    number_cite: str
    consulting_room: str
    horary: datetime
    id_patient: int # Una instancia de la clase "Paciente" que representa al paciente asociado a la cita.
    id_medic: int # Una instancia de la clase "Medico" que representa al médico asociado a la cita.
    state: str # El estado de la cita (por ejemplo, programada, confirmada, cancelada).
    admin: Union[int, None] # Una instancia de la clase "Admin" 
    assistant: Union[int, None] # Una instancia de la clase "Assistant"
    observations: str # Observaciones o notas adicionales sobre la cita.
    reminder_sent: bool # Un indicador para registrar si se ha enviado un recordatorio al paciente o no.
    registrado_por: Union[int, None] # El usuario que registró la cita en el sistema.
    created_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "query_type" : "Unkown",
                "query_description": "Content of the query",
                "site": "Centro de Salud Cojimies",
                "number_cite": "19242",
                "consulting_room": "2A",
                "horary": "",
                "id_patient": 1,
                "id_medic": 1,
                "state": "Programada",
                "admin": None,
                "assistant": None,
                "observations": "Observations to do after the cite",
                "reminder_sent": False,
                "register_by": None                
            }
        }

class ListCites(BaseModel):
    cites: List[Cites]

class UpdateCite(BaseModel):
    id_cite: int
    query_type: str
    query_description: str
    site: str
    number_cite: str
    consulting_room: str
    horary: datetime
    id_patient: int # Una instancia de la clase "Paciente" que representa al paciente asociado a la cita.
    id_medic: int # Una instancia de la clase "Medico" que representa al médico asociado a la cita.
    state: str # El estado de la cita (por ejemplo, programada, confirmada, cancelada).
    admin: Union[int, None] # Una instancia de la clase "Admin" 
    assistant: Union[int, None] # Una instancia de la clase "Assistant"
    observations: str # Observaciones o notas adicionales sobre la cita.
    reminder_sent: bool # Un indicador para registrar si se ha enviado un recordatorio al paciente o no.
    registrado_por: Union[int, None] # El usuario que registró la cita en el sistema.
    created_date: datetime
    
    class Config:
        schema_extra = {
            "example": {
                "id_cite": 1,
                "query_type" : "Unkown",
                "query_description": "Content of the query",
                "site": "Centro de Salud Cojimies",
                "number_cite": "19242",
                "consulting_room": "2A",
                "horary": "2013-10-07 08:23:19.120",
                "id_patient": 1,
                "id_medic": 1,
                "state": "Programada",
                "admin": None,
                "assistant": None,
                "observations": "Observations to do after the cite",
                "reminder_sent": False,
                "register_by": None                
            }
        }
