from  game_scene import *

if __name__ == "__main__":
    Game.init("하냥아 학교가자")
    scene = Game_Scene()
    while Game.run:
            
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                Game.run = False
                
        Game.screen.fill(Game.WHITE)
        
        scene.update()
        scene.render()
                
        for texture in Game.images:
            Game.screen.blit(texture.image, (0, 0))
        
        pygame.display.update()
        Game.clock.tick(1000/Game.FPS)
        
        Game.images.clear()

    Game.close()

   