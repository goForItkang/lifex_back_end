from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Header
from sqlalchemy.orm import Session

from app.service.hospital.hospital_service import HospitalService
from app.util.database_util import get_db
import logging
from app.util.jwt_util import decode_token
from starlette import status

router=  APIRouter()

def get_hospital_service(db: Session=Depends(get_db)):
    return HospitalService(db)


# 내 병원에 조회
@router.get("/hospital/{hospital_name}")
def get_hospital(hospital_name:str,
                 service:HospitalService = Depends(get_hospital_service)
                 ,authorization: str = Header(None)
                 ):
    if authorization is None:
        print("error401")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    if hospital_name != decode_token(authorization)["hospital"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )

    res = service.get_hospital(hospital_name)

    return res
# @router.get("/api/hospitals/status/{hospital_name}")
# def get_hospital_status(hospital_name:str,
#                         service:HospitalService = Depends(get_hospital_service)):
#     print(hospital_name)
#     res = service.get_hospital_status(hospital_name)
#     return res