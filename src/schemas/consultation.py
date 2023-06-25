from pydantic import BaseModel
from datetime import date, datetime

class consultation(BaseModel):
    date: date # La fecha de la cita.
    hour: datetime # La hora de la cita.
    patient: str # Una instancia de la clase "Paciente" que representa al paciente asociado a la cita.
    medic: str # Una instancia de la clase "Medico" que representa al médico asociado a la cita.
    reason: str # El motivo o razón de la consulta.
    diagnosis: str # El diagnóstico realizado durante la consulta.
    treatment: str # El tratamiento recomendado o prescrito durante la consulta.
    recipe: str # Una instancia de la clase "Receta" que representa la receta médica generada durante la consulta.
    observations: str # Observaciones adicionales sobre la consulta.
    registered_by: str # El usuario que registró la consulta en el sistema.
    
    
    