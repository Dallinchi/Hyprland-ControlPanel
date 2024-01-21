import logging

from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi import HTTPException

from utils import hyprctl, player, login, disk
from presets import get_presets

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/api/loginctl/poweroff")
def _loginctl_poweroff():
    login.Loginctl.poweroff()
    return "successful"


@router.get("/api/loginctl/reboot")
def _loginctl_reboot():
    login.Loginctl.reboot()
    return "successful"


@router.get("/api/player/volume/up")
def _amixer_volume_up():
    player.Amixer.volume_up()
    return "successful"


@router.get("/api/player/volume/down")
def _amixer_volume_down():
    player.Amixer.volume_down()
    return "successful"


@router.get("/api/player/play-pouse")
def _playerctl_play_pause():
    player.Playerctl.play_pouse()
    return "successful"


@router.get("/api/player/next")
def _playerctl_next():
    player.Playerctl.next()
    return "successful"


@router.get("/api/change-background")
def _swaybg_change_background():
    hyprctl.change_background()
    return "successful"


@router.get("/api/hyprctl/kill-active-window")
def _hyprctl_dispatch_killactive():
    hyprctl.Dispatch.killactive()
    return "successful"


@router.get("/api/presets/{name:str}/{toggle:str}")
def _presets(name: str, toggle: str):
    if name not in [preset.name for preset in get_presets()]:
        raise HTTPException(status_code=404)
    if toggle not in ["off", "on"]:
        raise HTTPException(status_code=404)

    for preset in get_presets():
        if preset.name == name:
            match toggle:
                case "on":
                    preset.start()
                case "off":
                    preset.finish()

    return "succesfull"

@router.post("/api/upload")
def _upload_file(file: UploadFile = File(...)):
    saved = disk.save(file)

    match saved["status"]:
        case "no space":
            raise HTTPException(status_code=403, detail="No Space")

    return {"saved": saved["status"], "usedspace": f"{disk.get_folder_size():.2f}"}
