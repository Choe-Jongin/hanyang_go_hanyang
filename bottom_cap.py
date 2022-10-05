from obj import *

class Bottomcap(Obj):

    def __init__(self):
        super().__init__('bottomcap')
        self.set_texture('images/ui/bot_cap.png')
        self.texture_cap = Texture_font('nanumgothic', 40, [255,255,255], True)
        self.visible = True
        self.pos = [0, 720]
        self.center = [0, 85]
        self.margin_cap = [10,20]
        
    def update(self, str, visible):
        self.visible = visible
        if str != '':
            self.texture_cap.set_image(str, self.pos, self.center, self.margin_cap)
        else :
            self.visible = False
        
    def render(self):
        if self.visible:
            super().render()
            
            Game.render(self.texture_cap)
        self.visible = False