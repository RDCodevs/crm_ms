from pydantic import BaseModel

class User_management(BaseModel):
    user_name: str
    password: str
    rol: str
    permit: str
    account_status: str
