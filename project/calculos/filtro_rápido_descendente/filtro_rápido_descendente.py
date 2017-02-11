from math import log10

class FRD_Methods():
    __slots__=()

    def fATF(self, Q, q):
        return Q/q

    def fAF(self, ATF, N):
        return  ATF/N       
    
    def f(self, Q):
        return 1.2*Q**(1/2)

    def fd90(self, CU, d10):
        return d10*10**(1.67*log10(CU))

    def fGa(self, d90, rho, rhop, g, mu):
        num=(d90**3)*rho*(rhop - rho)*g
        den=mu**2
        return num/den

    def fRemf(self, Ga):
        a=33.7
        b=0.0408
        return (a**2 + b*Ga)**(1/2) - a

    def fVmf(self, Remf, nu, d90):
        return (Remf*nu)/d90

    def fSv(self, Psi, deq):
        return 6/(Psi*deq)

    def fDeltaHL(self, mu, rho, epsilon0, epsilon, Sv, V):
        num1 = 4.17*mu*((1 - epsilon0)**(2))*(Sv**2)*V
        den1 = rho*g*epsilon0**3
        a = num1/den1

        num2 = 0.48*mu*(1 - epsilon0)*Sv*V**2
        den2 = g*epsilon0**3
        b = num2/den2

        return a + b

    def fQF(self, Q, NF):
        return Q/Nf

    def fh0(self, QF, B):
        return (QF/(1.84*B))**(2/3)

    # Esse função poderia ser genaralizada para diversas 
    # massas.
    def fMTotal(self, M1, M2):
        return M1 + M2

    def fX2(self, MAreia, MTotal):
        return MAreia/MTotal

    


class FRD_Part1():
    __slots__=()

    def parte1(self):
        pass

class FRD_Part2():
    __slots__=()

    def parte2(self):
        pass


class FRD_Part3():
    __slots__=()

    def parte3(self):
        pass


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

class FRD_Main():
    __slots__=()

    def dimensionar(self):    
        self.parte1()
        self.parte2()
        self.parte3()
        
        self.make_out()
        self.arredondamento()


FRD_dict_inputs={
    "B":None,
} 

def factory_FRD(inp):  
    r={
        "L0":None,
        
        "out":None
    }

    d=dict(inp, **r)

    class FRD(FRD_Methods, FRD_Part1, FRD_Part2, FRD_Part3,
                Extras, FRD_Main):
        __slots__ = [key for key in d]
        def __init__(self):
            for key in d:
                setattr(self, key, d[key])

    return FRD