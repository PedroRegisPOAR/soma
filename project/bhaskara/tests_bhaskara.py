import unittest
from bhaskara import Bhaskara


def test_bhaskara_fdelta(a=None, b=None, c=None, delta=None):
    class MyTestCase(unittest.TestCase):
        def test_fdelta(self):
            fdelta=Bhaskara.fdelta(a,b,c)
            self.assertTrue(abs(fdelta - delta) < 10**(-1), "O método fdelta esta errado. O valor deveria ser: {}, mas é {}".format(delta, fdelta)) 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def test_bhaskara_fsqrt_delta(delta=None, sqrt_delta=None):
    class MyTestCase(unittest.TestCase):
        def test_fsqrt_delta(self):
            fsqrt_delta=Bhaskara.fsqrt_delta(delta)
            self.assertTrue(abs(fsqrt_delta - sqrt_delta) < 10**(-1), "O método fsqrt_delta esta errado. O valor deveria ser: {}, mas é {}".format(sqrt_delta, fsqrt_delta)) 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)


t1_fdelta=test_bhaskara_fdelta(a=1, b=0, c=0, delta=0)
t2_fdelta=test_bhaskara_fdelta(a=1, b=1, c=0, delta=1)
t3_fdelta=test_bhaskara_fdelta(a=3, b=4, c=10, delta=-104)
suite1_fdelta=[t1_fdelta, t2_fdelta, t3_fdelta]

t1_fsqrt_delta=test_bhaskara_fsqrt_delta(delta=0, sqrt_delta=0)
t2_fsqrt_delta=test_bhaskara_fsqrt_delta(delta=25, sqrt_delta=5)
suite2_fsqrt_delta=[t1_fsqrt_delta, t2_fsqrt_delta]


alltests = unittest.TestSuite(suite1_fdelta + suite2_fsqrt_delta)

result = unittest.TextTestRunner(verbosity=2).run(alltests)


#   https://www.youtube.com/watch?v=FxSsnHeWQBY

'''
b=Bhaskara(1,2,4)
b.calculate_roots()
print(b.out)
'''