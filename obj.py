from game import *
from button import *

class Obj():
    
    def __init__(self, name="No name"):
        self.name = name
        self.pos    = [0, 0]
        self.center = [0, 0]
        self.texture = Texture()
        
    def set_texture(self, filename):
        self.texture = Texture(filename)
        
    def render(self, margin = [0,0]):
        self.texture.x = self.pos[0] + margin[0] - self.center[0]
        self.texture.y = self.pos[1] + margin[1] - self.center[1]
        Game.render(self.texture)
        
    def set_button(self, size):
        self.button = Rect_Button(self.pos, size)
        
    def overroll(self):
        return self.button.mouse_in(Game.m)
    
    def isClicked(self):
        return self.button.isClicked()