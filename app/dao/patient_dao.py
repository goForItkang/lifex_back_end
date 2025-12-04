from sqlalchemy import text

class PatientDAO:
    def __init__(self,db):
        self.db = db
    # 미 완성 코드
    def find_by_patient_id(self, patient_id):
        sql = text("""
        select * from patient where id=:patient_id
        """)
        return self.db.execute(sql,{"patient_id":patient_id}).fetchone()

    def find_all_patient_id(self):
        sql = text("""
        select * from patient
        """)
        res = self.db.execute(sql).fetchall()
        return [dict(res._mapping)]

    def find_by_patient_resident_number(self, resident_number):
        sql = text("""
        select * from patient where resident_number=:resident_number
        """)
        rows = self.db.execute(sql,{"resident_number":resident_number}).fetchall()

        return [dict(r._mapping) for r in rows]

    def find_by_patient_name(self, name):
        sql = text("""
        select * from patient where name=:name
        """)
        rows = self.db.execute(sql,{"name":name}).fetchall()

        return [dict(r._mapping) for r in rows]
