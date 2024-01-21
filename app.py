from pathlib import Path
import logging

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from api import router as api_router
from views import router as views_router

app = FastAPI()

app.include_router(api_router)
app.include_router(views_router)

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)


logging_formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(logging_formatter)

# Настройка логгера для перехвата логов от uvicorn
uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.setLevel(logging.INFO)
uvicorn_file_handler = logging.FileHandler('control.log')
uvicorn_file_handler.setFormatter(formatter)
uvicorn_logger.addHandler(uvicorn_file_handler)

logger = logging.getLogger(__name__)

logging.basicConfig(filename='control.log', encoding='utf-8', level=logging.INFO, format=logging_formatter)

# Middleware для логов роутинга
@app.middleware("http")
async def log_route(request: Request, call_next):
    path = request.url.path
    method = request.method
    client = request.client
    logger.info(f"{client} {method} -> {path}")
    response = await call_next(request)
    return response

