from pydantic import BaseModel
from datetime import date, datetime

class Medical_history(BaseModel):
    id: int
    patient: str
    creation_date: date
    last_update: date
    personal_history: str
    family_background: str
    current_drugs: str
    diagnoses: str
    treatments: str
    lab_reports: str
    observations:  str
