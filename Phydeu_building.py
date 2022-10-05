from building import *

class Phydeu_Building(Building):
    def __init__(self):
        super().__init__("체육대학")
        self.level = 1
        self.max_level = 1
        self.set_texture('images/buildings/phyedu.png')
        self.pos = (457, 384)
        self.center = (110, 200)
                
    def update(self):
        pass
    
    