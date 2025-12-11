# 약물 요청에 대한 승인
from app.dao.approval_dao import ApprovalDAO
from app.dao.hospital_dao import HospitalDAO
from app.dto.medicine.medicine_reqeust_dto import MedicineRequestDto


class ApprovalService:
    def  __init__(self,db):
        self.dao = ApprovalDAO(db)
        self.hospital_dao = HospitalDAO(db)
    # 약물 요청 service

    def request_approval_medicine(self, reqeust_hospital_id,request_doctor_id,dto:MedicineRequestDto):

        self.dao.insert_medicine_reqeust_history(reqeust_hospital_id, request_doctor_id,dto.hospital_id,dto.stock_id,dto.quantity)

    def request_medicine(self, hospital_id):
        return self.dao.fin_by_hospital_id_get_request_history(hospital_id)

    def approval_pending(self, hospital_id):
        return self.dao.find_by_hospital_id_get_pedding_medicine(hospital_id)
        pass
    # 승인과 거절에 대한 응답서비스
    def approval_medicine(self, id, status, user_id):
        return self.dao.update_reqeust_history(id, status, user_id)
        pass

    def request_medicine_by_inn(self, inn_name,hospital_id):
        return self.dao.find_by_inn_name_reqeust_medicine(inn_name,hospital_id)
        pass






