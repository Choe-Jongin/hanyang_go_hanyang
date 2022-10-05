from buding_info import Building_info
from obj import *

class Building(Obj):
    def __init__(self, name, level = 1, max_level = 1):
        super().__init__(name)
        self.level = level
        self.max_level = max_level
        self.button = Rhombus_Button([0,0],[0,0],[0,0],[0,0])
        self.info_textures = []
        self.set_effect(0,0,0)
        self.cost = 0
        self.levelup_cost = [0]
        self.dest = ''
        
        #info window
        self.info = Building_info()
        
    def set_button(self, A, B, C, D):
        self.button = Rhombus_Button(A, B, C, D)
        
    def set_effect(self, satisfaction, research, evaluation):
        self.satisfaction = satisfaction
        self.research = research
        self.evaluation = evaluation
        
    def set_lveffect(self):
        self.set_effect(self.effect[self.level][0], self.effect[self.level][1], self.effect[self.level][2])
        
    def show_info(self):
        self.info.visible = True
        
    def update(self):
        self.info.update()
    
    def info_render(self):
        self.info.render()
        
    #getters
    def get_satisfaction(self):
        if self.level == 0 :
            return 0
        return self.satisfaction
    
    def get_research(self):
        if self.level == 0 :
            return 0
        return self.research
    
    def get_evaluation(self):
        if self.level == 0 :
            return 0
        return self.evaluation
        
    def get_cost(self):
        return self.cost
    
    def get_levelup_cost(self):
        return self.levelup_cost[self.level]
    
    def get_level(self):
        if self.level == self.max_level:
            return 'LV MAX('+str(self.max_level)+')'
        return 'Lv.'+str(self.level)+'/'+str(self.max_level)

    def get_info(self):
        return self.info_textures
