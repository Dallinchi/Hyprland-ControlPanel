from fastapi import APIRouter

# Для новой ветви создать отдельный модуль и создать в нем не завимый route, после сего соеденить его здесь
from .system import router as system_route

router = APIRouter()

router.include_router(
    system_route,
    )