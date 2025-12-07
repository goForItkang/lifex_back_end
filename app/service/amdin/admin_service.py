from requests import Session

from app.dao.admin_dao import AdminDao


class AdminService:
    def __init__(self,db:Session):
        self.ado = AdminDao(db)


