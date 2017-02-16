import unittest

import random 

from projeção_populacional import factory_PP, ppinit



PP = factory_PP(ppinit)

class Level_1(unittest.TestCase):    
	def test_checaCL(self):
		# P0, P1, P2
		self.assertEqual(PP.checaCL(0, 0, 0), False)
		self.assertEqual(PP.checaCL(0, 1, 0), False)
		self.assertEqual(PP.checaCL(1, 1, 1), False)

		self.assertEqual(PP.checaCL(10, 5, 8), False)	
		self.assertEqual(PP.checaCL(1, 8, 6), False)	

		# A função checaCL retorna falso nesse caso porque mesmo com P0<P1<P2,
		# o fPs pode ser negativo como neste teste.
		self.assertEqual(PP.checaCL(30, 46, 73), False)
	
	def test_checaTD(self):	
		self.assertEqual(PP.checaTD(30, 46, 73), True)


	def test_fKdArgLog(self):
		self.assertTrue(PP.fKdArgLog(4, 10, 42)<0)
		self.assertTrue(PP.fKdArgLog(21, 99, 76)<0)	
	
	def test_fK1ArgLog(P0, P1, Ps):
		self.assertTrue(PP.fK1ArgLog(4, 10, 42)<0)				

	def test_fPs(self):
		# Mesmo com P0<P1<P2, o fPs pode ser negativo como neste teste
		self.assertTrue(PP.fPs(30, 46, 73) < 0)


n1 = unittest.TestLoader().loadTestsFromTestCase(Level_1)
suite1=[n1]
alltests = unittest.TestSuite(suite1)
#result = unittest.TextTestRunner(verbosity=2).run(alltests)


for i in range(10**1):
	n=2
	P0 = random.randint(1, 10**n)
	P1 = random.randint(1, 10**n)
	P2 = random.randint(1, 10**n)
	try:
		
		if P0*P2<P1**2 :
			Ps = PP.fPs(P0, P1, P2)
			if PP.fKdArgLog(P0, P1, Ps) < 0:
				print(P0, P1, P2)
	except:
		print("Algo errado", P0, P1, P2)
		Ps = PP.fPs(P0, P1, P2)

