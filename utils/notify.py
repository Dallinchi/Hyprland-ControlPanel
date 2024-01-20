import subprocess
    
def __notify(urgency:str):
    def send(text:str):
        subprocess.run(['notify-send', '-u', urgency, text], capture_output=True, text=True)

    return send


low = __notify('low')
normal = __notify('normal')
critical = __notify('critical')