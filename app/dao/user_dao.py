from sqlalchemy.engine import row
from sqlalchemy import text

class UserDAO:
    def __init__(self,db):
        self.db = db

    def find_by_login_id_and_password(self,login_id,password):
        sql = text("""select u.id,u.login_id,u.name,h.name as hospital_name,h.id as hospital_id,role.name as role
                      from user as u join hospital as h on h.id = u.hospital_id
                      join role on role.id = u.role_id
                      where login_id=:login_id and password=:password""")
        row =  self.db.execute(sql,{"login_id":login_id,"password":password}).fetchone()

        return dict(row._mapping)

    def save_user(self, login_id, password, phone, name, hospital_id, birth, url_name):
            sql = text("""
                       INSERT INTO user (hospital_id, login_id, password, phone, name, birth, license)
                       VALUES (:hospital_id, :login_id, :password, :phone, :name, :birth, :license_url)
                       """)
            self.db.execute(sql, {
                "hospital_id": hospital_id,
                "login_id": login_id,
                "password": password,
                "phone": phone,
                "name": name,
                "birth": birth,
                "license_url": url_name
            })

            self.db.commit()

