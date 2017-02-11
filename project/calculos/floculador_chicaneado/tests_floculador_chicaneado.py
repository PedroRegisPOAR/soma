import unittest
from floculador_chicaneado import factory_FloculadorChicaneado



#####
args_FloculadorChicaneado={
"T":15,
}
#####

#####
args_tests_FloculadorChicaneado={
"mu":0.00113,
"rho":999.1,
}
#####

def test_FloculadorChicaneado_dimensionar(args_uasb, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            FloculadorChicaneado=factory_FloculadorChicaneado(args_uasb)
            self.fc=FloculadorChicaneado()
#            self.fc.dimensionar()  
            
            d=dict(args_uasb, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.fc

        
        def test_mu(self):
            self.assertTrue( abs(self.fc.mu - self.mu) < 10**(-4), "A variavel mu esta errada. O valor deveria ser mu={}, mas é {}".format(self.mu, self.fc.mu)) 
        
        def test_rho(self):
            self.assertTrue( abs(self.fc.rho - self.rho) < 10**(-1), "A variavel rho esta errada. O valor deveria ser rho={}, mas é {}".format(self.rho, self.fc.rho)) 

                
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)



ex = test_FloculadorChicaneado_dimensionar(args_FloculadorChicaneado, 
	args_tests_FloculadorChicaneado)

suite1=[ex]
alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)





