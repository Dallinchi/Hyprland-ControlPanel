import subprocess

from utils import notify

class Loginctl:
    @staticmethod
    def poweroff():
        notify.normal("Выключение")
        subprocess.run(['loginctl', 'poweroff'], capture_output=True, text=True)
    
    @staticmethod
    def reboot():
        notify.normal("Перезагрузка")
        subprocess.run(['loginctl', 'reboot'], capture_output=True, text=True)
        
        