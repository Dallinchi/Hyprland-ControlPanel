from presets import BasePreset

class Preset(BasePreset):
    def __init__(self) -> None:
        super().__init__(name="Work")
    
    def start(self):
        print('Work is work')
                
    def finish(self):
        return super().finish()
        
    
            
    

