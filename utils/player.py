import subprocess

from utils import notify

class Playerctl:
    @staticmethod
    def play_pouse():
        subprocess.run(['playerctl', 'play-pause'], capture_output=True, text=True)
        notify.low("Плеер <|")
        
        
    @staticmethod
    def next():
        subprocess.run(['playerctl', 'next'], capture_output=True, text=True)
        notify.low("Плеер >>")
        
        
class Amixer:
    @staticmethod
    def volume_up():
        subprocess.run(['amixer', 'sset', 'Master', '2400+'], capture_output=True, text=True)
        notify.low("Громкость +")
        
        
    @staticmethod
    def volume_down():
        subprocess.run(['amixer', 'sset', 'Master', '2400-'], capture_output=True, text=True)
        notify.low("Громкость -")
        
        
        