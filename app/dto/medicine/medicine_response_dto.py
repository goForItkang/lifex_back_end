from pydantic import BaseModel
from typing import Optional

class MedicineResponseDto(BaseModel):
    stock_id:Optional[int] = None # 재고 number # 요청시 필요
    hospital_id:Optional[int] = None  # 병원 아이디
    hospital_name:Optional[str] = None # 병원 이름
    inn_name : str # 성분이름
    inn_korean_name : str # (한글)성분이름
    dosage : str #  복용량
    form :str # 재형
    quantity: int # 수량



