import unittest
from vazões_água import factory_VA, vainit, varesults

test1_vainit = dict(vainit)
test1_vainit['QPC'] = 200
test1_vainit['K1'] = 1.2
test1_vainit['K2'] = 1.5
test1_vainit['t3'] = 2017
test1_vainit['t4'] = 2027
test1_vainit['t5'] = 2037
test1_vainit['P3'] = 13000
test1_vainit['P4'] = 28000
test1_vainit['P5'] = 35000

test1_varesults = dict(varesults)
test1_varesults['QMín'] = 1
test1_varesults['QMéd'] = 1
test1_varesults['QMáx'] = 1
test1_varesults['out'] = 1

def test_VA_dimensionar(args_va, args_tests):
	class MyTestCase(unittest.TestCase):
		def setUp(self):
			VA = factory_VA(args_va)
			self.va = VA()
			self.va.calcular()   

			d = dict(args_va, **args_tests)
			for key in d:
				setattr(self, key, d[key])     

		def tearDown(self):
			del self.va
        
		def test_fQ(self):
			#self.assertTrue( 0 == 1)
			# self.va.fQ(K1, K2, QPC, P)
			self.assertEqual(self.va.fQ(1, 0, 0, 0), 0 )
			self.assertEqual(self.va.fQ(1, 1, 1, 1), 1/86400 )
			self.assertEqual((1,2), (1,2.1))
#		def test_vazões(self):
#			self.assertTrue(self.va.vazões())
			
        
	return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)


ex1 = test_VA_dimensionar(test1_vainit, test1_varesults)
suite1=[ex1]
alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)


