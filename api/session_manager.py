import logging

from fastapi import APIRouter

from utils import login


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
