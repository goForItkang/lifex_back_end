from pydantic import BaseModel

#
class HospitalRequestDto(BaseModel):
    hospital_name: str
    hospital_address: str
    hospital_phone: str