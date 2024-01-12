from os import system

class Playerctl:
    @staticmethod
    def play_pouse():
        system("playerctl play-pause")
        
    @staticmethod
    def next():
        system("playerctl next")
        
class Amixer:
    @staticmethod
    def volume_up():
        system("amixer sset Master 2400+")
        
    @staticmethod
    def volume_down():
        system("amixer sset Master 2400-")