from obj import *

class Scene():
    def __init__(self, name, bgfilename):
        self.name = name
        self.bgimage = Obj("background image")
        self.bgimage.set_texture(bgfilename)
        self.bgimage.texture.set_size(Game.size)
        
    def update(self):
        pass
    
    def render(self):
        Game.render(self.bgimage.texture)
    