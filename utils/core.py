import psutil

def close(name:str):
    # Находим процесс vs-code с помощью psutil
    for proc in psutil.process_iter(['pid', 'name']):
        if name in proc.name():
            # Отправляем сигнал SIGTERM (15) для закрытия процесса
            proc.send_signal(15)
