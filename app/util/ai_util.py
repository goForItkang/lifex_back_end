from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv
import os
from fastapi import HTTPException, status

# 환경 변수 로드
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# FastAPI 시작 시 클라이언트 객체를 생성하고 저장
try:
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")

    # 💡 클라이언트 객체 생성
    AI_CLIENT = genai.Client()
    print("Gemini AI Client 초기화")

except (ValueError, APIError) as e:
    print(f"Gemini 클라이언트 초기화 에러: {e}")
    AI_CLIENT = None
except Exception as e:
    print(f"에러: {e}")
    AI_CLIENT = None


def get_ai_client():
    if AI_CLIENT is None:

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI 서비스 서버 초기화에 실패했습니다. API 키를 확인하세요."
        )
    return AI_CLIENT