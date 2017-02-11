import unittest
from klassName import factory_KlassName



#####
args_uasb={
"A":67890,
}
#####

#####
args_tests={
"X":12345,
}
#####

def test_KlassName_dimensionar(args_uasb, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            KlassName=factory_KlassName(args_uasb)
            self.o=KlassName()
            self.o.dimensionar()   
            
            d=dict(args_uasb, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.o

        
        def test_X(self):
            self.assertTrue( abs(self.o.X - self.X) < 10**(-1), "A variavel X esta errada. O valor deveria ser X={}, mas é {}".format(self.X, self.o.X)) 
        
                
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)



ex_prof = test_KlassName_dimensionar(args_KlassName, args_tests)

suite1=[ex_prof]
alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)





