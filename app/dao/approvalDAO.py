from sqlalchemy import text


class ApprovalDAO:
    def __init__(self,db):
        self.db = db
    # 약물 요청에 대한
    def insert_medicine_reqeust_history(self, requester_user_id, requester_hospital_id,
                       response_hospital_id, stock_id, quantity):

        sql = text("""
               INSERT INTO medication_request_history (
                   requester_user_id,
                   requester_hospital_id,
                   response_hospital_id,
                   stock_id,
                   quantity,
                   status,
                   created_at
               )
               VALUES (
                          :requester_user_id,
                          :requester_hospital_id,
                          :response_hospital_id,
                          :stock_id,
                          :quantity,
                          'PENDING',
                          NOW()
                      )
               """)

        self.db.execute(sql, {
        "requester_user_id": requester_user_id,
        "requester_hospital_id": requester_hospital_id,
        "response_hospital_id": response_hospital_id,
        "stock_id": stock_id,
        "quantity": quantity
    })

        self.db.commit()
        return {"result": "SUCCESS"}

    def fin_by_hospital_id_get_request_history(self, hospital_id):
        sql = text("""
                   SELECT
                       r.id,
                       r.status,
                       r.requester_hospital_id,
                       requester_h.name AS requester_hospital_name,

                       r.response_hospital_id,
                       responder_h.name AS response_hospital_name,

                       r.quantity,
                       i.inn_name,
                       r.updated_at
                   FROM medication_request_history AS r
                            JOIN stock s
                                 ON r.stock_id = s.id
                            JOIN inn i
                                 ON s.inn_id = i.id
                            JOIN hospital requester_h
                                 ON r.requester_hospital_id = requester_h.id
                            JOIN hospital responder_h
                                 ON r.response_hospital_id = responder_h.id
                   WHERE r.response_hospital_id = :hospital_id
                      OR r.requester_hospital_id = :hospital_id
                   ORDER BY r.updated_at DESC
                   """)

        rows = self.db.execute(sql,{"hospital_id":hospital_id}).fetchall()
        return [dict(row._mapping) for row in rows]

    def find_by_hospital_id_get_pedding_medicine(self, hospital_id):
        sql = text("""
                   SELECT
                       m.id as id,
                       h.name AS hospital_name,
                       i.inn_name AS inn_name,
                       s.form AS form,
                       s.dosage AS dosage,
                       m.created_at AS created_at
                   FROM medication_request_history m
                            JOIN stock s ON m.stock_id = s.id
                            JOIN inn i ON s.inn_id = i.id
                            JOIN hospital h ON m.requester_hospital_id = h.id
                   WHERE m.status = 'PENDING'
                     AND m.response_hospital_id = :hospital_id;
        """)
        rows = self.db.execute(sql,{"hospital_id":hospital_id}).fetchall()
        return [dict(row._mapping) for row in rows]
        pass

    def update_reqeust_history(self, id, status, user_id):
        sql = text("""UPDATE medication_request_history SET status=:status, response_user_id=:user_id WHERE id=:id""")
        self.db.execute(sql,{"id":id,"status":status,"user_id":user_id})
        return self.db.commit()

