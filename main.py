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
from app.api.admin_api import router as admin_router
import os
app = FastAPI()


origins = [
    "http://3.35.37.170",   # 프론트 도메인
    "http://localhost:3000" # 개발 도메인
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
app.include_router(admin_router,prefix="/api")
if __name__ == "__main__":

    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)