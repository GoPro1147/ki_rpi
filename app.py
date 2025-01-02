from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks
import os
from camera import takePicture

app = FastAPI()

if not os.path.exists('output'):
    os.makedirs('output')


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

@app.get("/get_test_image")
async def get_test_image():
    test_dir = 'test'  # 테스트 디렉토리
    test_files = os.listdir(test_dir)  # 테스트 디렉토리의 파일 목록
    
    if not test_files:
        return {"error": "테스트 디렉토리에 파일이 없습니다."}
    
    first_file_path = os.path.join(test_dir, test_files[0])  # 첫 번째 파일의 경로
    
    # 파일 응답 반환
    response = FileResponse(first_file_path)
    
    return response
