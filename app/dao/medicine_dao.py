from sqlalchemy import text

class MedicineDAO:
    def __init__(self, db):
        self.db = db

    def find_by_inn(self, medicine: str, hospital_id: int):
        sql = text("""
                   SELECT
                       s.id AS stock_id,
                       s.hospital_id AS hospital_id,
                       h.name AS hospital_name,
                       s.form AS form,
                       s.dosage AS dosage,
                       s.quantity AS quantity,
                       i.inn_name AS inn_name,
                       i.korean_name AS inn_korean_name
                   FROM stock AS s
                            JOIN inn AS i
                                 ON s.inn_id = i.id
                       join hospital as h ON h.id = s.hospital_id
                   WHERE
                       (i.inn_name LIKE :medicine OR i.korean_name LIKE :medicine)
                     AND s.hospital_id <> :hospital_id 
                       and s.quantity > 0 
                       and s.expire_date > now()
                   """)

        rows = self.db.execute(
            sql,
            {
                "medicine": f"%{medicine}%",
                "hospital_id": hospital_id
            }
        ).fetchall()

        return rows

    def fnd_by_hospital_inn(self, hospital, medicine):
        sql = text("""
                   SELECT
                       s.id AS stock_id,
                       s.hospital_id AS hospital_id,
                       s.form AS form,
                       s.dosage AS dosage,
                       s.quantity AS quantity,
                       i.id AS inn_id,
                       i.inn_name AS inn_name,
                       i.korean_name AS inn_korean_name
                   FROM stock AS s
                            JOIN inn AS i
                                 ON s.inn_id = i.id
                            JOIN hospital ON hospital.id = s.hospital_id
                   WHERE (i.inn_name LIKE :medicine OR i.korean_name LIKE :medicine)
                     AND hospital.name = :hospital
                    and s.quantity > 0 
                    and s.expire_date > now()
                   """)

        rows = self.db.execute(
            sql,
            {"hospital": hospital, "medicine": f"%{medicine}%"}
        ).fetchall()

        return rows

    def hospital_get_ai_recommend_inn(self, recommended_list, hospital):
        like_conditions = " OR ".join(
            [f"i.inn_name LIKE :p{i}" for i in range(len(recommended_list))]
        )
        sql = text(f"""
            SELECT
                s.id AS stock_id,
                s.hospital_id AS hospital_id,
                s.form AS form,
                s.dosage AS dosage,
                s.quantity AS quantity,
                s.expire_date AS expire_date,
                i.id AS inn_id,
                i.inn_name AS inn_name,
                i.korean_name AS korean_name
            FROM stock AS s
            JOIN inn AS i
                ON s.inn_id = i.id
            JOIN hospital
                ON hospital.id = s.hospital_id
            WHERE hospital.name = :hospital
              AND ({like_conditions})
        """)
        params = {"hospital": hospital}
        for idx, name in enumerate(recommended_list):
            params[f"p{idx}"] = f"%{name}%"

        rows = self.db.execute(sql, params).fetchall()

        return [dict(row._mapping) for row in rows]

    def hospital_not_get_ai_recommend_inn(self, recommended_list, hospital):


        like_conditions = " OR ".join(
            [f"i.inn_name LIKE :p{i}" for i in range(len(recommended_list))]
            )

        sql = text(f"""
            SELECT
                s.id AS stock_id,
                s.hospital_id AS hospital_id,
                s.form AS form,
                s.dosage AS dosage,
                s.quantity AS quantity,
                s.expire_date AS expire_date,
                i.id AS inn_id,
                i.inn_name AS inn_name,
                i.korean_name AS korean_name,
                h.name AS hospital_name
            FROM stock AS s
            JOIN inn AS i
                ON s.inn_id = i.id
            JOIN hospital AS h
                ON h.id = s.hospital_id
            WHERE h.name <> :hospital       
              AND ({like_conditions})       
        """)

        params = {"hospital": hospital}
        for idx, name in enumerate(recommended_list):
            params[f"p{idx}"] = f"%{name}%"

        rows = self.db.execute(sql, params).fetchall()

        return [dict(row._mapping) for row in rows]

