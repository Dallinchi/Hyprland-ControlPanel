from os import system

class Loginctl:
    @staticmethod
    def poweroff():
        system("loginctl poweroff")
    
    @staticmethod
    def reboot():
        system("loginctl reboot")
        