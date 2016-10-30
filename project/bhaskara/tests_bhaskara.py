import unittest
from bhaskara import Bhaskara

'''
class BhaskaraMethodsTests(unittest.TestCase):
    def test_fdelta(self):
        a=0
        b=0
        c=0
        fdelta=Bhaskara.fdelta(a,b,c)
        delta=1
        self.assertTrue( abs(fdelta - delta) < 10**(-3), "O método fdelta esta errado. O valor deveria ser: {}, mas é {}".format(delta, fdelta))
'''

def test_bhaskara_fdelta(a=None, b=None, c=None, delta=None):
    class MyTestCase(unittest.TestCase):
        def test_foo(self):
            fdelta=Bhaskara.fdelta(a,b,c)
            self.assertTrue(abs(fdelta - delta) < 10**(-1), "O método fdelta esta errado. O valor deveria ser: {}, mas é {}".format(delta, fdelta)) 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)



t1_fdelta=test_bhaskara_fdelta(a=1, b=0, c=0, delta=0)
t2_fdelta=test_bhaskara_fdelta(a=1, b=1, c=0, delta=1)
t3_fdelta=test_bhaskara_fdelta(a=3, b=4, c=10, delta=-104)

suite1_fdelta=[t1_fdelta, t2_fdelta, t3_fdelta]

alltests = unittest.TestSuite(suite1_fdelta)

result = unittest.TextTestRunner(verbosity=2).run(alltests)


#   https://www.youtube.com/watch?v=FxSsnHeWQBY

'''
b=Bhaskara(1,2,4)
b.calculate_roots()
print(b.out)
'''