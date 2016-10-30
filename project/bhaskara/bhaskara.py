
class Bhaskara():
    __slots__ = ("a", "b", "c",
        "out", "delta", "sqrt_delta", "r1", "r2")
    def __init__(self, a, b, c):        
        self.a=a
        self.b=b
        self.c=c

        self.delta=None
        self.sqrt_delta=None
        self.r1=None
        self.r2=None
        self.out=None

    @classmethod
    def fsqrt_delta(self, delta):
        return delta**(1/2)

    @classmethod
    def fdelta(self, a, b, c):
        return (b**2 - 4*a*c)
    
    @classmethod
    def fr1(self, a, b, delta):
        return (-b + delta)/(2*a)

    @classmethod
    def fr2(self, a, b, delta):
        return (-b - delta)/(2*a)

    def make_out(self):
        d=dict((name, getattr(self, name)) for name in dir(self) 
        if not name.startswith('__') and 
        not callable(getattr(self,name))) 
        self.out=d

    def formatar(self):
        if type(self.out["r1"]) == complex:
            r1=self.out["r1"]
            r1_real=round(r1.real,3)
            r1_imag=round(r1.imag,3)
    
            if r1_imag<0:
                self.out["r1"]= str(r1_real) + " " + str(r1_imag) + "i"
            else:
                self.out["r1"]= str(r1_real) + " + " + str(r1_imag) +"i"

        if type(self.out["r2"]) == complex:
            r2=self.out["r2"]
            r2_real=round(r2.real,3)
            r2_imag=round(r2.imag,3)
    
            if r2_imag<0:
                self.out["r2"]= str(r2_real) + " " + str(r2_imag) + "i"
            else:
                self.out["r2"]= str(r2_real) + " + " + str(r2_imag) +"i"

    def roots(self):
        self.delta=self.fdelta(self.a, self.b, self.c)
        self.sqrt_delta=self.fsqrt_delta(self.delta)

        self.r1=self.fr1(self.a, self.b, self.sqrt_delta)
        self.r2=self.fr2(self.a, self.b, self.sqrt_delta)

    def calculate_roots(self):
        self.roots()
        self.make_out()
        self.formatar()