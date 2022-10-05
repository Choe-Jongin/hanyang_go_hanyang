from building import *

class Research_Building(Building):
    def __init__(self):
        super().__init__("연구단지",0,1)
        self.set_texture('images/buildings/tech.png')
        self.pos = (620, 600)
        self.center = (110, 178)
        self.set_effect(2,5,3)
        
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 110, self.pos[1] - 36),
                        (self.pos[0] - 49, self.pos[1] - 100),
                        (self.pos[0] + 68, self.pos[1] - 37))
        
        self.levelup_cost = [100000] 
        
        #info window
        self.info.set_building(self)
        self.levelup_btn = Obj('levelup_btn')
        self.levelup_btn.set_button([128,64])
        self.levelup_btn.set_texture('images/ui/box.png')
        self.levelup_btn.pos[1] = 505
        self.levelup_font = Texture_font('nanumgothic', 30, [0,0,0])
        self.caption = Texture_font('nanumgothic', 20, [0,0,0])
        
        #한 줄 소개
        self.dest = '각종 연구소, 실험단지가 입주해있다냥'
        
    def level_up(self):
        if Game.budget < self.levelup_cost[self.level] :
            return 'exceed budget'
        if self.level == self.max_level:
            return 'max level'
        Game.budget -= self.get_levelup_cost()
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