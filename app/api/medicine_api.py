# 약물에 대한 endPoint
from traceback import print_tb

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from app.dto.medicine.medicine_reqeust_dto import MedicineRequestDto
from app.service.medicine.approval_service import ApprovalService
from app.service.medicine.medicine_service import MedicineService
from app.util.database_util import get_db
from app.util.jwt_util import decode_token
from fastapi import Header
from app.dependency.service_provider import medicine_service_provider,medicine_approval_service_provider
#
router = APIRouter()

# def verify_token(authorization: str = Header(None)):
#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return authorization


# 외부병원 의약품 조회
@router.get("/medicines")
async def medicine(medicine:str,
    service: MedicineService = Depends(medicine_service_provider),
                   authorization: str = Header(None)
    ):
    if authorization is None:
        print("error401")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    hospital_id = decode_token(authorization)["hospital_id"]


    res = service.get_medicines(medicine,hospital_id)
    return res

# 내병원에 있는 의약품 조회
@router.get("/hospitals/medicines")
async def hospitalsInDrug(medicine:str,
                          authorization: str = Header(None),
    service : MedicineService = Depends(medicine_service_provider
                                        )
    ):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    print("병원 이름"+decode_token(authorization)['hospital'])

    hospital = decode_token(authorization)["hospital"]
    res = service.hospital_get_medicine(hospital,medicine)
    return res
# 병원에서 약물에 대한 요청
@router.post("/medicines-request")
def medicine_approval_request(
                            dto:MedicineRequestDto,
                            authorization: str = Header(None),
                            service:ApprovalService = Depends(medicine_approval_service_provider)
                       ):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    request_hospital_id = decode_token(authorization)["hospital_id"]
    request_doctor_id = decode_token(authorization)["id"]
    service.request_approval_medicine(request_hospital_id,
                                      request_doctor_id,
                                      dto)
    return
@router.get("/medicines-request")
def medicine_reqeust_list(
    authorization: str = Header(None),
    service:ApprovalService = Depends(medicine_approval_service_provider)
):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    hospital_id = decode_token(authorization)["hospital_id"]
    print("병원 ID 값 결과",hospital_id)
    res = service.request_medicine(hospital_id)

    return res

@router.get("/medicine/approval/pending")
def medicine_pending(
        authorization: str = Header(None),
        service:ApprovalService = Depends(medicine_approval_service_provider)
):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    role = decode_token(authorization)["role"]
    if role != "ROLE_PHARMACIST":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )

    hospital_id = decode_token(authorization)["hospital_id"]
    res = service.approval_pending(hospital_id)
    return res

@router.patch("/medicine/approval/{id}")
def medicine_approval(
        id:int,
        status:str,
        authorization: str = Header(None),
        service:ApprovalService = Depends(medicine_approval_service_provider)
):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    user_id = decode_token(authorization)["id"]
    service.approval_medicine(id,status,user_id)
    return

@router.get("/medicines-request/search")
def reqeust_medicine_by_inn(
        inn_name:str,
        authorization: str = Header(None),
        service:ApprovalService = Depends(medicine_approval_service_provider)
):
    hospital_id = decode_token(authorization)["hospital_id"]
    print("성분이름",inn_name)
    print("병원값 ",hospital_id)
    res = service.request_medicine_by_inn(inn_name,hospital_id)
    return res