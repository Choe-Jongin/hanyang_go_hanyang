from obj import *

class Building_info(Obj):

    def __init__(self):
        super().__init__("building info")
        self.set_texture('images/ui/building_info.png')
        self.thumbnail = Obj("buding_thumb")
        self.thumbnail.texture.set_size((178,178))
        
        #info window
        self.target_pos = [Game.size[0]/2-900/2, Game.size[1]/2-480/2]
        self.pos[0] = -900
        self.pos[1] = self.target_pos[1]
        self.visible = False
        
        #content
        self.building = None
        self.thumbnail.pos = [self.pos[0] + 30, self.pos[1] + 10]
        self.close = Obj('close')
        self.close.pos[1] = self.pos[1]+10
        self.close.set_texture('images/ui/x.png')
        self.close_btn = Rect_Button(self.close.pos, [32,32])
        
        #text
        self.name = Texture_font('nanumgothic', 40, [0,0,0], True)
        self.margin_name = [280,10]
        self.dest = Texture_font('nanumgothic', 15, [0,0,0], True)
        self.margin_dest= [250,70]
        self.lv = Texture_font('nanumgothic', 15, [0,0,0], True)
        self.margin_lv = [20,210]
        
        self.font_satisfaction  = Texture_font('nanumgothic', 20, [0,0,0])
        self.font_research      = Texture_font('nanumgothic', 20, [0,0,0])
        self.font_evaluation    = Texture_font('nanumgothic', 20, [0,0,0])
        
    def update(self):
        if self.building == None :
            return 
        
        #화면에 보일땐 오른쪽으로 이동
        if self.visible:
            if self.pos[0] < self.target_pos[0] - 5:
                self.pos[0] += (self.target_pos[0]-self.pos[0])/3
            else :
                self.pos[0] = self.target_pos[0]
        #안 보여야 할 땐 왼쪽으로 이동
        else :
            if self.pos[0] > -910 + 5:
                self.pos[0] += (-910-self.pos[0])/3
            else :
                self.pos[0] = -910
            
        #content 같이 이동
        self.name.set_image(self.building.name.center(20, ' '),     self.pos, self.center, self.margin_name)
        self.dest.set_image(self.building.dest.center(70, ' '),     self.pos, self.center, self.margin_dest)
        self.lv.set_image(self.building.get_level().center(35, ' '),self.pos, self.center, self.margin_lv)
        self.thumbnail.pos = [self.pos[0] + 20, self.pos[1] + 20]
        self.close.pos[0] = self.pos[0]+860
        
        self.font_satisfaction.set_image('만족도 %d'%(self.building.satisfaction), self.pos, self.center, [20,300])
        self.font_research.set_image    ('연구기술력 %d'%(self.building.research),self.pos, self.center,  [20,330])
        self.font_evaluation.set_image  ('평판 %d'%(self.building.evaluation), self.pos, self.center,     [20,360])
        
        if self.visible:
            #close대기
            if self.close_btn.isClicked():
                self.visible = False
    
    def render(self):
        if self.isClosed():
            return ;
        super().render()
        self.thumbnail.render()
        self.close.render()
        Game.render(self.name)
        Game.render(self.dest)
        Game.render(self.lv)
        Game.render(self.font_satisfaction)
        Game.render(self.font_research)
        Game.render(self.font_evaluation)
        
        
    def set_building(self, building) :
        self.building = building
        self.thumbnail.texture.original_image = building.texture.original_image
        self.thumbnail.texture.set_size((178,178))
        self.visible = True
        
    def isClosed(self):
        return self.pos[0] <= -900
        
    def info_close(self):
        self.visible = False