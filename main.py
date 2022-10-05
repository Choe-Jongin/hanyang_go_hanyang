from  game_scene import *

if __name__ == "__main__":
    Game.init("하냥아 학교가자")
    scene = Game_Scene()
    while Game.run:
        
        Game.mouse_clear()
        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                Game.run = False
                
            if event.type == pygame.MOUSEMOTION :
                Game.mouse_motion(pygame.mouse.get_pos())
                # print(Game.m)
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('down', end=' ')
                Game.mouse_down()
            
            if event.type == pygame.MOUSEBUTTONUP :
                print('up')
                Game.mouse_up()
        
        # Game.screen.fill(Game.WHITE)
        
        scene.update()
        scene.render()
                
        for texture in Game.images:
            Game.screen.blit(texture.image, (texture.x, texture.y))
        
        pygame.display.update()
        Game.clock.tick(Game.FPS)
        
        Game.images.clear()

    Game.close()
