
from pydantic import BaseModel
from datetime import date, datetime

class Notification_System(BaseModel):
    notification_method: str
    addressee: str
    notification_content: str
    notification_status: str
    shipping_date: date
    notification_type: str  
    communication_channel: str

    