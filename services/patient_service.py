from fastapi import HTTPException
from schemas.patient_schema import patients, Patients, PatientsCreate

class PatientService:

    @staticmethod
    def parse_patients(patient_data):
        data = []
        for pati in patient_data:
            data.append(patients[pati])
        return data
    
    @staticmethod
    def get_patient_by_id(patient_id):
        patient =patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        return patients[patient_id]
    
   
    @staticmethod
    def create_patient(patient_data: PatientsCreate):
        id = len(patients)
        patient = Patients(
            id=id,
            **patient_data.model_dump()
        )
        patients[id] = patient
        return patient

