from scene import *

class Ending_Scene(Scene):
    
    def __init__(self):
        super().__init__("Intro Scene", 'images/title/bg.png')
        
        self.clear = Obj('s1')
        self.clear.set_texture('images/ending/clear.png')
        self.clear.texture.set_alpha(0)

        self.fail = Obj('s1')
        self.fail.set_texture('images/ending/fail.png')
        self.fail.texture.set_alpha(0)
        
        self.font_satisfaction  = Texture_font('nanumgothic', 30, [0,0,0])
        self.font_research      = Texture_font('nanumgothic', 30, [0,0,0])
        self.font_evaluation    = Texture_font('nanumgothic', 30, [0,0,0])
        self.font_student       = Texture_font('nanumgothic', 30, [0,0,0])
        
        self.state = -1
        self.frame = 0
        self.finish = 0
        
    def update(self):
        
        self.frame += 1
        
        game_value = Game.ending_value
        self.state = Game.ending_value[0]
        self.font_satisfaction.set_image('만족도 %d'%(game_value[1]),    [0,0], [0,0], [150,300])
        self.font_research.set_image    ('연구기술력 %d'%(game_value[2]),[0,0], [0,0], [150,340])
        self.font_evaluation.set_image  ('평판 %d'%(game_value[3]),      [0,0], [0,0], [150,380])
        self.font_student.set_image     ('학생 수 %d'%(game_value[4]),   [0,0], [0,0], [150,420])
        
        if self.state == 0 :
            self.clear.texture.a += 5
            if self.clear.texture.a >= 100 :
                self.clear.texture.a = 100
                self.finish = 1
            self.clear.texture.set_alpha()
            
        if self.state == 1 :
            self.fail.render()
            self.fail.texture.a += 5
            if self.fail.texture.a >= 100 :
                self.fail.texture.a = 100
                self.finish = 1
            self.fail.texture.set_alpha()
            
        return 3
        
    def render(self):
        super().render()
        
        if self.state == 0 :
            self.clear.render()
        
        if self.state == 1 :
            self.fail.render()
        
        if self.finish == 1 :
            Game.render(self.font_satisfaction)
            Game.render(self.font_research)
            Game.render(self.font_evaluation)
            Game.render(self.font_student)