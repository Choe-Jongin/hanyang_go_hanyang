from scene import *

class Intro_Scene(Scene):
    
    def __init__(self):
        super().__init__("Intro Scene", 'images/intro/bg.png')
        
        self.s1 = Obj('s1')
        self.s1.set_texture('images/intro/s1.png')
        self.s1.texture.set_alpha(0)
        self.s1_stime = 20
        self.s1_etime = 100
            
        self.s2 = Obj('s2')
        self.s2.set_texture('images/intro/s2.png')
        self.s2.texture.set_alpha(0)
        self.s2_stime = 170
        self.s2_etime = 250
        
        self.bg = Obj('bg')
        self.bg.set_texture('images/title/bg.png')
        self.bg.texture.set_alpha(0)
        
        self.frame = 0
        
    def update(self):
        
        self.frame += 1
        
        if self.s1_stime < self.frame and self.frame < self.s1_etime :
            self.s1.texture.a += 2
            if self.s1.texture.a >100 :
                self.s1.texture.a = 100
            self.s1.texture.set_alpha()
            
        elif self.s1.texture.a > 0 :
            self.s1.texture.a -= 2
            if self.s1.texture.a < 0 :
                self.s1.texture.a = 0
            self.s1.texture.set_alpha()
            
        elif self.s2_stime < self.frame and self.frame < self.s2_etime :
            self.s2.texture.a += 2
            if self.s2.texture.a > 100 :
                self.s2.texture.a = 100
            self.s2.texture.set_alpha()
        
        elif self.s2.texture.a > 0 :
            self.s2.texture.a -= 2
            if self.s2.texture.a < 0 :
                self.s2.texture.a = 0
            self.s2.texture.set_alpha()
        elif 330 < self.frame and self.bg.texture.a < 95:
            self.bg.texture.a += 5
            self.bg.texture.set_alpha()
        elif 350 < self.frame :
            return 1
        return 0
        
    def render(self):
        super().render()
        self.s1.render()
        self.s2.render()
        self.bg.render()