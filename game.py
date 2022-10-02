from texture import *

class Game :
    name = "하냥아 학교가자"
    WHITE = (255,255,255)
    size = (1280,720)
    run = True
    FPS = 20
    images = []
    
    @staticmethod
    def init(game_name):
        Game.name = game_name;
        
        pygame.init()
        pygame.display.set_caption(Game.name)
        Game.screen = pygame.display.set_mode(Game.size)
        Game.clock = pygame.time.Clock()
        pygame.mixer.music.load('sound/bgm.mp3')
        # pygame.mixer.music.play(-1)
    
    @staticmethod
    def close():
        pygame.quit()
        
    @staticmethod
    def render(texture):
        Game.images.append(texture)