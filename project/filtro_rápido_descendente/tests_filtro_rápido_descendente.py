import unittest
#from uasb import UASB
from filtro_rápido_descendente import factory_FRD


from math import log10


d10=0.5
CU=1.5

d90= d10*10**(1.67*log10(CU))

print(d90)


def fGa(d90, rho, rhop, g, mu):
    num=(d90**3)*rho*(rhop - rho)*g
    den=mu**2
    return num/den



rho=998.2
rhop=2750
g=9.81
mu=0.001007


print(fGa(d90/1000, rho, rhop, g, mu))




