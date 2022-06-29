import bases

class Screen:
    def __init__(self, name: str):
        self.name = name
        self.objects: 'bases.Group' = bases.Group(f'{name}_objetos')
        self.isrunning = False