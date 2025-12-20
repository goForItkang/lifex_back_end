from pydantic import BaseModel


class HospitalResponseDto(BaseModel):
    hospital_id: int
    hospital_name: str
    hospital_address: str
    hospital_phone: str