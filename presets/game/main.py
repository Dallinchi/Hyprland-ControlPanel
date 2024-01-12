from presets import BasePreset

class Preset(BasePreset):
    def __init__(self) -> None:
        super().__init__(name="Game")
    
    def start(self):
        print('Work is game')
                
    def finish(self):
        return super().finish()
        
    
            
    

