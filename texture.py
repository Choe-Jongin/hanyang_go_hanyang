import pygame

class Texture():
    noimage = pygame.image.load('images/noimage.jpeg')
    
    def __init__(self, filename='images/noimage.jpeg'):
        self.filename = filename
        self.image = Texture.noimage
        try :
            self.original_image = pygame.image.load(filename)
        except :
            self.original_image = Texture.noimage
            print("no image :,",filename)
        
        self.original_size = self.original_image.get_size()
        self.image = self.original_image
        self.x, self.y = 0, 0
            
    def set_scale(self, scale):  
        self.image = pygame.transform.scale(self.image, scale)
        
    def scale(self, s): 
        self.image = pygame.transform.scale(self.original_image,
                                            (self.original_size[0]*s[0], self.original_size[1]*s[1]))
        
class Texture_font(Texture):
    def __init__(self, font, size, color, bold = False):
        self.font = pygame.font.SysFont(font, size, bold)
        self.color = color
        self.set_image('')
        self.x, self.y = 0, 0

    def set_image(self, text, pos = (0,0), center = (0,0), margin= (0,0)):
        self.x = pos[0] - center[0] + margin[0]
        self.y = pos[1] - center[1] + margin[1]
        self.image = self.font.render(text,True, self.color)
        