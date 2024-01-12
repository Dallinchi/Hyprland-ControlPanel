from os import system

    
def __notify(urgency:str):
    def send(text:str):
        system(f'notify-send -u "{urgency}" "{text}"')
    
    return send


low = __notify('low')
normal = __notify('normal')
critical = __notify('critical')