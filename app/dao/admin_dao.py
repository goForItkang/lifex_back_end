from sqlalchemy import text
class AdminDao:
    def __init__(self,db):
        self.db = db

    def find_all_by_hospital_id_request_medicine(self, hospital_id):
        sql = text("""
                   SELECT
                       mrh.id,
                       CASE
                           WHEN mrh.requester_hospital_id = :hospital_id THEN h_res.name
                           ELSE h_req.name
                           END AS other_hospital_name,
                       mrh.created_at,
                       mrh.updated_at,
                       i.korean_name AS inn_name
                   FROM medication_request_history mrh
                            JOIN stock s ON mrh.stock_id = s.id
                            JOIN inn i ON s.inn_id = i.id
                            JOIN hospital h_req ON mrh.requester_hospital_id = h_req.id
                            JOIN hospital h_res ON mrh.response_hospital_id = h_res.id
                   WHERE mrh.status = 'APPROVED'
                     AND (mrh.requester_hospital_id = :hospital_id OR mrh.response_hospital_id = :hospital_id)
                   """)

        rows = self.db.execute(sql, {"hospital_id": hospital_id}).fetchall()
        return [dict(row._mapping) for row in rows]

    def find_by_id_request_medicine(self, id):
        sql = text(""" 
            select * from medication_request_history where id=:id
        """)
        row = self.db.execute(sql,{"id":id}).fetchone()
        return dict(row._mapping)
