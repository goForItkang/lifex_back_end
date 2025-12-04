from sqlalchemy.orm import Session

from app.dao.hospital_dao import HospitalDAO


class HospitalService:
    def __init__(self,db:Session):
        self.dao = HospitalDAO(db)

    def get_hospital(self, hospital):
        res = self.dao.find_by_name(hospital)
        return res
    # hospital 정보 구하는 로직
    # def get_hospital_status(self, hospital_name):
    #     # 환자 정보를 camera로 잡을 경우
    #     return
