from pydantic import BaseModel
from typing import Optional

class PatientCreate(BaseModel):
    name: str
    phone: str
    doctor: str
    appointment_date: str
    status: Optional[str] = "scheduled"

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    doctor: Optional[str] = None
    appointment_date: Optional[str] = None

class PatientResponse(BaseModel):
    name: str
    phone: str
    doctor: str
    appointment_date: str
    status: str

    class Config:
        from_attributes = True
        orm_mode = True
