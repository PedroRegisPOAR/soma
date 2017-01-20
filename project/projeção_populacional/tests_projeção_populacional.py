import unittest

import numpy as np

from crescimento_populacional import factory_PP
from crescimento_populacional import PP_Parte4


def testcriaGráfico():

    p = PP_Parte4()

    x = list(np.arange(1, 50, 0.1))
    y = [2*t**(1/2) for t in x]

    p.criaGráfico('teste.png','', x, y, '-', [], [], '')

#testcriaGráfico()    