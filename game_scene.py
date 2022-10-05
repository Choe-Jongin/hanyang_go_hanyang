
from bottom_cap import Bottomcap
from buding_info import Building_info
from building import *
from Phydeu_building import Phydeu_Building
from camhub_building import Camhub_Building
from dormy_building import Dormy_Building
from gate_building import Gate_Building
from moon_building import Moon_Building
from eng_building import Engineer_Building
from main_building import Main_Building
from design_building import Design_Building
from lib_building import Lib_Building
from research_building import Research_Building
from sw_building import Sw_Building
from science_building import Science_Building
from techno_building import Techno_Building
from welfare_building import Welfare_Building

from scene import *
from topbar import *

class Game_Scene(Scene):
    
    def __init__(self):
        super().__init__("Game Scene", 'images/background.png')
        
        #the univ values and in game values
        self.satisfaction   = 50
        self.research       = 50
        self.evaluation     = 50
        
        self.student        = 1000
        self.budget         = 10000
        self.cost           = 0
        self.tuition_fee    = 400
        
        self.total_lv       = 0
        self.turn           = 1
        self.frame          = 0
        
        #ui
        self.topbar = Topbar()
        self.botcap = Bottomcap()
        self.next_button = Obj('next')
        self.next_button.set_texture('images/ui/next_turn.png')
        self.next_button.set_button([200,200])
        self.next_button.pos[0] = 1050
        self.next_button.pos[1] = 500
        
        #building registration
        self.buildings = []
        self.add_buildings(Camhub_Building())
        self.add_buildings(Techno_Building())
        self.add_buildings(Main_Building())
        self.add_buildings(Moon_Building())
        self.add_buildings(Design_Building())
        self.add_buildings(Phydeu_Building())
        self.add_buildings(Welfare_Building())
        self.add_buildings(Lib_Building())
        self.add_buildings(Science_Building())
        self.add_buildings(Engineer_Building())
        self.add_buildings(Sw_Building())
        self.add_buildings(Research_Building())
        self.add_buildings(Dormy_Building())
        self.add_buildings(Gate_Building())
        
        #info window
        self.opened_building = None
        
    def add_buildings(self, building):
        self.buildings.append(building)
        
    def next_turn(self):
        self.turn   += 1
        
        #calculate the univ values
        self.sum_values()

        #calculate the student
        self.student += self.get_student()
        
        #calculate tuition_fee and the budget
        Game.income_prv = self.get_budget(self.student)
        self.budget += self.get_budget(self.student)
        
        if self.turn%5 == 0 and self.turn <= 30:
            self.buildings[1].satisfaction += 1
            self.buildings[1].research += 1
            self.buildings[1].evaluation += 1
        
    
    #만족도, 연구기술력, 평판의 합을 구합니다.
    def sum_values(self):   
        self.satisfaction   = 0
        self.research       = 0
        self.evaluation     = 0
        self.cost           = 0
        self.total_lv       = 0
        for building in self.buildings:
            self.satisfaction   += building.get_satisfaction()
            self.research       += building.get_research()
            self.evaluation     += building.get_evaluation()
            self.cost           += building.get_cost()
            self.total_lv       += building.level
    
    #증가(혹은 감소)할 학생 숫자를 구합니다.
    def get_student(self):
        student = ((self.satisfaction + self.evaluation)/70)*200 - 150
        if self.student + student <= 0:
            Game.estimate_student = -self.student
        else :
            Game.estimate_student = student
        return Game.estimate_student
        
    #현재 상태라면 학기말에 들어올 예산을 구합니다.
    def get_budget(self, student):
        sum_univ_value = (self.satisfaction+self.research+self.evaluation)
        self.tuition_fee = (sum_univ_value/self.total_lv)
        Game.income_fee =       student * self.tuition_fee
        Game.income_res = self.research * self.evaluation * 20
        Game.estimate_income = Game.income_fee + Game.income_res - self.cost
        return Game.estimate_income

    def update(self):
        self.frame+=1
        
        #상태 갱신
        self.sum_values()
        self.get_budget(self.get_student() + self.student)
        
        #다른 창이 안 켜져있을 때만 체크
        if self.opened_building == None :
            #건물 클릭 확인
            for building in self.buildings:
                # building.update()
                if building.isClicked():
                    building.texture.scale([1, 1])
                    self.opened_building = building
                    self.opened_building.show_info()
                elif building.overroll():
                    building.texture.scale([1.05, 1.05])
                    self.botcap.update(building.name, True)
                else :
                    building.texture.scale([1, 1])
                    
            if self.next_button.overroll():
                self.next_button.texture.scale([1.05, 1.05])
            else :
                self.next_button.texture.scale([1, 1]) 
                
            if self.next_button.isClicked():
                self.next_turn()
        
        #info창 열린 건물있으면 내부 실행
        if self.opened_building != None:
            self.opened_building.update()
            if self.opened_building.info.isClosed():
                self.opened_building = None
    
        #상단바 UI 정보갱신
        self.topbar.update(self.satisfaction, 
                        self.research, 
                        self.evaluation, 
                        self.student, 
                        self.budget, 
                        self.turn)
        
        if self.student == 0 or self.budget < 0 :
            print('Fail')
        
        
    def render(self):
        super().render()
        #건물 출력
        for building in self.buildings:
            building.render()  
        
        #중간 UI출력
        self.next_button.render()
            
        #팝업 윈도우 출력
        if self.opened_building != None:
            self.opened_building.info_render()
        
        #상위 UI 출력
        self.botcap.render()
        self.topbar.render()