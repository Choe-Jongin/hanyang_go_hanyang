class Button:
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def isClick(self, m) :
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


    def vector(self,p1, p2):
       return [(p2[0] - p1[0]), (p2[1] - p1[1])]

    def dot(self, u, v):
        return u[0]* v[0] + u[1] * v[1]; 
    