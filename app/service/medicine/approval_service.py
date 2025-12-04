# 약물 요청에 대한 승인
from app.dao.approvalDAO import ApprovalDAO
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



