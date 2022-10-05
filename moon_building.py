from building import *

class Moon_Building(Building):
    def __init__(self):
        super().__init__("경상/언론정보/국제문화")
        self.set_texture('images/buildings/moon.png')
        self.pos = (960, 389)
        self.center = (110, 178)
        self.set_effect(1,0,2)
        
        #info window
        self.info.set_building(self)
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 110, self.pos[1] - 36),
                        (self.pos[0] - 49, self.pos[1] - 100),
                        (self.pos[0] + 68, self.pos[1] - 37))
