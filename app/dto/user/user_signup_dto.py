# 로그인 사용되는 Dto
from pydantic import BaseModel
from datetime import date
class SignupDTO(BaseModel):
    login_id : str # 사용자 id
    password : str # 사용자 패스워드
    phone : str # 사용자 전화번호
    name : str # 사용자 이름
    hospital : str # 병원
    birth : date
    licenseFile: str # 라이센서 파일 URL 의사 자격증


