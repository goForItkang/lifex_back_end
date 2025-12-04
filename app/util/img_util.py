# 이미지 저장 util
import os
from dotenv import load_dotenv
from fastapi import UploadFile
from datetime import datetime
load_dotenv()

IMG_PATH = os.getenv("IMG_PATH")
# 이미지 저장할려는 디렉토리 위치
if not IMG_PATH:
    raise ValueError("환경변수가 설정 되지 않았습니다.")

os.makedirs(IMG_PATH, exist_ok=True)
def save_image(file: UploadFile):
    ext = file.filename.split(".")[-1]
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + "." + ext
    file_path = os.path.join(IMG_PATH, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return filename  # 또는 file_path
