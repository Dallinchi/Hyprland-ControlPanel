from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi import HTTPException

from utils import hyprctl, player, login, disk
from presets import get_presets

router = APIRouter()


@router.get("/api/loginctl/poweroff")
def _loginctl_poweroff():
    try:
        login.Loginctl.poweroff()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/loginctl/reboot")
def _loginctl_reboot():
    try:
        login.Loginctl.reboot()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/player/volume/up")
def _amixer_voluume_up():
    try:
        player.Amixer.volume_up()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/player/volume/down")
def _amixer_voluume_down():
    try:
        player.Amixer.volume_down()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/player/play-pouse")
def _playerctl_play_pause():
    try:
        player.Playerctl.play_pouse()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/player/next")
def _playerctl_next():
    try:
        player.Playerctl.next()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/change-background")
def _swaybg_change_background():
    try:
        hyprctl.change_background()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/hyprctl/kill-active-window")
def _hyprctl_dispatch_killactive():
    try:
        hyprctl.Dispatch.killactive()
        return "successful"
    except Exception as error:
        return error


@router.get("/api/test/preset")
def _test():
    try:
        for preset in get_presets():
            print(preset.name)
        return "successful"
    except Exception as error:
        return error


@router.post("/api/upload")
def _upload_file(file: UploadFile = File(...)):
    saved = disk.save(file)

    match saved['status']:
        case "no space":
            raise HTTPException(status_code=403, detail="No Space")
        
    return {
        "saved": saved,
        "usedspace": f"{disk.get_folder_size():.2f}"
    }
