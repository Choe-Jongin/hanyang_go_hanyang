from building import *

class Dormy_Building(Building):
    def __init__(self):
        super().__init__("생활관(기숙사)")
        self.set_texture('images/buildings/dormy.png')
        self.pos = (400, 530)
        self.center = (110, 178)
        
        #info window
        self.info.set_building(self)
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 110, self.pos[1] - 36),
                        (self.pos[0] - 49, self.pos[1] - 100),
                        (self.pos[0] + 68, self.pos[1] - 37))
