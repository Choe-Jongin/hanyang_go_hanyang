
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
from sw_building import Sw_Building
from science_building import Science_Building
from welfare_building import Welfare_Building

from scene import *
from topbar import *

class Game_Scene(Scene):
    
    def __init__(self):
        super().__init__("Game Scene", 'images/background.png')
        
        #in game values
        self.satisfaction   = 50
        self.research       = 100
        self.evaluation     = 50
        self.student        = 1000
        self.budget         = 1000
        self.turn           = 10
        
        #ui
        self.topbar = Topbar()
        self.botcap = Bottomcap()
        
        #building registration
        self.buildings = []
        self.add_buildings(Camhub_Building())
        self.add_buildings(Main_Building())
        self.add_buildings(Moon_Building())
        self.add_buildings(Phydeu_Building())
        self.add_buildings(Design_Building())
        self.add_buildings(Welfare_Building())
        self.add_buildings(Lib_Building())
        self.add_buildings(Science_Building())
        self.add_buildings(Engineer_Building())
        self.add_buildings(Sw_Building())
        self.add_buildings(Dormy_Building())
        self.add_buildings(Gate_Building())
        
        self.bi = Building_info()
        
        self.frame  = 0
    
    def add_buildings(self, building):
        self.buildings.append(building)
        
    def next_turn(self):
        self.turn += 1
        self.budget += 1000
        
    def show_building_info(self, building) :
        self.bi.set_building(building)
        self.visible_bi = True

    def update(self):
        for building in self.buildings:
            
            building.update()
            if building.isClicked():
                building.texture.scale([1, 1])
                self.bi.set_building(building)
            elif building.overroll():
                building.texture.scale([1.05, 1.05])
                self.botcap.update(building.name, True)
            else :
                building.texture.scale([1, 1])
    
        self.topbar.update(self.satisfaction, 
                           self.research, 
                           self.evaluation, 
                           self.student, 
                           self.budget, 
                           self.turn)
    
        self.next_turn()
        self.bi.update()
         
    def render(self):
        super().render()
        for building in self.buildings:
            building.render()
        
        self.botcap.render()
        self.topbar.render()
        self.bi.render()