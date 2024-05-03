import logging

from fastapi import APIRouter

from utils import player

router = APIRouter()
logger = logging.getLogger(__name__)


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


@router.get("/api/player/previous")
def _playerctl_previous():
    player.Playerctl.previous()
    return "successful"


@router.get("/api/player/title")
def _playerctl_title():
    title = player.Playerctl.title()
    return title


@router.get("/api/player/status")
def _playerctl_status():
    status = player.Playerctl.status()
    return status
