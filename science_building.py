from building import *

class Science_Building(Building):
    def __init__(self):
        super().__init__("과학기술대학")
        self.set_texture('images/buildings/science.png')
        self.pos = (875, 437)
        self.center = (110, 178)
        self.set_effect(2,1,0)
        
        #info window
        self.info.set_building(self)
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 110, self.pos[1] - 36),
                        (self.pos[0] - 49, self.pos[1] - 100),
                        (self.pos[0] + 68, self.pos[1] - 37))
