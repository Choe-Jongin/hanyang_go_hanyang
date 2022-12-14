from intro_scene import *
from title_scene import *
from game_scene import *
from ending_scene import *

if __name__ == "__main__":
    Game.init("하냥아 학교가자")
    
    scene_index = 0
    next_scene = 1
    scene_list = [Intro_Scene(), Title_Scene(), Game_Scene(), Ending_Scene()]
    
    while Game.run:
        
        # Game.mouse_clear()
        Game.mouse = 'none'
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                Game.run = False
                
            if event.type == pygame.MOUSEMOTION :
                Game.mouse_motion(pygame.mouse.get_pos())
                # print(Game.m)
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # print('down', end=' ')
                Game.mouse_down()
            
            if event.type == pygame.MOUSEBUTTONUP :
                # print('up')
                Game.mouse_up()
        
        # Game.screen.fill(Game.WHITE)
        next_scene = scene_list[scene_index].update()
        scene_list[scene_index].render()
        
        #scene 교체
        if next_scene != scene_index:
            #TODO : Loading progress 
            if next_scene == 1 :
                Game.bgm.play(-1)
            scene_index = next_scene
                
        for texture in Game.images:
            Game.screen.blit(texture.image, (texture.x, texture.y))
        
        pygame.display.update()
        Game.clock.tick(Game.FPS)
        
        Game.images.clear()

    Game.close()
