#from scipy.optimize import minimize
from math import log10

def colebrook_white(f0, args):
    epsilon=args[0]
    Re=args[1]
    D=args[2]
    return f0**(-1/2) + 2*log10(epsilon/(3.7*D) + 2.51/(Re*f0**(1/2)))

def f(f0, args):
    return (colebrook_white(f0, args))**2

'''
epsilon=0.0035
Re=13400
D=0.15
args=[epsilon, Re, D]

f0=0.3164*Re**(-0.25)
res = minimize(f, f0, args, method='nelder-mead', options={'xtol': 10**(-10), 'disp': True})

print("res.x      = ", res.x)
print(0.3164*Re**(-0.25))
'''

def result_colebrook_white(epsilon, Re, D):
	args=[epsilon, Re, D]
	f0=0.3164*Re**(-0.25)	
	#res = minimize(f, f0, args, method='nelder-mead', options={'xtol': 10**(-6), 'disp': True})
	return None #{'epsilon': epsilon, 'Re':Re, 'D':D, 'f':res.x[0]}


