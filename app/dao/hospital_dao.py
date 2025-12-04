from sqlalchemy import text


class HospitalDAO:
    def __init__(self,db):
        self.db = db


    def find_by_name_get_id(self,name:str):
        sql = text("""select id from hospital where name=:name""")
        row = self.db.execute(sql,{"name":name}).fetchone()
        return row[0] if row else None

    def find_by_name(self, hospital):
        sql = text("""select * from hospital where name=:hospital""")
        row = self.db.execute(sql,{"hospital":hospital}).fetchone()

        return dict(row._mapping)


