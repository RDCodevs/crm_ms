from pydantic import BaseModel
import datetime

class Assistant(BaseModel):
    id: int
    gender: str
    name: str
    lastname: str
    phone: int
    supervisor_name: str
    email: str
    admin: str # Una instancia de la clase "Admin" que representa la conexión directa con el administrador.
    assigned_tasks: str # Una lista de las tareas asignadas al asistente por el administrador.
    available_time: datetime # El horario disponible del asistente para realizar tareas.
    last_connection: datetime # La fecha y hora de la última conexión del asistente al sistema.
    permissions: str # Una lista de los permisos o privilegios asignados al asistente por el administrador.
    completed_tasks: str # Una lista de las tareas completadas por el asistente.
    activity_records: str # Una lista de los registros o actividades realizadas por el asistente en el sistema.
