from building import *

class Design_Building(Building):
    def __init__(self):
        super().__init__("예능대학")
        self.set_texture('images/buildings/design.png')
        self.pos = (619, 292)
        self.center = (110, 178)
        self.set_effect(3,0,1)
        
        #info window
        self.info.set_building(self)
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 110, self.pos[1] - 36),
                        (self.pos[0] - 49, self.pos[1] - 100),
                        (self.pos[0] + 68, self.pos[1] - 37))
    