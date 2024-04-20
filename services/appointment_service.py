from fastapi import HTTPException

from schemas.appointment_schema import AppointmentsCreate, appointments, Appointments
from schemas.patient_schema import patients, Patients
from schemas.doctors_schema import doctors, Doctors

class AppointmentService:

    @staticmethod
    def create_appointment(payload: AppointmentsCreate):
        id = len(appointments)
        patient: Patients = patients[payload.patient]
        doctor: Doctors = doctor[payload.doctor]
        appointment = Appointments(
            id=id,
            patient=patient,
            doctor=doctor,
            date=payload.date
        )
        appointments.append(appointment)
        return appointment