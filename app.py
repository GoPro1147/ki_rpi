import os

from fastapi import FastAPI, File
from fastapi.responses import FileResponse

from camera import takePicture


app = FastAPI()

# 이미지를 반환하는 엔드포인트
@app.get("/get_image")
async def get_image():

    # 여기서는 예시로 이미지 파일 경로를 지정합니다. 실제로는 원하는 이미지 파일을 선택해야 합니다.
    image_path = takePicture()  # 이미지 파일 경로를 입력하세요.
    response = FileResponse(image_path)
    os.remove(image_path)
    # 파일 응답 반환
    return response