from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import UploadFile, File

from pathlib import Path
from os import system, popen
import re


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
