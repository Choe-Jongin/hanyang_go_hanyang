from texture import *

class Game :
    name = "하냥아 학교가자"
    WHITE = (255,255,255)
    size = (1280,720)
    run = True
    FPS = 40
    images = []
    ending_value = []
    
    @staticmethod
    def init(game_name):
        Game.name = game_name;
        Game.m = (0, 0)
        Game.mouse = 'none'
        
        #for in game
        Game.income_prv = 0
        Game.budget = 10000
        Game.dormy_bonus = 1
        
        #pygame settings
        pygame.init()
        pygame.display.set_caption(Game.name)
        Game.screen = pygame.display.set_mode(Game.size)
        Game.clock = pygame.time.Clock()
        Game.bgm = pygame.mixer.Sound('sound/bgm.mp3')
        Game.error = pygame.mixer.Sound('sound/error.mp3')
    
    @staticmethod
    def render(texture):
        Game.images.append(texture)
        
    @staticmethod
    def end(state, satisfaction = 0, research = 0, evaluation = 0, student = 0):
        Game.ending_value = [state, satisfaction, research, evaluation, student] 
        
    @staticmethod
    def mouse_motion(m):
        Game.m = m
        
    @staticmethod
    def mouse_clear():
        if Game.mouse == 'down' :
            Game.mouse = 'click'
        else :
            Game.mouse = 'none'
    def mouse_down():
        Game.mouse = 'down'
        
    @staticmethod
    def mouse_up():
        Game.mouse = 'click'
        
    @staticmethod
    def close():
        pygame.quit()
        
    @staticmethod
    def pos_add(pos1, pos2):
        return (pos1[0]+pos2[0], pos1[1]+pos2[1])
    
    @staticmethod
    def pos_sub(pos1, pos2):
        return (pos1[0]-pos2[0], pos1[1]-pos2[1])
    
    @staticmethod
    def pos_sum(positions):
        re = (0,0)
        for pos in positions :
            pos_add(re, pos)
        return re
            