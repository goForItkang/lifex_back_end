from pydantic import BaseModel
from typing import Optional

class MedicineRequestDto(BaseModel):
    hospital_id: int
    stock_id: int
    quantity: Optional[int] = 10

