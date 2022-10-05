from building import *

class Gate_Building(Building):
    def __init__(self):
        super().__init__("정문")
        self.level = 1
        self.max_level = 1
        self.set_texture('images/buildings/gate.png')
        self.pos = (855, 520)
        self.center = (30, 178)
        
    def update(self):
        pass
    
    