# 약물에 대한 endPoint
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
#
router = APIRouter()

# def verify_token(authorization: str = Header(None)):
#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return authorization

def get_medicine_service(db: Session = Depends(get_db)):
    return MedicineService(db)

def get_medicine_approval_service(db: Session = Depends(get_db)):
    return ApprovalService(db)
# 외부병원 의약품 조회
@router.get("/medicines")
async def medicine(medicine:str,
    service: MedicineService = Depends(get_medicine_service),
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
@router.get("/hospitals/{hospital}/medicines")
async def hospitalsInDrug(hospital:str,medicine:str,
                          authorization: str = Header(None),
    service : MedicineService = Depends(get_medicine_service
                                        )
    ):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    res = service.hospital_get_medicine(hospital,medicine)
    return res
# 병원에서 약물에 대한 요청
@router.post("/medicines-request")
def medicine_approval_request(
                            dto:MedicineRequestDto,
                            authorization: str = Header(None),
                            service:ApprovalService = Depends(get_medicine_approval_service)
                       ):
    request_hospital_id = decode_token(authorization)["hospital_id"]
    request_doctor_id = decode_token(authorization)["id"]
    service.request_approval_medicine(request_hospital_id,
                                      request_doctor_id,
                                      dto)
    return "요청이 완료되었습니다."
@router.get("/medicines-request")
def medicine_reqeust_list(
    hospital_id:int,
    service:ApprovalService = Depends(get_medicine_approval_service)
):
    print(hospital_id)
    res = service.request_medicine(hospital_id)
    print(res)
    return res


