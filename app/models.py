from pydantic import BaseModel

class SMSRequest(BaseModel):
    phone: str
    message: str