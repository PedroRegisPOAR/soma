class FloculadorChicaneado_Methods():
    __slots__=()

    def fm(self, rho, mu, T, f, A, G, Q):
        a = 18*mu*T
        b = rho*(13 + 9*f)
        c = (A*G/Q)**2
        return ((a*c)/b)**(1/3)

    def fma(self, m):
        return int(m) + 1

    def frho(self, T):
        t0=3.9818
        A=7.0134*10**(-8)
        B=7.926504*10**(-6)
        C=-7.575677*10**(-8)
        D=7.314894*10**(-10)
        E=-3.596458*10**(-12)
        rho=999.97358
        L=[A, B, C, D, E]
        soma=0
        for i in range(len(L)):
            soma+=L[i]*(T-t0)**(i+1)

        return rho*(1-soma)

    def fmu(self, T):
        a=2.414*10**(-5)
        b=247.8
        c=140 - 273.15 # Conversão para graus Celsius
        return a*10**(b/(T - c))     

    def fV(self, Q, Tf):
        return Q*(60*Tf)   

    def fA(self, H, L):
        return H*L   

    def fa(self, V, N, A):
        return V/(N*A)

    def fe(self, L, m):
        return L/m

    def fE(self, c, e):
        return c*e

class FloculadorChicaneado_Parte1():
    __slots__=()

    def parte1(self):
        self.mu = self.fmu(self.T)
        self.rho = self.frho(self.T)
        self.V = self.fV(self.Q, self.Tf)
        self.A = self.fA(self.H, self.L)
        self.a = self.fa(self.V, self.N, self.A)

        self.m1 = self.fm(self.rho, self.mu, self.T, self.f, self.A, self.G1, self.Q)
        self.m2 = self.fm(self.rho, self.mu, self.T, self.f, self.A, self.G2, self.Q)
        self.m3 = self.fm(self.rho, self.mu, self.T, self.f, self.A, self.G3, self.Q)

        self.m1a = self.fma(self.m1)
        self.m2a = self.fma(self.m2)
        self.m3a = self.fma(self.m3)

        self.e1 = self.fe(self.L, self.m1a)
        self.e2 = self.fe(self.L, self.m2a)
        self.e3 = self.fe(self.L, self.m3a)

        self.E1 = self.fE(self.c, self.e1)
        self.E2 = self.fE(self.c, self.e2)
        self.E3 = self.fE(self.c, self.e3)


class Extras():
    __slots__=()

    def make_out(self):
        d=dict((name, getattr(self, name)) for name in dir(self) 
        if not name.startswith('__') and 
        not callable(getattr(self,name))) 
        self.out=d

    def arredondamento(self):
        for key in self.out:
            if type(self.out[key]) == float:
                self.out[key]=round(self.out[key],4)


class FloculadorChicaneado_Main():
    __slots__=()

    def dimensionar(self):    
        self.parte1()
        
        self.make_out()
        self.arredondamento()



dict_inputs_FloculadorChicaneado={
    "T":None,
    "Q":None,
    "G1":None,
    "G2":None,
    "G3":None,
    "f":None,
    "Tf":None,
    "N":None,
    "L":None,
    "H":None,
    "c":None
} 



def factory_FloculadorChicaneado(inp):  


    r={
        "mu":None,
        "rho":None,
        "m1":None,
        "m2":None,
        "m3":None, 
        "m1a":None,
        "m2a":None,
        "m3a":None,        
        "a":None,
        "V":None, 
        "A":None, 
        "e1":None,    
        "e2":None,
        "e3":None,
        "E1":None,
        "E2":None,
        "E3":None,
        "out":None
    }

    
    d=dict(inp, **r)

    class FloculadorChicaneado(FloculadorChicaneado_Methods, FloculadorChicaneado_Parte1,
                Extras, FloculadorChicaneado_Main):
        __slots__ = [key for key in d]
        def __init__(self):
            for key in d:
                setattr(self, key, d[key])

    return FloculadorChicaneado





