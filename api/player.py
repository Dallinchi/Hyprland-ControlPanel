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

@router.get("/api/player/players")
def _playerctl_players():
    players = player.Playerctl.players()
    return players

@router.get("/api/player/{_player}/play-pause")
def _playerctl_play_pause(_player:str):
    player.Playerctl.play_pause(player=_player)
    return "successful"


@router.get("/api/player/{_player}/next")
def _playerctl_next(_player:str):
    player.Playerctl.next(player=_player)
    return "successful"


@router.get("/api/player/{_player}/previous")
def _playerctl_previous(_player:str):
    player.Playerctl.previous(player=_player)
    return "successful"


@router.get("/api/player/{_player}/volume")
def _playerctl_get_volume(_player:str):
    volume = player.Playerctl.get_volume(player=_player)
    return volume


@router.get("/api/player/{_player}/volume/{volume}")
def _playerctl_set_volume(_player:str, volume:float):
    player.Playerctl.set_volume(player=_player, value=volume)
    return "successful"


@router.get("/api/player/{_player}/title")
def _playerctl_title(_player:str):
    title = player.Playerctl.title(player=_player)
    return title


@router.get("/api/player/{_player}/status")
def _playerctl_status(_player:str):
    status = player.Playerctl.status(player=_player)
    return status



