from building import *

class Camhub_Building(Building):
    def __init__(self):
        super().__init__("캠퍼스혁신파크")
        self.level = 1
        self.max_level = 1
        self.set_texture('images/buildings/camhub.png')
        self.pos = (330, 307)
        self.center = (110, 256)
        
    def update(self):
        pass
    
    