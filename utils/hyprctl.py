import subprocess
import re

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

def change_background():
    subprocess.run(['change_background'], capture_output=True, text=True)

        
class Dispatch:
    @staticmethod
    def exec(command:str):
        subprocess.run(['hyprctl', 'dispatch', 'exec', command], capture_output=True, text=True)

    @staticmethod
    def killactive():
        subprocess.run(['hyprctl', 'dispatch', 'killactive'], capture_output=True, text=True)