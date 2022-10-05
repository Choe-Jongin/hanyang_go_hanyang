from obj import *

class Topbar(Obj):

    def __init__(self):
        super().__init__('top bar')
        self.set_texture('images/ui/topbar.png')
        self.values = []
        self.texture_turn = Texture_font('nanumgothic', 40, [255,255,255], True)
        self.texture_value = Texture_font('nanumgothic', 20, [255,255,255])
        
        self.margin_turn = (15,45)
        
    def update(self, satisfaction, research, evaluation, student, budget, turn): 
        self.turn           = str(turn)+'학기'
        self.texture_turn.set_image(self.turn, self.pos, self.center, self.margin_turn)
        
        
        self.values = '만족도 %d      연구기술력 %d      평판 %d      학생수 %d명      예산 %d원'%(satisfaction, research, evaluation, student, budget)
        self.values = '%150s'%(self.values)
        self.texture_value.set_image(self.values, self.pos, self.center, (10,10))
        
    def render(self):
        super().render()
        Game.render(self.texture_turn)
        Game.render(self.texture_value)
        