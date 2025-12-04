from sqlalchemy.orm import Session

from app.dao import hospital_dao
from app.dao.hospital_dao import HospitalDAO
from app.dao.user_dao import UserDAO
from app.util.img_util import save_image
from app.util.jwt_util import create_access_token
class UserService:
    def __init__(self,db:Session):
        self.dao = UserDAO(db)
        self.hospital_dao = HospitalDAO(db)
    def login(self, dto):
        res = self.dao.find_by_login_id_and_password(dto.login_id,dto.password)
        token = create_access_token(res)

        return token
    # 회원가입
    def signup(self, login_id, password, phone, name, hospital, birth, licenseFile):
        url_name = save_image(licenseFile)
        hospital_id = self.hospital_dao.find_by_name_get_id(hospital)
        res = self.dao.save_user(login_id,password,phone,name,hospital_id,birth,url_name)
        # 의사 면허증에
        pass




