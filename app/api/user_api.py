from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.dto.user.user_login_dto import LoginDTO
from app.dto.user.user_signup_dto import SignupDTO
from fastapi import Form, File, UploadFile
from datetime import date
from app.service.user.user_service import UserService
from app.util.database_util import get_db
from app.dependency.service_provider import user_service_provider
router = APIRouter()


# 사용자 회원가입
@router.post("/signup",summary="사용자 회원가입")
def signup(
    login_id: str = Form(...),
    password: str = Form(...),
    phone: str = Form(...),
    name: str = Form(...),
    hospital: str = Form(...),
    birth: date = Form(...),
    licenseFile: UploadFile = File(...),
        service:UserService=Depends(user_service_provider)
):
    service.signup(login_id,password,phone,name,hospital,birth,licenseFile)
    return

# 사용자 로그인
@router.post("/login",summary="사용자 로그인")
def login(
        dto:LoginDTO,
        service:UserService=Depends(user_service_provider)
):
    print(dto)
    res = service.login(dto)
    return res