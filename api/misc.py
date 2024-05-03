import logging

from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi import HTTPException

from utils import hyprctl, disk
from presets import get_presets

router = APIRouter()
logger = logging.getLogger(__name__)


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
