from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# .env 파일 로드
load_dotenv()

databaseURL = os.getenv("DB_URL")

if not databaseURL:
    raise ValueError("env 파일이 없거나 DB에 연결 할 수 없습니다.")

# Base 클래스 (모델 상속용)
Base = declarative_base()

# Engine 생성
engine = create_engine(
    databaseURL,
    echo=True,       # SQL 출력
    future=True
)

# DB 세션 생성기
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# FastAPI 의존성 주입용 DB 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
