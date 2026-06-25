# Patient Appointment Tracker

## Overview
A simple REST API for managing doctor appointments and patient information. Built with FastAPI, it allows users to create, read, update, and delete patient appointment records.

## What It Does
This application provides a backend system to track patient appointments with doctors. Users can:
- Register new patient appointments
- Retrieve all appointments or search for specific ones
- Find appointments by doctor name
- Update appointment details (date, doctor, status, etc.)
- Cancel/delete appointments

## How It Works

### Technology Stack
- **FastAPI**: Web framework for building the REST API
- **SQLAlchemy**: ORM (Object-Relational Mapping) for database operations
- **SQLite**: Database for storing appointment records

### Key Components
1. **Models** (`models.py`): Defines the Patient database structure with fields like name, phone, doctor, appointment date, and status
2. **Schemas** (`schemas.py`): Pydantic models for data validation and API responses
3. **CRUD** (`crud.py`): Database operations (Create, Read, Update, Delete)
4. **Main** (`main.py`): API endpoints and application setup
5. **Database** (`database.py`): Database configuration and connection

### API Endpoints
- `POST /patients/` - Create a new appointment
- `GET /patients/` - Get all appointments
- `GET /patients/{patient_id}` - Get a specific patient's appointment
- `GET /patients/doctor/{doctor_name}` - Get all appointments for a doctor
- `PUT /patients/{patient_id}` - Update an appointment
- `DELETE /patients/{patient_id}` - Delete an appointment

## Running the Application
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`
