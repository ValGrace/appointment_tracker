from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def create_appointment(db: Session, patient: schemas.PatientCreate):
    dupe_phone = db.query(models.Patient).filter(models.Patient.phone ==patient.phone).first()
    if dupe_phone:
        raise HTTPException(400, "Bad Request: Phone number is already registered")
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_appointment(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_appointment_by_doctor(db: Session, doctor_name: str):
    return db.query(models.Patient).filter(models.Patient.doctor == doctor_name).all()

def get_appointments(db: Session):
    return db.query(models.Patient).all()

def update_appointment(db: Session, patient_id: int, data: schemas.PatientUpdate):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        return None
    updated_apt = data.model_dump(exclude_unset=True)
    for field, value in updated_apt.items():
        setattr(patient, field, value)
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        return None
    db.delete(patient)
    db.commit()
    return patient