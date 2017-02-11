import unittest
from vazões_esgoto import factory_VE, veinit, veresults


VE = factory_VE(veinit)

class Level_1(unittest.TestCase):    
	def test_fKmédio(self):
		self.assertEqual(VE.fKmédio(1, 1), 1)

	def test_comprimentos(self):
		# comprimentos(self, r, P3, P4, P5)
		self.assertEqual(VE.comprimentos(2, 3, 4, 5), (6, 8, 10))			

class Level_2(unittest.TestCase):
	def test_vazõesInfiltração(self):
		self.assertEqual(VE.vazõesInfiltração(2, 3, 4, 5), (6, 8, 10))		

class Level_3(unittest.TestCase):
	def test_vazõesMínimas(self):
		# vazõesMínimas(CR, K3, QPC, P3, QInft3, QInft4, QInft5)			
		self.assertEqual(VE.vazõesMínimas(1, 1, 1, 1, 1, 1, 1, 1, 1), (6, 8, 10))	

	def test_vazõesMédias(self):
		# vazõesMédias(CR, Km, QPC, P3, P4, P5, QInft3, QInft4, QInft5)			
		self.assertEqual(VE.vazõesMédias(0, 99, 99, 99, 99, 99, 2, 3, 4), (2, 3, 4))	
		self.assertEqual(VE.vazõesMédias(0, 99, 99, 99, 99, 99, 0, 0, 0), (0, 0, 0))

		self.assertEqual(VE.vazõesMédias(100, 3, 4, 99, 99, 99, 2, 3, 4), (2, 3, 4))	

class Level_4(unittest.TestCase):
	def test_vazõesMáximas(self):
		# vazõesMáximas(K1, K2, QMédt3, QMédt4, QMédt5)
		self.assertEqual(VE.vazõesMáximas(2, 3, 4, 5, 6), (2*3*4, 2*3*5, 2*3*6))	


# http://stackoverflow.com/questions/3022952/test-assertions-for-tuples-with-floats
def f(a):
	return [(1.000001/x, x * 2) for x in a]


class TestDict(unittest.TestCase):
	def test_dict(self):
		self.assertEqual({'a':1, 'b':2}, {'a':1, 'b':2})

	def testF(self):
	    for tuple1, tuple2 in zip(f(range(1,3)), [(1.0, 2), (0.5, 4)]):
	        for val1, val2 in zip(tuple1, tuple2):
	            if type(val2) is float:
	                self.assertAlmostEquals(val1, val2, 5)
	            else:
	                self.assertEquals(val1, val2)

"""
n1 = unittest.TestLoader().loadTestsFromTestCase(Level_1)
n2 = unittest.TestLoader().loadTestsFromTestCase(Level_2)
n3 = unittest.TestLoader().loadTestsFromTestCase(Level_3)
n4 = unittest.TestLoader().loadTestsFromTestCase(Level_4)

test_dict  = unittest.TestLoader().loadTestsFromTestCase(TestDict)
suite1=[n1, n2, n3, n4, test_dict]
alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)
"""





veinit_test1 = dict(veinit)
veresults_test1 = dict(veresults)


veinit_test1['CR'] = 1
veinit_test1['r'] = 1
veinit_test1['K1'] = 1
veinit_test1['K2'] = 1
veinit_test1['K3'] = 1
veinit_test1['TInf'] = 1 
veinit_test1['QPC'] = 1
veinit_test1['t3'] = 1
veinit_test1['t4'] = 1
veinit_test1['t5'] = 1
veinit_test1['P3'] = 1
veinit_test1['P4'] = 1
veinit_test1['P5'] = 1


veresults_test1['Km'] = 1
veresults_test1['Lt3'] = 1
veresults_test1['Lt4'] = 1
veresults_test1['Lt5'] = 1
veresults_test1['QInft3'] = 1
veresults_test1['QInft4'] = 1
veresults_test1['QInft5'] = 1
veresults_test1['QMínt3'] = 1
veresults_test1['QMínt4'] = 1
veresults_test1['QMínt5'] = 1
veresults_test1['QMédt3'] = 1
veresults_test1['QMédt4'] = 1
veresults_test1['QMédt5'] = 1
veresults_test1['QMáxt3'] = 1
veresults_test1['QMáxt4'] = 1
veresults_test1['QMáxt5'] = 1


