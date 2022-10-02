from obj import *

class Building(Obj):
    def __init__(self, name):
        super().__init__(name)
        self.level = 0
        
    def update(self):
        pass
    