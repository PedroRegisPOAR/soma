import math

class CalhaParshall():
    __slots__ = ("DimencoesPadronizadas", "Valoreskn", "W", "mu", "rho", 
        "C", "D", "K", "N", "k", "n", "H0", "D0", "U0", "q", "E0", "U1",
        "h1", "F1", "h2","h3", "U3", "L", "h", "Tm", "Gm", 
        "d", "Q", "g", "T", "GmMin", "GmMax", "FMin", "dimensionado_ok")


    def __init__(self, Q, g, T, GmMin, GmMax, FMin):
           
        self.Q=Q
        self.g=g
        self.T=T
        
        self.GmMax=GmMax
        self.GmMin=GmMin
        self.FMin=FMin 


        self.DimencoesPadronizadas=[
            [ 229, 880, 864, 380, 575, 763, 305, 457, 76, 114],
            [ 305, 1372, 1344, 610, 845, 915, 610, 915, 76, 229],
            [ 457, 1449, 1420, 762, 1026, 915, 610, 915, 76, 229],
            [ 610, 1525, 1496, 915, 1207, 915, 610, 915, 76, 229],
            [ 915, 1677, 1645, 1220, 1572, 915, 610, 915, 76, 229],
            [ 1220, 1830, 1795, 1525, 1938, 915, 610, 915, 76, 229],
            [ 1525, 1983, 1941, 1830, 2303, 915, 610, 915, 76, 229],
            [ 1830, 2135, 2090, 2135, 2667, 915, 610, 915, 76, 229],
            [ 2135, 2288, 2240, 2440, 3030, 915, 610, 915, 76, 229],
            [ 2440, 2440, 2392, 2745, 3400, 915, 610, 915, 76, 229]]
 
        # Valores modificados.
        self.Valoreskn=[[229, 1486, 0.633],
                        [305, 1276, 0.657],
                        [457, 0.966, 0.65],
                        [610, 0.795, 0.64],
                        [915, 0.608, 0.639],
                        [1220, 0.505, 0.634],
                        [1525, 0.436, 0.63],
                        [1830, 0.389, 0.627],
                        [2135, 0.355, 0.625],
                        [2440, 0.324, 0.623]]    

        self.W=None
        self.mu=None
        self.rho=None
        self.C=None
        self.D=None
        self.K=None
        self.N=None
        self.k=None
        self.n=None
        self.H0=None
        self.D0=None
        self.U0=None
        self.q=None
        self.E0=None
        self.U1=None
        self.h1=None
        self.F1=None
        self.h2=None
        self.h3=None
        self.U3=None
        self.L=None
        self.h=None
        self.Tm=None
        self.Gm=None
        self.d=None

        self.dimensionado_ok=False

    def setCDKN(self, W):
        indice=-1
        for i in range(len(self.DimencoesPadronizadas)):
            if self.DimencoesPadronizadas[i][0]==W:
                indice=i
        if indice==-1:
            print("Erro no método setCDKN. Provavelmente o W={} da calha parshall não existe na tabela.".format(W))
        else:
            self.C=self.DimencoesPadronizadas[indice][3]/1000
            self.D=self.DimencoesPadronizadas[indice][4]/1000
            self.K=self.DimencoesPadronizadas[indice][8]/1000
            self.N=self.DimencoesPadronizadas[indice][9]/1000

    def setkn(self, W):
        indice=-1
        for i in range(len(self.Valoreskn)):
            if self.Valoreskn[i][0]==W:
                indice=i
        if indice==-1:
            print("Erro no método setnk. Provavelmente o W ={} da calha parshall não existe na tabela.".format(W))
        else:
            self.k=self.Valoreskn[indice][1]
            self.n=self.Valoreskn[indice][2]
    
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

    def fH0(self, k, Q, n):
        return k*Q**(n)
        
    def fD0(self, D, W):
        return (2/3)*(D - W) + W
    
    def fU0(self, Q, D0, H0):
        return Q/(D0*H0)

    def fq(self, Q, W):
        return Q/(W)

    def fE0(self, U0, g, H0, N):
        return (U0**2)/(2*g) + H0 + N

    def fU1(self, g, q, E0):
        x=-g*q/(((2/3)*g*E0)**(1.5))
        a=((2*g*E0)/3)**(1/2)
        return 2*a*math.cos(math.acos(x)/3)

    def fh1(self, q, U1):
        return q/U1

    def froud(self, g, h, U):
        return U/(g*h)**(1/2)
    
    def fh2(self, h1, F1):
        return (h1/2)*((1 + 8*F1**2)**(1/2) - 1)

    def fh3(self, h2, N, K):
        return h2 - (N - K)

    def fU3(self, Q, C, h3):
        return Q/(C*h3)
        
    def fL(self, h1, h2):
        return 6*(h2 - h1)

    def fh(self, h1, h2):
        return ((h2 - h1)**3)/(4*h1*h2)

    def fTm(self, L, U1, U3):
        return (2*L)/(U1 + U3)

    def fGm(self, h, g, rho, mu, Tm):
        return ((g*rho*h)/(mu*Tm))**(1/2)

    def make_dict(self):
        d=dict((name, getattr(self, name)) for name in dir(self) 
            if not name.startswith('__') and 
            not callable(getattr(self,name)) and 
            type(getattr(self,name))==float or
            type(getattr(self,name))==bool) 
        self.d=d

    def arredondamento(self):
        for key in self.d:
            if type(self.d[key]) == float:
                self.d[key]=round(self.d[key],4)

    def dimensiona(self):
