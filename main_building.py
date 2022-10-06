from building import *

class Main_Building(Building):
    def __init__(self):
        super().__init__("본관 대학본부")
        self.set_texture('images/buildings/main.png')
        self.pos = (828, 317)
        self.center = (110, 178)
        self.set_effect(3,3,3)
        self.income_info = Texture_font('nanumgothic', 18, [0,0,0])
        self.estimate_income = Texture_font('nanumgothic', 18, [0,0,0])
        self.estimate_student = Texture_font('nanumgothic', 18, [0,0,0])
        
        #info window
        self.info.set_building(self)
        
        #feature
        self.scholarship = 0
        self.clean = 0
        self.effect_cost = 550
        
        self.scholarship_up = Obj('sc_up')
        self.scholarship_dn = Obj('sc_dn')
        self.scholarship_up.set_button([30,30])
        self.scholarship_dn.set_button([30,30])
        self.scholarship_up.set_texture('images/ui/arrow_up.png')
        self.scholarship_dn.set_texture('images/ui/arrow_down.png')
        self.scholarship_up.pos[1] = 405
        self.scholarship_dn.pos[1] = 425
        self.scholarship_font = Texture_font('nanumgothic', 20, [0,0,0])
        self.scholarship_cap_font = Texture_font('nanumgothic', 16, [0,0,0])
        
        self.clean_up = Obj('cl_up')
        self.clean_dn = Obj('cl_dn')
        self.clean_up.set_button([30,30])
        self.clean_dn.set_button([30,30])
        self.clean_up.set_texture('images/ui/arrow_up.png')
        self.clean_dn.set_texture('images/ui/arrow_down.png')
        self.clean_up.pos[1] = 405
        self.clean_dn.pos[1] = 425
        self.clean_font = Texture_font('nanumgothic', 20, [0,0,0])
        self.clean_cap_font = Texture_font('nanumgothic', 16, [0,0,0])
        
        self.set_button((self.pos[0], self.pos[1]),
                        (self.pos[0] - 110, self.pos[1] - 36),
                        (self.pos[0] - 49, self.pos[1] - 100),
                        (self.pos[0] + 68, self.pos[1] - 37))
        
        #한 줄 소개
        self.dest = '에리카 캠퍼스의 본관이다냥. 포토 스팟으로 좋으니 구경오라냥!!'
        
    def update(self): 
        super().update()
        self.info.update()
        
        self.income_info.set_image('예산 출처:[등록금 %d냥, 연구실적 %d냥], 지난학기 수입:%d냥'%
                            (Game.income_fee, Game.income_res, Game.income_prv),
                            self.info.pos, self.info.center, [230,150])
        self.estimate_income.set_image('다음 학기 예상 수입 : %d냥'%
                            (Game.estimate_income),
                            self.info.pos, self.info.center, [230,180])
        self.estimate_student.set_image('다음 학기 예상 정원 : %d명'%
                            (Game.estimate_student),
                            self.info.pos, self.info.center, [230,210])
        
        self.scholarship_up.pos[0] = self.info.pos[0] + 380
        self.scholarship_dn.pos[0] = self.info.pos[0] + 380
        self.clean_up.pos[0] = self.info.pos[0] + 610
        self.clean_dn.pos[0] = self.info.pos[0] + 610
        
        self.scholarship_font.set_image('장학금:'+str(self.scholarship), self.info.pos, self.info.center, [300,300])
        self.scholarship_cap_font.set_image('만족도:+'+str(self.scholarship)
                                        +' 지출:'+str(self.scholarship*self.get_active_cost(self.scholarship) )
                                        , self.info.pos, self.info.center, [290,340])
        self.clean_font.set_image('조경/미화:'+str(self.clean), self.info.pos, self.info.center, [500,300])
        self.clean_cap_font.set_image('평판:+'+str(self.clean)
                                        +' 지출:'+str(self.clean*self.get_active_cost(self.clean) )
                                        , self.info.pos, self.info.center, [490,340])
        
        if self.scholarship_up.isClicked():
            if self.scholarship < 9:
                self.scholarship += 1
        if self.scholarship_dn.isClicked():
            if self.scholarship > 0:
                self.scholarship -= 1
        if self.clean_up.isClicked():
            if self.clean < 9:
                self.clean += 1
        if self.clean_dn.isClicked():
            if self.clean > 0:
                self.clean -= 1

    def render(self):
        super().render()
        
    def info_render(self):
        super().info_render()
        Game.render(self.income_info)
        Game.render(self.estimate_income)
        Game.render(self.estimate_student)
        
        #buttons
        self.scholarship_up.render()
        self.scholarship_dn.render()
        self.clean_up.render()
        self.clean_dn.render()
        Game.render(self.scholarship_font)
        Game.render(self.scholarship_cap_font)
        Game.render(self.clean_font)    
        Game.render(self.clean_cap_font)    
        
    def get_active_cost(self, eff):
        return (10+eff)*self.effect_cost//10
        
    def get_cost(self):
        return (self.cost 
                + self.scholarship*self.get_active_cost(self.scholarship) 
                + self.clean*self.get_active_cost(self.clean) )
        
    def get_satisfaction(self):
        return self.satisfaction + self.scholarship
    
    def get_evaluation(self):
        return self.evaluation + self.clean
        