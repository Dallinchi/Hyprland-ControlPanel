import subprocess

from utils import notify

class Playerctl:
    @staticmethod
    def play_pouse():
        subprocess.run(['playerctl', 'play-pause'], capture_output=True, text=True)
    
    @staticmethod
    def play():
        subprocess.run(['playerctl', 'play'], capture_output=True, text=True)
        
    @staticmethod
    def pause():
        subprocess.run(['playerctl', 'pause'], capture_output=True, text=True)
        
    @staticmethod
    def status():
        status = subprocess.run(['playerctl', 'status'], capture_output=True, text=True)
        return status.stdout.strip()        
        
    @staticmethod
    def next():
        subprocess.run(['playerctl', 'next'], capture_output=True, text=True)
        
    @staticmethod
    def previous():
        subprocess.run(['playerctl', 'previous'], capture_output=True, text=True)
    
    @staticmethod
    def title():
        output = subprocess.run(['playerctl', 'metadata', 'title'], capture_output=True, text=True)
        return output.stdout

        
class Amixer:
    @staticmethod
    def volume_up():
        subprocess.run(['amixer', 'sset', 'Master', '2400+'], capture_output=True, text=True)
        
    @staticmethod
    def get_volume():
        command = "amixer get Master | grep -oP '\\d+%' | head -n1"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def volume_down():
        subprocess.run(['amixer', 'sset', 'Master', '2400-'], capture_output=True, text=True)
        
        
        