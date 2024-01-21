from pathlib import Path
from time import sleep
from os import path

from presets import BasePreset
from utils import hyprctl, player
from utils import core

class Preset(BasePreset):
    def __init__(self) -> None:
        super().__init__(name="Work")
    
    def start(self):
        hyprctl.Dispatch.exec('[workspace 4] spotify')        
        sleep(5)
        hyprctl.Dispatch.moveworkspacetomonitor(4, 0)
        
        hyprctl.Dispatch.exec('[workspace 2] alacritty -o "window.startup_mode=Fullscreen" -e ranger')    
        sleep(2)
        hyprctl.Dispatch.moveworkspacetomonitor(2, 1)
        
        hyprctl.Dispatch.workspace(3)        
        hyprctl.Dispatch.moveworkspacetomonitor(3, 0)
        hyprctl.Dispatch.exec('code-oss')        
        hyprctl.change_background(path_to_wallpapers=Path(path.join(path.dirname(__file__), 'media','wallpapers')))
        player.Playerctl.play()
        
                
    def finish(self):
        core.close('electron')
        core.close('spotify')
        core.close('alacritty')
        hyprctl.change_background()
        player.Playerctl.pause()
        