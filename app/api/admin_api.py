from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Header
from sqlalchemy.orm import Session
from starlette import status

from app.service.amdin.admin_service import AdminService
from app.util.database_util import get_db
from app.util.jwt_util import decode_token
from app.dependency.service_provider import admin_service_provider
router = APIRouter()
# 관리자가 보는 승인 내역들

@router.get("/admin/medicine/approval")
def admin_medicine_approval(
        service:AdminService = Depends(admin_service_provider),
        authorization:str = Header(None)
):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
    )
    role = decode_token(authorization)["role"]
    if role != "ROLE_ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
    hospital_id = decode_token(authorization)["hospital_id"]
    res = service.find_all_by_hospital_id_request_medicine(hospital_id)

    return res
@router.get("/admin/medicine/approval/{id}")
def admin_medicine_approval_detail(
        id:int,
        service:AdminService = Depends(admin_service_provider),
        authorization:str = Header(None)
):
    print("받아온 ID",id)
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    role = decode_token(authorization)["role"]
    if  role != "ROLE_ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )

    res = service.find_by_id_request_medicine(id)
    print(res)
    return res

