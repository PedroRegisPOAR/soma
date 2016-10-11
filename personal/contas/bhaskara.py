class ResultadosBhaskara():
    def __init__(self):
        self.r1=None
        self.r2=None
        
class Bhaskara():
    def __init__(self, a, b, c):

        self.r=ResultadosBhaskara()
        
        self.a=a
        self.b=b
        self.c=c

        self.d=self.delta()

    def delta(self):
        return (self.b**2 - 4*self.a*self.c)**(1/2)
    
    def r1(self):
        return (-self.b + self.d)/(2*self.a)

    def r2(self):
        return (-self.b - self.d)/(2*self.a)

    def roots(self):
        self.r.r1=self.r1()
        self.r.r2=self.r2()
