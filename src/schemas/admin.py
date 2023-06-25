from pydantic import BaseModel
import datetime

class Admin(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    phone: int
    role: str
    creation_date: datetime # La fecha de creación del perfil de administrador.
    last_connection: datetime # La fecha y hora de la última conexión del administrador al sistema.
    permissions: str # Una lista de los permisos o privilegios asignados al administrador.
    assigned_doctors: str # Una lista de los médicos asignados o gestionados por el administrador.
    assigned_patients: str # Una lista de los pacientes asignados por el administrador.
    activity_logs: str # Una lista de los registros o actividades realizadas por el administrador en el sistema.
    
