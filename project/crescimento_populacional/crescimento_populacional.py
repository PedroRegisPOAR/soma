import os
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot as plt

#import numpy as np



def fexemplo(x, y):	
	
	l = list(np.arange(0, 10, 0.1))
	a = [y*t for t in l]

	plt.plot(l, a, 'o', color='r')
	plt.axis([0, 10, 0, 20])
	#return plt

	# Truque para mudar o lugar onde a figura será criada.
	initial_path = os.getcwd()
	path = 'project/static/crescimento_populacional/'
	os.chdir(path)

	plt.savefig('nome_figura.png')
	plt.close()
	#plt.show()

	# Não sei se isso é realmente necessario.
	os.chdir(initial_path)

'''
class CrescimentoPopulacional():
    def __init__(self, t0, t1, t2, t3, t4, t5, P0, P1, P2):
        self.t0 = t0
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5

        self.P0 = P0
        self.P1 = P1
        self.P2 = P2
    
        self.Ka = None
        self.Kg = None
        self.Ps = None
        self.Kd = None
        self.K1 = None
        self.c = None

        self.P3_PA = None
        self.P3_PG = None
        self.P3_TD = None
        self.P3_CL = None

        self.P4_PA = None
        self.P4_PG = None
        self.P4_TD = None
        self.P4_CL = None

        self.P5_PA = None
        self.P5_PG = None
        self.P5_TD = None
        self.P5_CL = None

        self.y_PA = None
        self.y_PG = None
        self.y_TD = None
        self.y_CL = None

		self.x_censo = None
        self.y_censo = None 
        
        self.y_PA_ajuste = None
        self.y_PG_ajuste = None
        self.y_TD_ajuste = None
        self.y_CL_ajuste = None

        self.x_ajuste = None


    def fKa(self, P1, P2, t1 ,t2):
        return (P2 - P1)/(t2 - t1)

    def projeçãoAritimética(self, t, P0, Ka, t0):
        return P0 + Ka*(t - t0)

    def fKg(self, P0, P2, t0, t2):
        return (math.log(P2) - math.log(P0))/(t2 - t0)

    def projeçãoGeométrica(self, t, P0, Kg, t0):
        return P0*math.e**(Kg*(t - t0))        
    
    def fPs(self, P0, P1, P2):
        num = 2*P0*P1*P2 - (P1**2)*(P0 + P2)
        den = (P0*P2 - P1**2)
        return num/den

    def fKd(self, Ps, P0, P2, t0, t2):
        num = - math.log((Ps - P2)/(Ps + P0))
        den = t2 - t0
        return num/den

    def taxaDecrescente(self, t, t0, Ps, P0, Kd):
        return P0 + (Ps - P0)*(1 - math.e**(-Kd*(t - t0)))    

    def fc(self, Ps, P0):
        return (Ps - P0)/P0

    def fK1(self, t1, t2, P0, P1, Ps):
        a= (1/(t2 - t1))
        num = P0*(Ps - P1)
        den = P1*(Ps - P0)
        b = math.log(num/den)
        return a*b

    def crescimentoLogístico(self, t, t0, Ps, c, K1):
        return Ps/(1 + c*math.e**(K1*(t - t0)))

    def preenche_y_ajuste(self):
        def f1(t):
            return self.projeçãoAritimética(t, self.P0, self.Ka, self.t0)
        def f2(t):
            return self.projeçãoGeométrica(t, self.P0, self.Kg, self.t0)
        def f3(t):
            return self.taxaDecrescente(t, self.t0, self.Ps, self.P0, self.Kd)
        def f4(t):
            return self.crescimentoLogístico(t, self.t0, self.Ps, self.c, self.K1)

        self.y_PA_ajuste = [f1(t) for t in self.x_ajuste]
        self.y_PG_ajuste = [f2(t) for t in self.x_ajuste]
        self.y_TD_ajuste = [f3(t) for t in self.x_ajuste]
        self.y_CL_ajuste = [f4(t) for t in self.x_ajuste]

    # ls abrevia linestyle
    def criaGráfico(self, x_projeção, y_projeção, ls_projeção, x_censo, y_censo, ls_censo):
        x = x_projeção + x_censo
        y = y_projeção + y_censo

        p = 0.005
        x_min = min(x) - p*( (max(x)**2 + min(x)**2)**(1/2) )
        y_min = min(y) - p*( (max(y)**2 + min(y)**2)**(1/2) )
        x_max = max(x) + p*( (max(x)**2 + min(x)**2)**(1/2) )
        y_max = max(y) + p*( (max(y)**2 + min(y)**2)**(1/2) )

        plt.axis([x_min, x_max, y_min, y_max])

        plt.plot(x_projeção, y_projeção, ls_projeção)
        plt.plot(x_censo, y_censo, ls_censo)

        plt.show()

    def inicializaConstantes(self):
        self.Ka = self.fKa(self.P1, self.P2, self.t1 ,self.t2)
        self.Kg = self.fKg(self.P0, self.P2, self.t0, self.t2)
        self.Ps = self.fPs(self.P0, self.P1, self.P2)
        self.Kd = self.fKd(self.Ps, self.P0, self.P2, self.t0, self.t2)
        self.c  = self.fc(self.Ps, self.P0)
        self.K1 = self.fK1(self.t1, self.t2, self.P0, self.P1, self.Ps)        

    def projeções(self, t):
        a = self.projeçãoAritimética(t, self.P0, self.Ka, self.t0)
        b = self.projeçãoGeométrica(t, self.P0, self.Kg, self.t0)
        c = self.taxaDecrescente(t, self.t0, self.Ps, self.P0, self.Kd)
        d = self.crescimentoLogístico(t, self.t0, self.Ps,
                                                self.c, self.K1)
        return a, b, c, d

    def projeta(self):

        self.x_ajuste = list(np.arange(- 0.005*self.t0 + self.t0, self.t5, 0.1))
		self.x_censo = [self.t0, self.t1, self.t2]
        self.y_censo = [self.P0, self.P1, self.P2]

        self.inicializaConstantes()

        self.P3_PA, self.P3_PG, self.P3_TD, self.P3_CL = self.projeções(self.t3)
        self.P4_PA, self.P4_PG, self.P4_TD, self.P4_CL = self.projeções(self.t4)
        self.P5_PA, self.P5_PG, self.P5_TD, self.P5_CL = self.projeções(self.t5)

        self.preenche_y_ajuste()
        
        self.criaGráfico(self.x_ajuste, self.y_PA_ajuste, '-', self.x_censo, self.y_censo, 'o')
        self.criaGráfico(self.x_ajuste, self.y_PG_ajuste, '-', self.x_censo, self.y_censo, 'o')
        self.criaGráfico(self.x_ajuste, self.y_TD_ajuste, '-', self.x_censo, self.y_censo, 'o')
        self.criaGráfico(self.x_ajuste, self.y_CL_ajuste, '-', self.x_censo, self.y_censo, 'o')                        
'''

