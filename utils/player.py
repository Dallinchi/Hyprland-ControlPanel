import subprocess

class Playerctl:
    @staticmethod
    def play_pause(player:str | None = None):
        command = f"playerctl -p {player} play-pause"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def play(player:str | None = None):
        command = f"playerctl -p {player} play"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def pause(player:str | None = None):
        command = f"playerctl -p {player} pause"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def status(player:str | None = None):
        command = f"playerctl -p {player} status"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
        
    @staticmethod
    def next(player:str | None = None):
        command = f"playerctl -p {player} next"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def previous(player:str | None = None):
        command = f"playerctl -p {player} previous"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def title(player:str | None = None):
        # Ты видишь кастыль? А он есть.
        # Ставим задержку, иначе в комбинации next/prev он показывает прошлый title
        command = f"sleep 0.1 && playerctl -p {player} metadata title"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def set_volume(player:str | None = None, value:float = 0):
        status = '+' if value > 0 else '-'
        
        command = f"playerctl -p {player} volume {abs(value)}{status}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
        
    @staticmethod
    def get_volume(player:str | None = None):
        command = f"playerctl -p {player} volume"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        return output[:-1]
    
    @staticmethod
    def players():
        command = f"playerctl -l"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        # Вывод этой команды показывает лишнее, отсекаем всё после точки
        return [player.split('.')[0] for player in output[:-1].split()]
    

        
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
        