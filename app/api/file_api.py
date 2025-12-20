from fastapi import APIRouter
from fastapi.params import Depends

from app.dependency.service_provider import medicine_approval_service_provider
from app.dto.approval.approval_response_dto import ApprovalResponseDto
from app.service.medicine.approval_service import ApprovalService
from app.util.file_util import create_file
from app.dependency import service_provider
router = APIRouter()

@router.post("/file/download/{id}")
def download_file(id:int,
                  service:ApprovalService = Depends(medicine_approval_service_provider)
                  ):
    ApprovalResponseDto
    create_file(id)
    return