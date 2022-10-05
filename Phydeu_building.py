from building import *

class Phydeu_Building(Building):
    def __init__(self):
        super().__init__("예체능대학", 1, 3)
        self.set_texture('images/buildings/phyedu.png')
        self.pos = (457, 384)
        self.center = (110, 200)
        self.levelup_cost = [0,4000,10000] 
        self.effect = [[0,0,0],[1,0,5],[2,1,7],[3,2,9]]
        self.set_lveffect()
        
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 90, self.pos[1] - 36),
                        (self.pos[0] + 30, self.pos[1] - 130),
                        (self.pos[0] + 110, self.pos[1] - 36))
        
        #한 줄 소개
        self.dest = '예체능 대학이 모여있다냥. 생각보다 예술, 체육인 선배들이 많으니 찾아보라냥!!'


        #info window
        self.info.set_building(self)
        self.levelup_btn = Obj('levelup_btn')
        self.levelup_btn.set_button([128,64])
        self.levelup_btn.set_texture('images/ui/box.png')
        self.levelup_btn.pos[1] = 505
        self.levelup_font = Texture_font('nanumgothic', 30, [0,0,0])
        self.caption = Texture_font('nanumgothic', 20, [0,0,0])
        
    def level_up(self):
        if Game.budget < self.levelup_cost[self.level] :
            return 'exceed budget'
        if self.level == self.max_level:
            return 'max level'
        Game.budget -= self.get_levelup_cost()
        self.level += 1
        self.set_lveffect()
        self.cost = 500*self.level
        return 0
        
    def update(self): 
        super().update()
        self.info.update()
        
        if self.level != self.max_level:
            self.levelup_btn.pos[0] = self.info.pos[0] + 700
            self.levelup_font.set_image( '레벨업', self.levelup_btn.pos, self.levelup_btn.center, [20,20])
            self.caption.set_image( '레벨 상승(%d냥) : 만족도 %d  연구기술 %d  평판 %d' %(
                                    self.get_levelup_cost(),
                                    self.effect[self.level+1][0],
                                    self.effect[self.level+1][1],
                                    self.effect[self.level+1][2]),
                                    self.info.pos, self.info.center, [300,200])
            if self.levelup_btn.isClicked():
                if self.level_up() != 0 :
                    Game.error.play(0)
        
    def render(self):
            super().render()
        
    def info_render(self):
        super().info_render()
        if self.level != self.max_level:
            self.levelup_btn.render()
            Game.render(self.levelup_font)
            Game.render(self.caption)