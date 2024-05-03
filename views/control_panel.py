from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request
import presets

from templates import templates
from utils import disk, player

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def render_homepage(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Control panel",
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
async def render_session(request: Request):
    return templates.TemplateResponse(
        "session-manager.html",
        {
            "request": request,
            "title": "Session manager",
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
                    ],
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
async def render_player(request: Request):
    return templates.TemplateResponse(
        "player.html",
        {
            "request": request,
            "title": f"Player control \n {player.Playerctl.title()}",
            "btns": [
                {
                    "title": "Play | Pause",
                    "btns": [
                        {
                            "action": "/api/player/play-pouse",
                            "btn-id": "btn-player-play-pouse",
                            "btn-title": "",
                        },
                    ],
                },
                {
                    "title": "Prev | Next",
                    "btns": [
                        {
                            "action": "/api/player/previous",
                            "btn-id": "btn-player-previous",
                            "btn-title": "<-",
                        },
                        {
                            "action": "/api/player/next",
                            "btn-id":  "btn-player-next",
                            "btn-title": "->",
                        },
                    ],
                },
                {
                    "title": "Volume",
                    "btns": [
                        {
                            "action": "/api/player/volume/up",
                            "btn-id":  "btn-player-volume-up",
                            "btn-title": "+",
                        },
                        {
                            "action": "/api/player/volume/down",
                            "btn-id": "btn-player-volume-down",
                            "btn-title": "-",
                        },
                    ],
                },
            ],
        },
    )


@router.get("/misc", response_class=HTMLResponse)
async def render_misc(request: Request):
    return templates.TemplateResponse(
        "misc.html",
        {
            "request": request,
            "title": "Misc",
            "btns": [
                {
                    "title": "Change background",
                    "btns": [
                        {
                            "action": "/api/change-background",
                            "btn-id":  "btn-change-background",
                            "btn-title": "",
                        },
                    ],
                },
                {
                    "title": "Kill Active Window",
                    "btns": [
                        {
                            "action": "/api/hyprctl/kill-active-window",
                            "btn-id":  "btn-kill-active-window",
                            "btn-title": " ",
                        },
                    ],
                },
            ],
        },
    )


@router.get("/presets", response_class=HTMLResponse)
async def render_preset(request: Request):
    return templates.TemplateResponse(
        "presets.html",
        {
            "request": request,
            "btns": [
                {
                    "title": btn.name,
                    "btns": [
                        {
                            "action": "/api/presets/{btn.name}/on",
                            "btn-id":  "btn-preset-{btn.name}-on",
                            "btn-title": "on",
                        },
                        {
                            "action": "/api/presets/{btn.name}/off",
                            "btn-id":  "btn-preset-{btn.name}-off",
                            "btn-title": "off",
                        },
                    ],
                }
                for btn in presets.get_presets()
            ],
        },
    )


@router.get("/upload", response_class=HTMLResponse)
async def render_sharefiles(request: Request):
    return templates.TemplateResponse(
        "upload-form.html",
        {
            "request": request,
            "space": {
                "used": f"{disk.get_folder_size():.2f}",
                "space": disk.ALLOCATED_SPACE,
            },
        },
    )
