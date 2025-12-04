from __future__ import annotations

from fastapi import APIRouter, HTTPException, status, Depends, Header
from google import genai
from google.genai.errors import APIError
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.service.medicine.medicine_service import MedicineService
from app.util.ai_util import get_ai_client
from app.service.patient.patient_service import PatientService
from typing import Optional
from app.util.database_util import get_db
from app.util.jwt_util import decode_token

import ast
import re

router = APIRouter(prefix="/ai", tags=["AI Recommendation"])

def get_patient_service(db: Session = Depends(get_db)):
    return PatientService(db)
def get_medicine_service(db: Session = Depends(get_db)):
    return MedicineService(db)


class AIRequest(BaseModel):
    medicine: str
    hospital_name: str
    patient_id: Optional[int] = None
    condition: Optional[str] = None



@router.post("/recommendations")
async def ai_drug_recommendation(
        request: AIRequest,
        patient_service: PatientService = Depends(get_patient_service),
        medical_service: MedicineService = Depends(get_medicine_service),

):

    # 환자 정보가 있을 경우
    if request.patient_id is not None:
        patient = patient_service.get_patient_by_id(request.patient_id)
        request.condition = patient.condition  # condition override

    client = get_ai_client()

    # 시스템 프롬프트
    system_instruction = (
        "당신은 응급 약물 전문의입니다. "
        "반드시 Python List 형식만 반환하세요. "
        "예: [\"DrugA\", \"DrugB\"] 영어로 반환해줘야합니다."
        "설명 문장은 절대 넣지 마세요."
        "3~4개 추천을 해주세요"
    )

    # 유저 프롬프트
    user_prompt = (
        f"Patient condition: {request.condition}. "
        f"Give similar INN drug components for: '{request.medicine}'. "
        "Return only python list."
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )

        raw = response.text
        # ```python ... ``` 제거
        cleaned = re.sub(r"```python|```", "", raw).strip()

        try:
            recommended_list = ast.literal_eval(cleaned)
            print("결과에 대한응답",recommended_list)
            res = medical_service.get_medicines_list(recommended_list,request.hospital_name)
            return res
        except Exception:
            recommended_list = []
            print("⚠️ AI 응답 파싱 실패:", cleaned)
            return  Exception
    except Exception as e:
        print("SERVER ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


# 외부 병원에 대한 ai 추천
@router.post("/medicine/recommendations")
async def ai_drug_recommendation(
        request: AIRequest,
        patient_service: PatientService = Depends(get_patient_service),
        medical_service: MedicineService = Depends(get_medicine_service)
):
    # 환자 정보가 있을 경우
    if request.patient_id is not None:
        patient = patient_service.get_patient_by_id(request.patient_id)
        request.condition = patient.condition  # condition override

    client = get_ai_client()

    # 시스템 프롬프트
    system_instruction = (
        "당신은 응급 약물 전문의입니다. "
        "반드시 Python List 형식만 반환하세요. "
        "예: [\"DrugA\", \"DrugB\"] 영어로 반환해줘야합니다."
        "설명 문장은 절대 넣지 마세요."
        "3~4개 추천을 해주세요"
    )

    # 유저 프롬프트
    user_prompt = (
        f"Patient condition: {request.condition}. "
        f"Give similar INN drug components for: '{request.medicine}'. "
        "Return only python list."
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )

        raw = response.text
        # ```python ... ``` 제거
        cleaned = re.sub(r"```python|```", "", raw).strip()

        # Python list 문자열 → 실제 list 변환
        try:
            recommended_list = ast.literal_eval(cleaned)
            print("결과에 대한응답",recommended_list)
            res = medical_service.get_medicines_list_not_hospital(recommended_list,request.hospital_name)
            print("데이터 조회 결과",res)
            return res
        except Exception:
            recommended_list = []
            print("⚠️ AI 응답 파싱 실패:", cleaned)
            return  Exception


    except APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini API 오류: {e.message}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"서버 오류: {str(e)}"
        )
