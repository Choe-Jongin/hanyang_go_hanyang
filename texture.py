import pygame

class Texture():
    noimage = pygame.image.load('images/noimage.jpeg')
    
    def __init__(self, filename='images/noimage.jpeg'):
        self.filename = filename
        self.image = Texture.noimage
        try :
            self.image = pygame.image.load(filename)
        except :
            self.image = Texture.noimage
            print("no image :,",filename)
            
    def set_scale(self, scale):  
        self.image = pygame.transform.scale(self.image, scale)