# 로그인 사용되는 Dto
from pydantic import BaseModel

class LoginDTO(BaseModel):
    login_id : str # 사용자 id
    password : str # 사용자 패스워드



