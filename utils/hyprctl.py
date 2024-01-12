from os import popen, system
import re

def get_ration_monitor(reverse:bool) -> str:
    '''
    Возвращает ориентацию второго монитора (HDMI-A-1)
    '''
    output = popen('hyprctl monitors').read()
    transform = re.search(r"Monitor HDMI-A-1.*?transform: (\d+)", output, re.DOTALL)
    
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
    system("change_background")
        
class Dispatch:
    @staticmethod
    def exec(command:str):
        system(f'hyprctl dispatch exec {command}')

    @staticmethod
    def killactive():
        system('hyprctl dispatch killactive')