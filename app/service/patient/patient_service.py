
from sqlalchemy.orm import Session

from app.dao.patient_dao import PatientDAO


class PatientService:
    def __init__(self,db:Session):
        self.dao = PatientDAO(db)
    def get_patient_by_id(self,patient_id):
        return self.dao.find_by_patient_id(patient_id)

    def get_patient_list(self):
        return self.dao.find_all_patient_id()

    def get_patient_by_resident_number(self, resident_number):
        return self.dao.find_by_patient_resident_number(resident_number)
        pass

    def get_patient_by_name(self, name):
        return self.dao.find_by_patient_name(name)

