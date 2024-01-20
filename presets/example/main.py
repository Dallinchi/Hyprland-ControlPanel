from presets import BasePreset

class Preset(BasePreset):
    def __init__(self) -> None:
        super().__init__(name="Example")
    
    def start(self):
        return super().start()
        
                
    def finish(self):
        return super().finish()
        