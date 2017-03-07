import unittest

from calha_parshall import factoryCalhaParshall, cpinit, cpresults

# Link interessante
# http://www.dec.ufcg.edu.br/saneamento/PARSHALL.html


cpinit_test1 = dict(cpinit)
cpresults_test1 = dict(cpresults)

cpresults_test1['mu'] = 0.001065
cpresults_test1['rho'] = 998.68
cpresults_test1['W'] = 2.44
cpresults_test1['A'] = 2.44
cpresults_test1['B'] = 2.392
cpresults_test1['B23'] = 1.6
cpresults_test1['C'] = 2.745
cpresults_test1['D'] = 3.4
cpresults_test1['E'] = 0.915
cpresults_test1['F'] = 0.61
cpresults_test1['L'] = 0.915
cpresults_test1['K'] = 0.076
cpresults_test1['N'] = 0.229
cpresults_test1['k'] = 0.389
cpresults_test1['n'] = 0.627
cpresults_test1['H0'] = 0.363
cpresults_test1['D0'] = 3.08
cpresults_test1['U0'] = 1.073
cpresults_test1['q'] = 0.492
cpresults_test1['E0'] = 0.651
cpresults_test1['U1'] = 3.108
cpresults_test1['h1'] = 0.158
cpresults_test1['F1'] = 2.5
cpresults_test1['h2'] = 0.485
cpresults_test1['h3'] = 0.331
cpresults_test1['U3'] = 1.318
cpresults_test1['Lr'] = 1.962
cpresults_test1['h'] = 0.113
cpresults_test1['Tm'] = 0.89
cpresults_test1['Gm'] = 1078


cpinit_test1['Q'] = 1.2
cpinit_test1['g'] = 9.807
cpinit_test1['T'] = 17.5
cpinit_test1['c'] = 6
cpinit_test1['iW'] = 10


