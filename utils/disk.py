from fastapi import UploadFile
import shutil
import os

from utils import hyprctl, notify

# Директория сохранения файлов
UPLOAD_DIRECTORY = f"./media/uploads/"
# Доступное место в ГБ
ALLOCATED_SPACE = 5


def get_folder_size() -> float:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(UPLOAD_DIRECTORY):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 ** 3)

def _path_to_file(file_type:str, filename:str) -> str:
        _directory = f"{UPLOAD_DIRECTORY}{file_type}/"
        
        if not os.path.exists(_directory):
            os.makedirs(_directory)

        return os.path.abspath(_directory + str(filename))

def _check_to_usage_space(filesize:int) -> bool:
    if filesize / (1000 ** 3) + get_folder_size() < ALLOCATED_SPACE:
        return True
    return False
    
    
def save(file:UploadFile) -> dict: 
    if not _check_to_usage_space(file.size):
        notify.critical(f"No place - {file.filename}")
        return {"status": "no space"}
        
    file_type = file.headers.get('content-type')
    if file_type:
        file_type = file_type.split('/')[0]
    else:
        file_type = 'more'

    directory = _path_to_file(file_type, file.filename)
    
    with open(directory, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        notify.critical(f"Saved - {file.filename}")
        
    return {"status": "saved"}
    
