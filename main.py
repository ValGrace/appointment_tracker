from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Patient Appointment Tracker",
    description="Track doctor appointments using fastapi",
    version="1.0.0"
    )

@app.post("/patients/", response_model=schemas.PatientResponse)
def create_appointment(patient: schemas.PatientCreate, db: Session = Depends(get_db)):

    return crud.create_appointment(db, patient)

@app.get("/patients/", response_model = List[schemas.PatientResponse])
def get_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)

@app.get("/patients/{patient_id}", response_model = schemas.PatientResponse)
def get_appointment(patient_id: int, db: Session = Depends(get_db)):
    appointment = crud.get_appointment(db, patient_id)
    if not appointment:
        raise HTTPException(404, "Patient appointment not found")
    return appointment

@app.get("/patients/doctor/{doctor_name}", response_model = List[schemas.PatientResponse])
def get_by_doctor(doctor_name: str, db: Session = Depends(get_db)):
    doctor_apts = crud.get_appointment_by_doctor(db, doctor_name)
    if not doctor_apts:
        raise HTTPException(404, f"Doctor {doctor_name} has no appointments")
    return doctor_apts

@app.put("/patients/{patient_id}", response_model = schemas.PatientResponse)
def update_appointment(patient_id: int, data: schemas.PatientUpdate, db: Session = Depends(get_db)):
    updated_appointment = crud.update_appointment(db, patient_id, data)
    if not updated_appointment:
        raise HTTPException(404, "Appointment details not updated")
    return updated_appointment

@app.delete("/patients/{patient_id}")
def delete_appointments(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.delete_patient(db, patient_id)
    if not patient:
        raise HTTPException(404, "Patient not found")
    return {
        "message": "Successfully deleted appointment"
    }