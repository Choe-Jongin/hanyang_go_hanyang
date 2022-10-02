from scene import *

class Game_Scene(Scene):
    
    def __init__(self):
        super().__init__("Game Scene")
        self.set_texture('images/background.png')
        self.texture.set_scale(Game.size)
        
        
    def update(self):
        pass

    def render(self):
        super().render()
        