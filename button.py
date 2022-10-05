from game import *

class Button:
    
    def __init__(self, pos):
        self.pos = pos
        Button.sound = pygame.mixer.Sound('sound/click.mp3')
    
    def vector(self,p1, p2):
       return [(p2[0] - p1[0]), (p2[1] - p1[1])]

    def dot(self, u, v):
        return u[0]* v[0] + u[1] * v[1]; 
    
    def mouse_in(self, m) :
        pass
    
    def isClicked(self):
        if Game.mouse == 'click' and self.mouse_in(Game.m) :
            Button.sound.play(0)
            return True
        return False
    
class Rect_Button(Button):
    def __init__(self, pos, size):
        super().__init__(pos)
        self.size = size
        self.A = [0, 0]
        self.B = size
        
    def mouse_in(self, m) :
        return (self.pos[0] + self.A[0] <= m[0] and
                self.pos[1] + self.A[1] <= m[1] and 
                self.pos[0] + self.B[0] >= m[0] and
                self.pos[1] + self.B[1] >= m[1])
       
class Rhombus_Button(Button):
         
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def mouse_in(self, m) :
        if(self.A == self.B == self.C == self.D):
            return False
        
        AB = self.vector(self.A, self.B);
        AM = self.vector(self.A, m);
        BC = self.vector(self.B, self.C);
        BM = self.vector(self.B, m);
        dotABAM = self.dot(AB, AM);
        dotABAB = self.dot(AB, AB);
        dotBCBM = self.dot(BC, BM);
        dotBCBC = self.dot(BC, BC);
        return (0 <= dotABAM and dotABAM <= dotABAB and 0 <= dotBCBM and dotBCBM <= dotBCBC)
