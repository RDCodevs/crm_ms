from pydantic import BaseModel
from datetime import date, datetime

class Cites(BaseModel):
    id: int
    query_type: str
    query_description: str
    site: str
    number_cite: int
    consulting_room: str
    horary: datetime
    date: date # La fecha de la cita.
    hour: datetime # La hora de la cita.
    patient: str # Una instancia de la clase "Paciente" que representa al paciente asociado a la cita.
    medic: str # Una instancia de la clase "Medico" que representa al médico asociado a la cita.
    state: str # El estado de la cita (por ejemplo, programada, confirmada, cancelada).
    admin: str # Una instancia de la clase "Admin" 
    assistant: str # Una instancia de la clase "Assistant"
    observations: str # Observaciones o notas adicionales sobre la cita.
    reminder_sent: str # Un indicador para registrar si se ha enviado un recordatorio al paciente o no.
    registrado_por: str # El usuario que registró la cita en el sistema.
    
    

    
