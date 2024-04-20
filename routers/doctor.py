from fastapi import APIRouter, Response

from schemas.doctors_schema import doctors, DoctorsCreate
from services.doctors_service import DoctorService

doctor_router = APIRouter()




@doctor_router.get("/",status_code=200)
def get_doctors():
    data = DoctorService.parse_doctors(doctor_data=doctors)
    return {'message': 'successful', 'data': data}


@doctor_router.get ('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'successful', 'data': data}


@doctor_router.post('', status_code=201)
def create_doctor(payload: DoctorsCreate ):
    data = DoctorService.create_doctor(payload)
    return {'message': 'created', 'data': data}