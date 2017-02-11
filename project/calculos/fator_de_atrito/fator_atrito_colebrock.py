#from scipy.optimize import minimize
from math import log10

# O servidor não importa o scipy :(
'''
def colebrook_white(f0, args):
    epsilon=args[0]
    Re=args[1]
    D=args[2]
    return f0**(-1/2) + 2*log10(epsilon/(3.7*D) + 2.51/(Re*f0**(1/2)))

def f(f0, args):
    return (colebrook_white(f0, args))**2


epsilon=0.0035
Re=13400
D=0.15
args=[epsilon, Re, D]

f0=0.3164*Re**(-0.25)
res = minimize(f, f0, args, method='nelder-mead', options={'xtol': 10**(-10), 'disp': True})

print("res.x      = ", res.x)
print(0.3164*Re**(-0.25))


def result_colebrook_white(epsilon, Re, D):
	args=[epsilon, Re, D]
	f0=0.3164*Re**(-0.25)	
	#res = minimize(f, f0, args, method='nelder-mead', options={'xtol': 10**(-6), 'disp': True})
	return None #{'epsilon': epsilon, 'Re':Re, 'D':D, 'f':res.x[0]}
'''


def ftest(x):
	return x**2

def métodoDaBisseção(a, b, Precisão, MáximoIterações, função, *args):
    Erro=1.0
    x=a
    Iterações=0
    
    if função(a, *args)*função(b, *args) < 0:
        while Erro > 10**(-Precisão) or Iterações <= MáximoIterações:
            xanterior = x
            
            x = (a + b) / 2
            
            if função(x, *args)*função(b, *args) < 0:
                a = x
            else:
                b = x
            
            Erro = abs((x - xanterior) / x)
            Iterações = Iterações + 1
        
        return x
    else:
        return  "Erro"
        exit

def colebrook_white(f, epsilon, Re, D):
    return f**(-1/2) + 2*log10(epsilon/(3.7*D) + 2.51/(Re*f**(1/2)))

# TO DO: Por hora o numero de iterações esta bem alto para "tornar mais provavel que se atinja a 
# precisão desejada". Isso deve ser melhorado.
def solução_Colebrook_White(epsilon, Re, D):
	f = métodoDaBisseção(10**(-5), 0.5, 5, 250, colebrook_white, epsilon, Re, D)
	return {'epsilon': epsilon, 'Re':Re, 'D':D, 'f':f}


# TO DO: Fazer uma classe que diz se o metodo convergiu, se não convergiu, mas mostra qual o erro atual.
'''
class MétodoDaBisseção():
	def __init__(self):
		self.falhou=True
		self.convergiu=False
		self.solução=None
		self.erro_solução=None

	def métodoDaBisseção(self, a, b, Precisão, MáximoIterações, função, *args):
	    erro=1.0
	    x=a
	    iterações=0
	    
	    if função(a, *args)*função(b, *args) < 0:
	        while Erro > 10**(-Precisão) or iterações <= MáximoIterações:
	            xanterior = x
	            
	            x = (a + b) / 2
	            
	            if função(x, *args)*função(b, *args) < 0:
	                a = x
	            else:
	                b = x
	            
	            erro = abs((x - xanterior) / x)
	            iterações = iterações + 1

	        if erro > 10**(-Precisão):
	        	self.convergiu=True
	        	self.falhou=False
	        else:
	        	self.solução=x
	        	self.erro_solução=Erro
	        	self.falhou=False
#	        return x
	    else:
	        return  "Erro"
	        exit
'''


