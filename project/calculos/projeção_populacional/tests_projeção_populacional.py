import unittest

import random 

from projeção_populacional import factory_PP, ppinit



for x in range(1,10):
	for key in ppinit:
	    ppinit[key] = random.randint(1,9)

	PP=factory_PP(ppinit)
	pp=PP()    
	pp.verificação()
