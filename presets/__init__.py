import abc

class BasePreset(metaclass=abc.ABCMeta):
    def __init__(self, name:str) -> None:
        self.name = name 
    
    @abc.abstractmethod
    def start(self):
        print("Work!")

    @abc.abstractmethod
    def finish(self):
        print("Exit preset")


def get_presets() -> list[BasePreset]:
    from presets import work
    from presets import game
    
    # При добавлении нового пресета, импортируй и добавь в список ниже
    return [
        work.Preset(),
        game.Preset()
    ]

