from fastapi import APIRouter, HTTPException, status

router = APIRouter()

from sqlalchemy.orm import Session
from fastapi.params import Depends

from app.service.patient.patient_service import PatientService
from app.util.database_util import get_db

def get_patient_service(db:Session = Depends(get_db)):
    return PatientService(db)
@router.get("/patients", summary="환자 조회 (전체/ID/이름/주민번호)")
def get_patients(
        patient_id: int = None,
        name: str = None,
        resident_number: str = None,
        service:PatientService = Depends(get_patient_service)
):
    #ID로 조회
    if patient_id is not None:
        res = service.get_patient_by_id(patient_id)
        return {"data": res}

    #이름으로 조회
    if name is not None:
        res = service.get_patient_by_name(name)
        return {"data": res}

    #주민번호로 조회
    if resident_number is not None:
        res = service.get_patient_by_resident_number(resident_number)
        return {"data": res}

    #아무 query도 없으면 전체 목록
    res = service.get_patient_list()
    return {"data": res}



