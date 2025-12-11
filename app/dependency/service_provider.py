from fastapi import Depends
from fastapi import Depends
from sqlalchemy.orm import Session

from app.service.amdin.admin_service import AdminService
from app.service.medicine.approval_service import ApprovalService
from app.util.database_util import get_db
from app.service.hospital.hospital_service import HospitalService

# hospital ServiceProvider
def hospital_service_provider(db: Session = Depends(get_db)):
    service = HospitalService(db)
    try:
        yield service
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
# admin ServiceProvider
def admin_service_provider(db: Session = Depends(get_db)):
    service = AdminService(db)
    try:
        yield service
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
# 약물 승인 ServiceProvider
def medicine_approval_service_provider(db: Session = Depends(get_db)):
    service = ApprovalService(db)
    try:
        yield service
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
# 약물 ServiceProvider
def medicine_service_provider(db: Session = Depends(get_db)):
    service = ApprovalService(db)
    try:
        yield service
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
# user ServiceProvider
def user_service_provider(db: Session = Depends(get_db)):
    service = ApprovalService(db)
    try:
        yield service
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
# 환자 service provider
def patient_service_provider(db: Session = Depends(get_db)):
    service = ApprovalService(db)
    try:
        yield service
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()