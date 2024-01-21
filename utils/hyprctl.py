import subprocess
import re
from os import listdir, path
from pathlib import Path
from random import choice

from utils import notify

def get_ration_monitor(reverse:bool) -> str:
    '''
    Возвращает ориентацию второго монитора (HDMI-A-1)
    '''
    output = subprocess.run(['hyprctl', 'monitors'], capture_output=True, text=True)
    transform = re.search(r"Monitor HDMI-A-1.*?transform: (\d+)", output.stdout.strip(), re.DOTALL)
    
    if transform:
        transform = int(transform.group(1))
        
        if transform:
            if reverse:
                return "16:9"
            return "9:16"
                
        if reverse:
            return "9:16"
        return "16:9"
    return ''

def change_background(path_to_wallpapers:Path=Path('/home/dallinchi/Pictures/Wallpapers/')):
    wallpapers = listdir(path_to_wallpapers.absolute())
    Dispatch.exec(f'swaybg -i {path_to_wallpapers.absolute()}/{choice(wallpapers)} -m fill')

        
class Dispatch:
    @staticmethod
    def exec(command:str):
        subprocess.run(['hyprctl', 'dispatch', 'exec', command], capture_output=True, text=True)

    @staticmethod
    def killactive():
        subprocess.run(['hyprctl', 'dispatch', 'killactive'], capture_output=True, text=True)
        
    @staticmethod
    def workspace(workspace:int):
        subprocess.run(['hyprctl', 'dispatch', 'workspace', str(workspace)], capture_output=True, text=True)
    
    @staticmethod
    def moveworkspacetomonitor(workspace:int, monitors:int):
        subprocess.run(['hyprctl', 'dispatch', 'moveworkspacetomonitor', str(workspace), str(monitors)], capture_output=True, text=True)