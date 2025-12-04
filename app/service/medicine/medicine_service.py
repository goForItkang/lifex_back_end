# drug service
from app.dao.medicine_dao import MedicineDAO
from sqlalchemy.orm import Session
class MedicineService:
    def __init__(self,db:Session):
        self.dao = MedicineDAO(db)
    # 성분으로 조회하기
    def get_medicines(self,medicine:str,hospital_id:int):
        return  self.dao.find_by_inn(medicine,hospital_id)
    # 본인 병원에서 약품 조회
    def hospital_get_medicine(self, hospital, medicine):
        return self.dao.fnd_by_hospital_inn(hospital, medicine)
    # 본인 병원에서 AI에게 추천받은 약 성분 리스트
    def get_medicines_list(self, recommended_list, hospital:str):
        return self.dao.hospital_get_ai_recommend_inn(recommended_list, hospital)
    def get_medicines_list_not_hospital(self,recommended_list,hospital:str):
        return self.dao.hospital_not_get_ai_recommend_inn(recommended_list, hospital)

