from fastapi import HTTPException
from schemas.doctors_schema import doctors, DoctorsCreate, Doctors

class DoctorService:

    @staticmethod
    def parse_doctors(doctor_data):
        data = []
        for doc in doctor_data:
            data.append(doctors[doc])
        return data
    

    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)   
        return doctors[doctor_id]
    
    
    @staticmethod
    def create_doctor(doctor_data: DoctorsCreate):
        id = len(doctors) +1
        doctor = Doctors(
            id=id,
            **doctor_data.model_dump()
            )
        doctors[id] = doctor
        return doctor
        

    