import bases
import bases.interfaces as interfaces

class Screen(interfaces.ScreenInterface):
    def __init__(self, name: str):
        self.name = name
        self.objects: 'bases.Group' = bases.Group(f'{name}_objetos')
        self.isrunning = False