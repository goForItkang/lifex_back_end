from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Header
from sqlalchemy.orm import Session
from starlette import status

from app.service.amdin.admin_service import AdminService
from app.util.database_util import get_db
from app.util.jwt_util import decode_token
router = APIRouter()
# 관리자가 보는 승인 내역들


def get_admin_service(db:Session =Depends(get_db)):
    return AdminService(db)
@router.get("/admin/medicine/approval")
def admin_medicine_approval(
        service:AdminService = Depends(get_admin_service),
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

    return