def testsNível1(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp
        
        def test_W(self):
            self.assertTrue( abs(self.cp.W - self.W) < 10**(-1), 
            'A variavel W esta errada. O valor deveria ser W={}, mas é {}'
            .format(self.W, self.cp.W)) 

        def test_A(self):
            self.assertTrue( abs(self.cp.A - self.A) < 10**(-2), 
            'A variavel A esta errada. O valor deveria ser A={}, mas é {}'
            .format(self.A, self.cp.A)) 

        def test_B(self):
            self.assertTrue( abs(self.cp.B - self.B) < 10**(-2), 
            'A variavel B esta errada. O valor deveria ser B={}, mas é {}'
            .format(self.B, self.cp.B))

        def test_C(self):
            self.assertTrue( abs(self.cp.C - self.C) < 10**(-1), 
            'A variavel C esta errada. O valor deveria ser C={}, mas é {}'
            .format(self.C, self.cp.C)) 

        def test_D(self):
            self.assertTrue( abs(self.cp.D - self.D) < 10**(-1), 
            'A variavel D esta errada. O valor deveria ser D={}, mas é {}'
            .format(self.D, self.cp.D)) 

        def test_E(self):
            self.assertTrue( abs(self.cp.E - self.E) < 10**(-1), 
            'A variavel E esta errada. O valor deveria ser E={}, mas é {}'
            .format(self.E, self.cp.E)) 

        def test_F(self):
            self.assertTrue( abs(self.cp.F - self.F) < 10**(-1), 
            'A variavel E esta errada. O valor deveria ser F={}, mas é {}'
            .format(self.F, self.cp.F)) 

        def test_L(self):
            self.assertTrue( abs(self.cp.L - self.L) < 10**(-1), 
            'A variavel L esta errada. O valor deveria ser L={}, mas é {}'
            .format(self.L, self.cp.L)) 

        def test_K(self):
            self.assertTrue( abs(self.cp.K - self.K) < 10**(-1), 
            'A variavel K esta errada. O valor deveria ser K={}, mas é {}'
            .format(self.K, self.cp.K)) 

        def test_N(self):
            self.assertTrue( abs(self.cp.N - self.N) < 10**(-1), 
            'A variavel N esta errada. O valor deveria ser N={}, mas é {}'
            .format(self.N, self.cp.N)) 

        def test_k(self):
            self.assertTrue( abs(self.cp.k - self.k) < 10**(-1), 
            'A variavel k esta errada. O valor deveria ser k={}, mas é {}'
            .format(self.k, self.cp.k)) 

        def test_n(self):
            self.assertTrue( abs(self.cp.n - self.n) < 10**(-1), 
            'A variavel n esta errada. O valor deveria ser n={}, mas é {}'
            .format(self.n, self.cp.n))   

        def test_mu(self):
            self.assertTrue( abs(self.cp.mu - self.mu) < 10**(-1), 
            'A variavel mu esta errada. O valor deveria ser mu={}, mas é {}'
            .format(self.mu, self.cp.mu)) 

        def test_rho(self):
            self.assertTrue( abs(self.cp.rho - self.rho) < 10**(-2), 
            'A variavel rho esta errada. O valor deveria ser rho={}, mas é {}'
            .format(self.rho, self.cp.rho)) 

        def test_H0(self):
            self.assertTrue( abs(self.cp.H0 - self.H0) < 10**(-1), 
            'A variavel H0 esta errada. O valor deveria ser H0={}, mas é {}'
            .format(self.H0, self.cp.H0)) 

        def test_D0(self):
            self.assertTrue( abs(self.cp.D0 - self.D0) < 10**(-5), 
            'A variavel D0 esta errada. O valor deveria ser D0={}, mas é {}'
            .format(self.D0, self.cp.D0)) 

        def test_q(self):
            self.assertTrue( abs(self.cp.q - self.q) < 10**(-3), 
            'A variavel q esta errada. O valor deveria ser q={}, mas é {}'
            .format(self.q, self.cp.q)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível2(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_U0(self):
            self.assertTrue( abs(self.cp.U0 - self.U0) < 10**(-3), 
            'A variavel U0 esta errada. O valor deveria ser U0={}, mas é {}'
            .format(self.U0, self.cp.U0)) 

        def test_B23(self):
            self.assertTrue( abs(self.cp.B23 - self.B23) < 10**(-2), 
            'A variavel B23 esta errada. O valor deveria ser B23={}, mas é {}'
            .format(self.B23, self.cp.B23)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível3(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_E0(self):
            self.assertTrue( abs(self.cp.E0 - self.E0) < 10**(-2), 
            'A variavel E0 esta errada. O valor deveria ser E0={}, mas é {}'
            .format(self.E0, self.cp.E0)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível4(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_U1(self):
            self.assertTrue( abs(self.cp.U1 - self.U1) < 10**(-2), 
            'A variavel U1 esta errada. O valor deveria ser U1={}, mas é {}'
            .format(self.U1, self.cp.U1))

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível5(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_h1(self):
            self.assertTrue( abs(self.cp.h1 - self.h1) < 10**(-3), 
            'A variavel h1 esta errada. O valor deveria ser h1={}, mas é {}'
            .format(self.h1, self.cp.h1)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível6(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp
        
        def test_F1(self):
            self.assertTrue( abs(self.cp.F1 - self.F1) < 10**(-2), 
            'A variavel F1 esta errada. O valor deveria ser F1={}, mas é {}'
            .format(self.F1, self.cp.F1)) 

        def test_h2(self):
            self.assertTrue( abs(self.cp.h2 - self.h2) < 10**(-1), 
            'A variavel h2 esta errada. O valor deveria ser h2={}, mas é {}'
            .format(self.h2, self.cp.h2)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível7(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])      
        def tearDown(self):
            del self.cp

        def test_Lr(self):
            self.assertTrue( abs(self.cp.Lr - self.Lr) < 10**(-2), 
            'A variavel Lr esta errada. O valor deveria ser Lr={}, mas é {}'
            .format(self.Lr, self.cp.Lr)) 

        def test_h3(self):
            self.assertTrue( abs(self.cp.h3 - self.h3) < 10**(-1), 
            'A variavel h3 esta errada. O valor deveria ser h3={}, mas é {}'
            .format(self.h3, self.cp.h3)) 
            
        def test_h(self):
            self.assertTrue( abs(self.cp.h - self.h) < 10**(-1), 
            'A variavel h esta errada. O valor deveria ser h={}, mas é {}'
            .format(self.h, self.cp.h))

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível8(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_U3(self):
            self.assertTrue( abs(self.cp.U3 - self.U3) < 10**(-1), 
            'A variavel U3 esta errada. O valor deveria ser U3={}, mas é {}'
            .format(self.U3, self.cp.U3)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível9(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_Tm(self):
            self.assertTrue( abs(self.cp.Tm - self.Tm) < 10**(-2), 
            'A variavel Tm esta errada. O valor deveria ser Tm={}, mas é {}'
            .format(self.Tm, self.cp.Tm)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível10(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factoryCalhaParshall(args)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_Gm(self):
            self.assertTrue( abs(self.cp.Gm - self.Gm) < 10**(1), 
            'A variavel Gm esta errada. O valor deveria ser Gm={}, mas é {}'
            .format(self.Gm, self.cp.Gm))

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)


n1 = testsNível1(cpinit_test1, cpresults_test1)  
n2 = testsNível2(cpinit_test1, cpresults_test1)  
n3 = testsNível3(cpinit_test1, cpresults_test1)  
n4 = testsNível4(cpinit_test1, cpresults_test1)  
n5 = testsNível5(cpinit_test1, cpresults_test1)  
n6 = testsNível6(cpinit_test1, cpresults_test1)  
n7 = testsNível7(cpinit_test1, cpresults_test1)  
n8 = testsNível8(cpinit_test1, cpresults_test1)  
n9 = testsNível9(cpinit_test1, cpresults_test1)  
n10 = testsNível10(cpinit_test1, cpresults_test1)  

exemploLivro = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

alltests = unittest.TestSuite(exemploLivro)
result = unittest.TextTestRunner(verbosity=2).run(alltests)
        