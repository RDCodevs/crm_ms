from pydantic import BaseModel
from datetime import date, datetime

class User_management(BaseModel):
    user_name: str
    password: str
    rol: str
    permissions: str
    account_status: str
    activity_records: str
    admin: str
    assistant: str
    last_update: date
    logins: str