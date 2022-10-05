from building import *

class Camhub_Building(Building):
    def __init__(self):
        super().__init__("캠퍼스혁신파크",0,1)
        self.set_texture('images/buildings/camhub.png')
        self.pos = (330, 307)
        self.center = (110, 232)
        self.set_effect(10,10,10)
        
        #특수 충돌 범위
        self.rect_pos = (280, 140)
        self.button = Rect_Button( self.rect_pos, [130,130] )
        
        self.levelup_cost = [300000] 
        
        #info window
        self.info.set_building(self)
        self.levelup_btn = Obj('levelup_btn')
        self.levelup_btn.set_button([128,64])
        self.levelup_btn.set_texture('images/ui/box.png')
        self.levelup_btn.pos[1] = 505
        self.levelup_font = Texture_font('nanumgothic', 30, [0,0,0])
        self.caption = Texture_font('nanumgothic', 20, [0,0,0])
        
        #한 줄 소개
        self.dest = '정부의 캠퍼스혁신파크 선도사업에 선정되어, 카카오데이터 센터등 6900억원이 투입됩다냥!!'
        
    def level_up(self):
        if Game.budget < self.levelup_cost[self.level] :
            return 'exceed budget'
        if self.level == self.max_level:
            return 'max level'
        Game.budget -= self.get_levelup_cost()
        self.set_effect(10,10,10)
        self.level += 1
        return 0
        
    def update(self): 
        super().update()
        self.info.update()
        
        if self.level == 0 :
            self.levelup_btn.pos[0] = self.info.pos[0] + 700
            self.levelup_font.set_image( '레벨업', self.levelup_btn.pos, self.levelup_btn.center, [20,20])
            self.caption.set_image( '레벨1로 업그레이드시, 효과가 활성화 됩니다.('+str(self.get_levelup_cost())+'냥)', self.info.pos, self.info.center, [300,200])
            if self.levelup_btn.isClicked():
                if self.level_up() != 0 :
                    Game.error.play(0)
        
    def render(self):
            super().render()
        
    def info_render(self):
        super().info_render()
        if self.level == 0 :
            self.levelup_btn.render()
            Game.render(self.levelup_font)
            Game.render(self.caption)