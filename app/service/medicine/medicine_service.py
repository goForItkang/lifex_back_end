# drug service
from app.dao.medicine_dao import MedicineDAO
from sqlalchemy.orm import Session

from app.dto.medicine.medicine_response_dto import MedicineResponseDto


class MedicineService:
    def __init__(self,db:Session):
        self.dao = MedicineDAO(db)
    # 성분으로 조회하기
    def get_external_hospital_medicine(self,medicine:str,hospital_id:int):
        rows = self.dao.find_by_inn(medicine,hospital_id)
        return [MedicineResponseDto(**dict(row._mapping))for row in rows]
    # 본인 병원에서 약품 조회
    def get_internal_hospital_medicine(self, hospital, medicine):
        rows = self.dao.fnd_by_hospital_inn(medicine, hospital)
        return [MedicineResponseDto(**dict(row._mapping))for row in rows]
    # 본인 병원에서 AI에게 추천받은 약 성분 리스트
    def get_medicines_list(self, recommended_list, hospital:str):
        rows = self.dao.hospital_get_ai_recommend_inn(recommended_list, hospital)
        return [MedicineResponseDto(**dict(row._mapping))for row in rows]
    def get_medicines_list_not_hospital(self,recommended_list,hospital:str):
        rows = self.dao.hospital_not_get_ai_recommend_inn(recommended_list, hospital)
        return [MedicineResponseDto(**dict(row._mapping))for row in rows]

