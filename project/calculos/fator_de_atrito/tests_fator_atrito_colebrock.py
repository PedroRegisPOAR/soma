import unittest
from fator_atrito_colebrock import métodoDaBisseção, colebrook_white


class Test_MétodoDaBisseção(unittest.TestCase):
	def test_1(self):
		def f(x,k):
			return x**2 - k
		mb=métodoDaBisseção(-1, 5, 4, 50, f, 2)
		self.assertTrue(abs(mb - 2**(1/2)) < 10**(-8), "O teste 1 do MétodoDaBisseção esta errado. O valor deveria ser: {}, mas é {}".format(2**(1/2),mb)) 


class Test_Solução_Colebrook_White(unittest.TestCase):
	def test_1(self):
		epsilon=0.0035
		Re=13400
		D=0.15
		cw=métodoDaBisseção(10**(-4), 0.5, 3, 250, colebrook_white, epsilon, Re, D)
		gab_cw=0.0541806444873049
		self.assertTrue(abs(cw - gab_cw) < 10**(-12), "O teste 1 do métodoDaBisseção esta errado. O valor deveria ser: {}, mas é {}".format(gab_cw,cw)) 

	#	https://www.wolframalpha.com/input/?i=solve+f%5E(-1%2F2)+%2B+2*log10(0.0035%2F(3.7*0.9)+%2B+2.51%2F(1400*f%5E(1%2F2)))
	def test_2(self):
		epsilon=0.0035
		Re=13400
		D=0.9
		cw=métodoDaBisseção(10**(-4), 0.5, 3, 250, colebrook_white, epsilon, Re, D)
		gab_cw=0.03463518057605736698253056410
		self.assertTrue(abs(cw - gab_cw) < 10**(-12), "O teste 2 do métodoDaBisseção esta errado. O valor deveria ser: {}, mas é {}".format(gab_cw,cw)) 

	def test_3(self):
		epsilon=0.0035
		Re=1400
		D=0.9
		cw=métodoDaBisseção(10**(-4), 0.5, 3, 250, colebrook_white, epsilon, Re, D)
		gab_cw=0.0582522259242826076229411
		self.assertTrue(abs(cw - gab_cw) < 10**(-12), "O teste 3 do métodoDaBisseção esta errado. O valor deveria ser: {}, mas é {}".format(gab_cw,cw)) 




test1=unittest.TestLoader().loadTestsFromTestCase(Test_MétodoDaBisseção)
suite1=[test1]

test2=unittest.TestLoader().loadTestsFromTestCase(Test_Solução_Colebrook_White)
suite2=[test1, test2]

alltests = unittest.TestSuite(suite2)
result = unittest.TextTestRunner(verbosity=2).run(alltests)