from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api.hospital_api import router
# 라우터 import (경로에 맞게 조정)
from app.api.medicine_api import router as medicine_router
from app.api.ai_api import router as ai_router
from app.api.patient_api import router as patient_router
from app.api.user_api import router as user_router
from app.api.hospital_api import router as hospital_router
import os
app = FastAPI()


origins = [
    "http://3.35.37.170",   # 프론트 도메인
    "http://localhost:3000" # 로컬 개발용 (원하면 추가)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(medicine_router,prefix="/api")
app.include_router(ai_router, prefix="/api")
app.include_router(patient_router,prefix="/api")
app.include_router(user_router,prefix="/api")
app.include_router(hospital_router,prefix="/api")

if __name__ == "__main__":
    # app/core/ai_client.py가 import 될 때 클라이언트 초기화가 먼저 진행됩니다.

    # 🚨 주의: Uvicorn을 직접 실행하는 코드는 배포 환경에서는 사용하지 않습니다.
    # 개발 환경 테스트용입니다.
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)