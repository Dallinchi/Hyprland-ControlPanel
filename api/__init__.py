from fastapi import APIRouter

# Для новой ветви создать отдельный модуль и создать в нем не завимый route, после сего соеденить его здесь
from .misc import router as misc_route
from .player import router as player_route
from .session_manager import router as session_manager_route

router = APIRouter()

router.include_router(misc_route)
router.include_router(player_route)
router.include_router(session_manager_route)