from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request

from templates import templates
from utils import disk

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def render_homepage(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "btns": [
                {"title": "Player", "action": "/player/"},
                {"title": "Loginctl", "action": "/loginctl/"},
                {"title": "Misc", "action": "/misc/"},
                {"title": "Presets", "action": "/presets/"},
                {"title": "Upload File", "action": "/upload/"},
            ],
        },
    )


@router.get("/loginctl", response_class=HTMLResponse)
async def render_powerpage(request: Request):
    return templates.TemplateResponse(
        "panel-btns.html",
        {
            "request": request,
            "btns": [
                {
                    "title": "Power OFF",
                    "action": [
                        "/api/loginctl/poweroff",
                    ],
                    "btn-id": [
                        "btn-system-poweroff",
                    ],
                    "btn-title": [
                        "",
                    ]
                },
                {
                    "title": "Reboot",
                    "action": [
                        "/api/loginctl/reboot",
                    ],
                    "btn-id": [
                        "btn-system-reboot",
                    ],
                    "btn-title": [
                        "",
                    ],
                },
            ],
        },
    )


@router.get("/player", response_class=HTMLResponse)
async def render_playerpage(request: Request):
    return templates.TemplateResponse(
        "panel-btns.html",
        {
            "request": request,
            "btns": [
                {
                    "title": "Play | Pouse",
                    "action": [
                        "/api/player/play-pouse",
                    ],
                    "btn-id": [
                        "btn-player-play-pouse",
                    ],
                    "btn-title": [
                        "",
                    ],
                },
                {
                    "title": "Next",
                    "action": [
                        "/api/player/next",
                    ],
                    "btn-id": [
                        "btn-player-next",
                    ],
                    "btn-title": [
                        "",
                    ],
                },
                {
                    "title": "Volume",
                    "action": [
                        "/api/player/volume/up",
                        "/api/player/volume/down",
                    ],
                    "btn-id": [
                        "btn-player-volume-up",
                        "btn-player-volume-down",
                    ],
                    "btn-title": ["+", "-"],
                },
            ],
        },
    )


@router.get("/misc", response_class=HTMLResponse)
async def render_miscpage(request: Request):
    return templates.TemplateResponse(
        "panel-btns.html",
        {
            "request": request,
            "btns": [
                {
                    "title": "Change background",
                    "action": [
                        "/api/change-background",
                    ],
                    "btn-id": [
                        "btn-change-background",
                    ],
                    "btn-title": [
                        " ",
                    ],
                },
                {
                    "title": "Kill Active Window",
                    "action": [
                        "/api/hyprctl/kill-active-window",
                    ],
                    "btn-id": [
                        "btn-kill-active-window",
                    ],
                    "btn-title": [
                        " ",
                    ],
                },
            ],
        },
    )


@router.get("/upload", response_class=HTMLResponse)
async def render_filepage(request: Request):
    return templates.TemplateResponse(
        "upload-form.html",
        {
            "request": request,
            "space": {
                "used": f"{disk.get_folder_size():.2f}",
                "space": disk.ALLOCATED_SPACE,
            } 
        },
    )
