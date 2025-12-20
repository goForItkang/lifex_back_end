from typing import Optional
# 승인 요청에 대한 정보
class ApprovalRequestDto:
    approval_id : Optional[int] = None
    approval_status : str # DB default 값이 있음
    stock_id : int
    quantity : int
    reason : Optional[str] = None
