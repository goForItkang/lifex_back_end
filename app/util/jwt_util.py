#jwt(Json Web Token) 생성
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime,timedelta
# env에 있는 값 읽어오기
load_dotenv()
# 서명키
jwt_signing_key = os.getenv("JWT_SIGNING_KEY")
# 시크릿 키
jwt_secret_key = os.getenv("JWT_SECRET_KEY")
# 세션 정보
jwt_expire = int(os.getenv("JWT_EXPIRE"))

jwt_algorithm=os.getenv("JWT_ALGORITHM")
# token 생성
def create_access_token(dto):


    payload = {
        "id":dto["id"],
        "login_id":dto["login_id"],
        "name":dto["name"],
        "hospital":dto["hospital_name"],
        "hospital_id":dto["hospital_id"],
        "role" :"doctor",
        "exp": int((datetime.utcnow() + timedelta(minutes=jwt_expire)).timestamp())
    }

    token = jwt.encode(
        payload=payload,
        key=jwt_secret_key,
        algorithm=jwt_algorithm
    )
    return token

def decode_token(token: str):
    if token.startswith("Bearer "):
        token = token[len("Bearer "):]
    return jwt.decode(token, jwt_secret_key, algorithms=[jwt_algorithm])


def vaildate_token(token:str):
    return

