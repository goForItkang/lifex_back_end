# auth/dependencies.py
from traceback import print_tb

from fastapi import Header, HTTPException, Depends
from starlette import status
from app.util.jwt_util import decode_token

# Authorization 헤더에서 토큰 추출
def get_current_user(authorization: str = Header(None)):
    print(decode_token(authorization))
    if authorization is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization Header"
        )

    try:
        payload = decode_token(authorization)
        return payload
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )


# 관리자(ROLE_ADMIN) 권한 검증
def get_admin_user(
        user: dict = Depends(get_current_user)
):
    if user.get("role") != "ROLE_ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return user


# 병원 권한 검증