def test_VE_dimensionar(args_ve, args_tests):
	class MyTestCase(unittest.TestCase):
		def setUp(self):
			VE = factory_VE(args_ve)
			self.ve = VE()
			self.ve.calcular()   

			d = dict(args_ve, **args_tests)
			for key in d:
				setattr(self, key, d[key])     

		def tearDown(self):
			del self.ve

		def test_Km(self):
			self.assertTrue( abs(self.ve.Km - self.Km) < 10**(-1), 
			"""A variavel Km esta errada. O valor deveria ser Km={},
			 mas é {}""".format(self.Km, self.ve.Km)) 

		def test_Lt3(self):
			self.assertTrue( abs(self.ve.Lt3 - self.Lt3) < 10**(-1), 
			"""A variavel Lt3 esta errada. O valor deveria ser Lt3={},
			 mas é {}""".format(self.Lt3, self.ve.Lt3)) 

		def test_Lt4(self):
			self.assertTrue( abs(self.ve.Lt4 - self.Lt4) < 10**(-1), 
			"""A variavel Lt4 esta errada. O valor deveria ser Lt4={},
			 mas é {}""".format(self.Lt4, self.ve.Lt4)) 

		def test_Lt5(self):
			self.assertTrue( abs(self.ve.Lt5 - self.Lt5) < 10**(-1), 
			"""A variavel Lt5 esta errada. O valor deveria ser Lt5={},
			 mas é {}""".format(self.Lt5, self.ve.Lt5)) 

		def test_QInft3(self):
			self.assertTrue( abs(self.ve.QInft3 - self.QInft3) < 10**(-1), 
			"""A variavel QInft3 esta errada. O valor deveria ser QInft3={},
			 mas é {}""".format(self.QInft3, self.ve.QInft3)) 

		def test_QInft4(self):
			self.assertTrue( abs(self.ve.QInft4 - self.QInft4) < 10**(-1), 
			"""A variavel QInft4 esta errada. O valor deveria ser QInft4={},
			 mas é {}""".format(self.QInft4, self.ve.QInft4)) 

		def test_QInft5(self):
			self.assertTrue( abs(self.ve.QInft5 - self.QInft5) < 10**(-1), 
			"""A variavel QInft5 esta errada. O valor deveria ser QInft5={},
			 mas é {}""".format(self.QInft5, self.ve.QInft5)) 

		def test_QMínt3(self):
			self.assertTrue( abs(self.ve.QMínt3 - self.QMínt3) < 10**(-1), 
			"""A variavel QMínt3 esta errada. O valor deveria ser QMínt3={},
			 mas é {}""".format(self.QMínt3, self.ve.QMínt3)) 

		def test_QMínt4(self):
			self.assertTrue( abs(self.ve.QMínt4 - self.QMínt4) < 10**(-1), 
			"""A variavel QMínt4 esta errada. O valor deveria ser QMínt4={},
			 mas é {}""".format(self.QMínt4, self.ve.QMínt4)) 

		def test_QMínt5(self):
			self.assertTrue( abs(self.ve.QMínt5 - self.QMínt5) < 10**(-1), 
			"""A variavel QMínt5 esta errada. O valor deveria ser QMínt5={},
			 mas é {}""".format(self.QMínt5, self.ve.QMínt5)) 

		def test_QMédt3(self):
			self.assertTrue( abs(self.ve.QMédt3 - self.QMédt3) < 10**(-1), 
			"""A variavel QMédt3 esta errada. O valor deveria ser QMédt3={},
			 mas é {}""".format(self.QMédt3, self.ve.QMédt3)) 

		def test_QMédt4(self):
			self.assertTrue( abs(self.ve.QMédt4 - self.QMédt4) < 10**(-1), 
			"""A variavel QMédt4 esta errada. O valor deveria ser QMédt4={},
			 mas é {}""".format(self.QMédt4, self.ve.QMédt4)) 

		def test_QMédt5(self):
			self.assertTrue( abs(self.ve.QMédt5 - self.QMédt5) < 10**(-1), 
			"""A variavel QMédt5 esta errada. O valor deveria ser QMédt5={},
			 mas é {}""".format(self.QMédt5, self.ve.QMédt5)) 

		def test_QMáxt3(self):
			self.assertTrue( abs(self.ve.QMáxt3 - self.QMáxt3) < 10**(-1), 
			"""A variavel QMáxt3 esta errada. O valor deveria ser QMáxt3={},
			 mas é {}""".format(self.QMáxt3, self.ve.QMáxt3)) 

		def test_QMáxt4(self):
			self.assertTrue( abs(self.ve.QMáxt4 - self.QMáxt4) < 10**(-1), 
			"""A variavel QMáxt4 esta errada. O valor deveria ser QMáxt4={},
			 mas é {}""".format(self.QMáxt4, self.ve.QMáxt4)) 

		def test_QMáxt5(self):
			self.assertTrue( abs(self.ve.QMáxt5 - self.QMáxt5) < 10**(-1), 
			"""A variavel QMáxt5 esta errada. O valor deveria ser QMáxt5={},
			 mas é {}""".format(self.QMáxt5, self.ve.QMáxt5)) 

	return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)



ex1 = test_VE_dimensionar(veinit_test1, veresults_test1)
suite1=[ex1]
alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)


'''
def escreve_testes_dict(d, obj):                 
    for key in d:
        cabeçalho = 'def test_' + key + '(self):'
        corpo = '\tself.assertTrue( abs(self.'
        corpo += obj + '.' + key +' - self.' + key 
        corpo += ') < 10**(-1), '
        corpo += '\n\t"""A variavel ' + key +' esta errada. O valor deveria ser '
        corpo += key + '={},' + '\n\t' +' mas é {}"""'
        corpo += '.format(self.' + key + ', self.' + obj + '.' + key + ')) \n'        
        print(cabeçalho)
        print(corpo)

escreve_testes_dict(d, 've')


for key in veresults:
	print("veresults_test1['" + key + "'] = ")


'''