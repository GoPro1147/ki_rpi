from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks
import os
from camera import takePicture

app = FastAPI()

def delete_file(file_path: str):
    if os.path.exists(file_path):  # 파일이 존재하는지 확인
        os.remove(file_path)  # 파일 삭제

@app.get("/get_image")
async def get_image(background_tasks: BackgroundTasks):
    image_path = takePicture()  # 이미지 파일 경로를 입력하세요.
    
    # 파일 응답 반환
    response = FileResponse(image_path)

    # 파일 삭제를 백그라운드 태스크로 등록
    background_tasks.add_task(delete_file, image_path)

    return response
