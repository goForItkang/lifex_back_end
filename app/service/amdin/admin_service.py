from requests import Session

from app.dao.admin_dao import AdminDao


class AdminService:
    def __init__(self,db:Session):
        self.dao = AdminDao(db)

    def find_all_by_hospital_id_request_medicine(self, hospital_id):
        return self.dao.find_all_by_hospital_id_request_medicine(hospital_id)

    def find_by_id_request_medicine(self, id):
        return self.dao.find_by_id_request_medicine(id)


