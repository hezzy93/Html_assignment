
from fastapi import APIRouter
from schemas.appointment_schema import AppointmentsCreate, appointments

from services.appointment_service import AppointmentService


appointment_router = APIRouter()

@appointment_router.post('', status_code=201)
def create_appointment(payload: AppointmentsCreate):
    data = AppointmentService.create_appointment(payload)
    return {'message': 'success', 'data': data}


@appointment_router.get('', status_code=200)
def get_appointments():
    return {'message': 'success', 'data': appointments}

@appointment_router.get('/{appointment_id}')
def get_appointment_by_id(appointment_id: int):
    data = AppointmentService.get_appointment_by_id(payload)
    return {'message': 'success',  'data': data}