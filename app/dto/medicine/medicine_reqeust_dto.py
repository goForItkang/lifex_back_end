from pydantic import BaseModel
from typing import Optional
# 약 요청에 대한 부분 수정 필요
class MedicineRequestDto(BaseModel):
    hospital_id: int
    stock_id: int
    quantity: Optional[int] = 10

