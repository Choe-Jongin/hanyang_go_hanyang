from building import *

class Phydeu_Building(Building):
    def __init__(self):
        super().__init__("체육대학")
        self.set_texture('images/buildings/phyedu.png')
        self.pos = (457, 384)
        self.center = (110, 200)
        self.set_effect(1,0,3)

        #info window
        self.info.set_building(self)
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 90, self.pos[1] - 36),
                        (self.pos[0] + 30, self.pos[1] - 130),
                        (self.pos[0] + 110, self.pos[1] - 36))
        