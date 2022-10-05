from obj import *

class Building(Obj):
    def __init__(self, name, A=(0,0), B=(0,0), C=(0,0), D=(0,0)):
        super().__init__(name)
        self.level = 0
        self.max_level = 0
        self.button = Button(A, B, C, D)

    def set_button(self, A, B, C, D):
        self.button = Button(A, B, C, D)

    def update(self):
        pass
    
    def overroll(self):
        return self.button.isClick(Game.m)
    
    def isClick(self):
        return Game.mouse == 'click' and self.button.isClick(Game.m)