#        self.setCDKN(self.W)
#        self.setkn(self.W)
        
        self.rho=self.frho(self.T)
        self.mu=self.fmu(self.T)
        self.H0=self.fH0(self.k, self.Q, self.n)
        self.D0=self.fD0(self.D, self.W)
        self.U0=self.fU0(self.Q, self.D0, self.H0)
        self.q =self.fq(self.Q, self.W)
        self.E0=self.fE0(self.U0, self.g, self.H0, self.N)
        self.U1=self.fU1(self.g, self.q, self.E0)
        self.h1=self.fh1(self.q, self.U1)
        self.F1=self.froud(self.g, self.h1, self.U1)
        self.h2=self.fh2(self.h1, self.F1)
        self.h3=self.fh3(self.h2, self.N, self.K)
        self.U3=self.fU3(self.Q, self.C, self.h3)
        self.L =self.fL(self.h1, self.h2)
        self.h =self.fh(self.h1, self.h2)
        self.Tm=self.fTm(self.L, self.U1, self.U3)
        self.Gm=self.fGm(self.h, self.g, self.rho, self.mu, self.Tm)

#        self.H0=round(self.H0,3)
#        self.D0=round(self.D0,3)
#        self.U0=round(self.U0,3)
#        self.q =round(self.q ,3)
#        self.E0=round(self.E0,3)
#        self.U1=round(self.U1,3)
#        self.h1=round(self.h1,3)
#        self.F1=round(self.F1,3)
#        self.h2=round(self.h2,3)
#        self.h3=round(self.h3,3)
#        self.U3=round(self.U3,3)
#        self.L =round(self.L ,3)
#        self.h =round(self.h ,3)
#        self.Tm=round(self.Tm,3)
#        self.Gm=round(self.Gm,3)

        
    def dimensiona_inteligente(self):
        for i in range(len(self.DimencoesPadronizadas)):
#            print(self.DimençõesPadronizadas[i][0])
            
            self.W=self.DimencoesPadronizadas[i][0]
            
            self.setCDKN(self.W)
            self.setkn(self.W)
            
            self.W=self.DimencoesPadronizadas[i][0]/1000

            self.dimensiona()

#            if self.Gm>1000:
#                print("i= ",i ,"self.Gm = ", self.Gm)

#            if self.F1>2:
#                print("i= ",i ,"self.F1 = ", self.F1)

#            if self.Tm*self.Gm>300 and self.Tm*self.Gm<1600:
#                print("i= ",i ,"self.F1 = ", self.F1)
#                print("i= ",i ,"self.Gm = ", self.Gm)
            
#            if type(self.Gm) != complex:
#                print("i = ", i, "Tm= ", self.Gm)

#            if self.F1 > 5:
#                print(i, " ok")        
            if (type(self.Gm) != complex and
             self.Gm>=self.GmMin and 
             self.Gm<=self.GmMax and 
             self.F1>self.FMin and 
             self.h3>0):
                self.make_dict()
                self.arredondamento()
                self.dimensionado_ok=True
#                print("passou no if")
#                print("i= ",i)
#                print(self.Gm)
                
#                print(self.d)
                break





            
Q = 0.12
g = 9.81
T = 17.5
GmMin = 1050
GmMax = 2000
FMin = 4.5               
#######

                  
cp=CalhaParshall(Q, g, T, GmMin, GmMax, FMin)
#cp.dimensiona()
cp.dimensiona_inteligente()

print("dimensionado_ok = ", cp.dimensionado_ok)

'''
print("W = ", cp.d['W'])
print("C = ", cp.d['C'])
print("D = ", cp.d['D'])
print("K = ", cp.d['K'])
print("N = ", cp.d['N'])

print("k = ", cp.d['k'])
print("n = ", cp.d['n'])

print("H0= ", cp.d['H0'])
print("D0= ", cp.d['D0'])
print("U0= ", cp.d['U0'])

print("q= ", cp.d['q'])
print("E0= ", cp.d['E0'])
print("U1= ", cp.d['U1'])
print("h1= ", cp.d['h1'])

print("F1= ", cp.d['F1'])

print("h2= ", cp.d['h2'])
print("h3= ", cp.d['h3'])
print("U3= ", cp.d['U3'])

print("L= ", cp.d['L'])
print("h= ", cp.d['h'])

print("T= ", cp.d['Tm'])
print("G= ", cp.d['Gm'])
'''


'''
print("W = ", cp.W)
print("C = ", cp.C)
print("D = ", cp.D)
print("K = ", cp.K)
print("N = ", cp.N)

print("k = ", cp.k)
print("n = ", cp.n)

print("H0= ", cp.H0)
print("D0= ", cp.D0)
print("U0= ", cp.U0)

print("q= ", cp.q)
print("E0= ", cp.E0)
print("U1= ", cp.U1)
print("h1= ", cp.h1)

print("F1= ", cp.F1)

print("h2= ", cp.h2)
print("h3= ", cp.h3)
print("U3= ", cp.U3)

print("L= ", cp.L)
print("h= ", cp.h)

print("T= ", cp.Tm)
print("G= ", cp.Gm)
'''

