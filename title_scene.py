from scene import *

class Title_Scene(Scene):
    
    def __init__(self):
        super().__init__("title Scene", 'images/title/bg.png')
        
        #메인 배너
        self.title = Obj('title')
        self.title.set_texture('images/title/title.png')
        self.title.pos = [Game.size[0]/2, -310]
        self.title.center = [839/2, 0]
        self.title_dest = [Game.size[0]/2, 15]
        self.title.texture.set_alpha(100)
        self.title_state = 0
        
        #메뉴
        self.menus = [Obj('menu1'), Obj('menu2'), Obj('menu3'), Obj('menu4') ]
        for i in range(len(self.menus)):
            self.menus[i].set_texture('images/title/menu'+str(i+1)+'.png')
            self.menus[i].pos = [1280 + 225 + 200*i, 400 + 80*i] 
            self.menus[i].center = [225,0] 
            self.menus[i].set_button([450, 64])
            self.menus[i].button.set_rect([-220,0], [220,60])
            
        #팝업 이미지
        self.help = Obj('help')
        self.cast = Obj('cast')
        self.help.set_texture('images/title/help.png')
        self.cast.set_texture('images/title/cast.png')
        self.help.set_button(Game.size)
        self.cast.set_button(Game.size)
        self.show_help = False
        self.show_cast = False
        
    def update(self):
        if self.title_state == 0 :
            self.title.pos[1] += (self.title_dest[1] - self.title.pos[1])/7
            if self.title.pos[1] >= self.title_dest[1]-3 :
                self.title.pos[1] = self.title_dest[1]
                self.title_state = 2
        
        else :
            
            if self.title_state == 1 :
                self.title.pos[1] += 0.5
                if self.title.pos[1] > self.title_dest[1] + 10 :
                    self.title_state = 2
            elif self.title_state == 2:
                self.title.pos[1] -= 0.5
                if self.title.pos[1] < self.title_dest[1] - 10 :
                    self.title_state = 1
                    
            #popup close
            if self.show_help and self.help.isClicked():
                self.show_help = False
            if self.show_cast and self.cast.isClicked():
                self.show_cast = False
            
            #menu 이동 및 클릭 대기
            for menu in self.menus :
                menu.pos[0] += (Game.size[0]/2 - menu.pos[0])/4
                if menu.pos[0] < Game.size[0]/2 :
                    menu.pos[0] = Game.size[0]/2
                
                #오버롤 효과
                if menu.overroll() :
                    menu.texture.set_alpha(100)
                else :
                    menu.texture.set_alpha(80)
                
                #열린 팝업이 없으면 메뉴 클릭 대기
                if not self.show_help and not self.show_help and menu.isClicked():
                    if menu.name == 'menu1':
                        return 2
                    
                    elif menu.name == 'menu2':
                        self.show_help = True
                        
                    elif menu.name == 'menu3':
                        self.show_cast = True
                        
                    elif menu.name == 'menu4':
                        Game.run = False
                
        return 1
        
    def render(self):
        super().render()
        self.title.render()
        for menu in self.menus :
            menu.render()
            
        if self.show_help :
            self.help.render()
        if self.show_cast :
            self.cast.render()