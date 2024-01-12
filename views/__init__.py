from fastapi import APIRouter


# Для новой ветви создать отдельный модуль и создать в нем не завимый route, после сего соеденить его здесь
from .control_panel import router as control_panel_router

router = APIRouter()

router.include_router(
    control_panel_router,
                      )

