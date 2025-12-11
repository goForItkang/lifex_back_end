# 약물 요청에 대한 승인
from app.dao.approval_dao import ApprovalDAO
from app.dao.hospital_dao import HospitalDAO
from app.dto.medicine.medicine_reqeust_dto import MedicineRequestDto


class ApprovalService:
    def  __init__(self,db):
        self.dao = ApprovalDAO(db)
        self.hospital_dao = HospitalDAO(db)
    # 약물 요청 service

    def request_medicine_approval(self, reqeust_hospital_id,request_doctor_id,dto:MedicineRequestDto):

        self.dao.insert_medicine_reqeust_history(reqeust_hospital_id, request_doctor_id,dto.hospital_id,dto.stock_id,dto.quantity)

    def get_medicine_reqeust_list(self, hospital_id):
        return self.dao.find_request_history_by_hospital_id(hospital_id)

    def get_medicine_request_pending(self, hospital_id):
        return self.dao.find_pending_requests(hospital_id)
        pass
    # 승인과 거절에 대한 응답서비스
    def status_update_medicine_request(self, id, status, user_id):
        return self.dao.update_request_status(id, status, user_id)
        pass

    def get_reqeust_medicine_by_inn(self, inn_name,hospital_id):
        return self.dao.find_requests_by_inn_name(inn_name,hospital_id)
        pass






