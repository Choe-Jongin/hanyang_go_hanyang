from game import *

class Obj():
    
    def __init__(self, name="No name"):
        self.name = name
        self.x, self.y = 0, 0
        self.texture = Texture()
        
    def set_texture(self, filename):
        self.texture = Texture(filename)
        
    def render(self):
        Game.render(self.texture)