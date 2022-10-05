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
        self.values = [ '만족도 '+str(satisfaction), 
                       '연구기술력 '+str(research), 
                       '평판 '+str(evaluation), 
                       '학생 '+str(student)+'원', 
                       '예산 '+str(budget)+'원']
        self.turn           = str(turn)+'학기'
        self.texture_turn.set_image(self.turn, self.pos, self.center, self.margin_turn)
        
    def render(self):
        super().render()
        Game.render(self.texture_turn)
        