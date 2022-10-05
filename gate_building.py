from building import *

class Gate_Building(Building):
    def __init__(self):
        super().__init__("정문")
        self.set_texture('images/buildings/gate.png')
        self.pos = (855, 520)
        self.center = (30, 178)
        self.set_effect(2,0,2)
    
        #info window
        self.info.set_building(self)