from obj import *

class Building(Obj):
    def __init__(self, name, A=(0,0), B=(0,0), C=(0,0), D=(0,0)):
        super().__init__(name)
        self.level = 0
        self.max_level = 0
        self.button = Rhombus_Button(A, B, C, D)

    def set_button(self, A, B, C, D):
        self.button = Rhombus_Button(A, B, C, D)

    def update(self):
        pass
    
    def overroll(self):
        return self.button.mouse_in(Game.m)
    
    def isClicked(self):
        return self.button.isClicked()