'''
ppinit = {	
		't0':None,
		't1':None,
		't2':None,
		't3':None,
		't4':None,
		't5':None,
		'P0':None,
		'P1':None,
		'P2':None,
	}


global ppresults
ppresults = {
	    'Ka': None,		
	    'Kg': None,		
	    'Ps': None,		
	    'Kd': None,		
	    'K1': None,		
	    'c': None,				
	    'P3_PA': None,		
	    'P3_PG': None,		
	    'P3_TD': None,		
	    'P3_CL': None,				
	    'P4_PA': None,		
	    'P4_PG': None,		
	    'P4_TD': None,		
	    'P4_CL': None,				
	    'P5_PA': None,		
	    'P5_PG': None,		
	    'P5_TD': None,		
	    'P5_CL': None,				
	    'y_PA': None,		
	    'y_PG': None,		
	    'y_TD': None,		
	    'y_CL': None,				
		'x_censo': None,
	    'y_censo': None, 		        	
	    'y_PA_ajuste': None,		
	    'y_PG_ajuste': None,		
	    'y_TD_ajuste': None,		
	    'y_CL_ajuste': None,		
	}


class PP_Methods():
    __slots__=()

    def fKa(self, P1, P2, t1 ,t2):
        return (P2 - P1)/(t2 - t1)

    def projeçãoAritimética(self, t, P0, Ka, t0):
        return P0 + Ka*(t - t0)

    def fKg(self, P0, P2, t0, t2):
        return (math.log(P2) - math.log(P0))/(t2 - t0)

    def projeçãoGeométrica(self, t, P0, Kg, t0):
        return P0*math.e**(Kg*(t - t0))        
    
    def fPs(self, P0, P1, P2):
        num = 2*P0*P1*P2 - (P1**2)*(P0 + P2)
        den = (P0*P2 - P1**2)
        return num/den

    def fKd(self, Ps, P0, P2, t0, t2):
        num = - math.log((Ps - P2)/(Ps + P0))
        den = t2 - t0
        return num/den

    def taxaDecrescente(self, t, t0, Ps, P0, Kd):
        return P0 + (Ps - P0)*(1 - math.e**(-Kd*(t - t0)))    

    def fc(self, Ps, P0):
        return (Ps - P0)/P0

    def fK1(self, t1, t2, P0, P1, Ps):
        a= (1/(t2 - t1))
        num = P0*(Ps - P1)
        den = P1*(Ps - P0)
        b = math.log(num/den)
        return a*b

    def crescimentoLogístico(self, t, t0, Ps, c, K1):
        return Ps/(1 + c*math.e**(K1*(t - t0)))


class PP_Parte1():
	__slots__=()
	def inicializaConstantes(self):
		self.Ka = self.fKa(self.P1, self.P2, self.t1 ,self.t2)
		self.Kg = self.fKg(self.P0, self.P2, self.t0, self.t2)
		self.Ps = self.fPs(self.P0, self.P1, self.P2)
		self.Kd = self.fKd(self.Ps, self.P0, self.P2, self.t0, self.t2)
		self.c  = self.fc(self.Ps, self.P0)
		self.K1 = self.fK1(self.t1, self.t2, self.P0, self.P1, self.Ps)  


class PP_Parte2():
    __slots__=()

    def projeções(self, t):
        a = self.projeçãoAritimética(t, self.P0, self.Ka, self.t0)
        b = self.projeçãoGeométrica(t, self.P0, self.Kg, self.t0)
        c = self.taxaDecrescente(t, self.t0, self.Ps, self.P0, self.Kd)
        d = self.crescimentoLogístico(t, self.t0, self.Ps,
                                                self.c, self.K1)
        return a, b, c, d


class PP_Parte3():
    __slots__=()

    def preenche_y_ajuste(self):
        def f1(t):
            return self.projeçãoAritimética(t, self.P0, self.Ka, self.t0)
        def f2(t):
            return self.projeçãoGeométrica(t, self.P0, self.Kg, self.t0)
        def f3(t):
            return self.taxaDecrescente(t, self.t0, self.Ps, self.P0, self.Kd)
        def f4(t):
            return self.crescimentoLogístico(t, self.t0, self.Ps, self.c, self.K1)

        self.y_PA_ajuste = [f1(t) for t in self.x_ajuste]
        self.y_PG_ajuste = [f2(t) for t in self.x_ajuste]
        self.y_TD_ajuste = [f3(t) for t in self.x_ajuste]
        self.y_CL_ajuste = [f4(t) for t in self.x_ajuste]



class PP_Parte4():
    __slots__=()	

    def criaGráfico(self, x_projeção, y_projeção, ls_projeção, x_censo, y_censo, ls_censo):
        x = x_projeção + x_censo
        y = y_projeção + y_censo

        p = 0.005
        x_min = min(x) - p*( (max(x)**2 + min(x)**2)**(1/2) )
        y_min = min(y) - p*( (max(y)**2 + min(y)**2)**(1/2) )
        x_max = max(x) + p*( (max(x)**2 + min(x)**2)**(1/2) )
        y_max = max(y) + p*( (max(y)**2 + min(y)**2)**(1/2) )

        plt.axis([x_min, x_max, y_min, y_max])

        plt.plot(x_projeção, y_projeção, ls_projeção)
        plt.plot(x_censo, y_censo, ls_censo)

        plt.show()


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

class PP_Main():
	__slots__=()
	def projeta(self):
		self.x_ajuste = list(np.arange(- 0.005*self.t0 + self.t0, self.t5, 0.1))
		self.x_censo = [self.t0, self.t1, self.t2]
		self.y_censo = [self.P0, self.P1, self.P2]

		self.inicializaConstantes()

		self.P3_PA, self.P3_PG, self.P3_TD, self.P3_CL = self.projeções(self.t3)
		self.P4_PA, self.P4_PG, self.P4_TD, self.P4_CL = self.projeções(self.t4)
		self.P5_PA, self.P5_PG, self.P5_TD, self.P5_CL = self.projeções(self.t5)
		
		self.preenche_y_ajuste()
        
		self.criaGráfico(self.x_ajuste, self.y_PA_ajuste, '-', self.x_censo, self.y_censo, 'o')
		self.criaGráfico(self.x_ajuste, self.y_PG_ajuste, '-', self.x_censo, self.y_censo, 'o')
		self.criaGráfico(self.x_ajuste, self.y_TD_ajuste, '-', self.x_censo, self.y_censo, 'o')
		self.criaGráfico(self.x_ajuste, self.y_CL_ajuste, '-', self.x_censo, self.y_censo, 'o')                        


def factory_PP(ppinit):
	global ppresults

	d=dict(ppinit, **ppresults)

	class PP(PP_Methods, PP_Part1, PP_Part2, PP_Part3,
	            PP_Part3, Extras, PP_Main):
	    __slots__ = [key for key in d]
	    def __init__(self):
	        for key in d:
	            setattr(self, key, d[key])
	return PP
'''