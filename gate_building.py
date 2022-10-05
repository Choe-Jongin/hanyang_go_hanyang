from building import *

class Gate_Building(Building):
    def __init__(self):
        super().__init__("아고라(정문)")
        self.set_texture('images/buildings/gate.png')
        self.pos = (855, 520)
        self.center = (30, 178)
        self.set_effect(2,0,2)
    
        #info window
        self.info.set_building(self)       
        
        #특수 충돌 범위
        self.rect_pos = (966, 440)
        self.button = Rect_Button( self.rect_pos, [100,100] )
        
        self.dest = '한양대학교 에리카의 상징과도 같은 아고라다냥. 내부에는 홍보관과 역사관이 있다냥'