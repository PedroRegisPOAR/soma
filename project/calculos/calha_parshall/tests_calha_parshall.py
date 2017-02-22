import unittest

from calha_parshall import factory_CP, cpinit, cpresults

# Link interessante
# http://www.dec.ufcg.edu.br/saneamento/PARSHALL.html



cpinit_test1 = dict(cpinit)
cpresults_test1 = dict(cpresults)

cpresults_test1['mu'] = 0.001065
cpresults_test1['rho'] = 998.68
cpresults_test1['W'] = 2.44
cpresults_test1['C'] = 2.745
cpresults_test1['D'] = 3.4
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
cpresults_test1['L'] = 1.962
cpresults_test1['h'] = 0.113
cpresults_test1['Tm'] = 0.89
cpresults_test1['Gm'] = 1078


cpinit_test1['Q'] = 1.2
cpinit_test1['g'] = 9.807
cpinit_test1['T'] = 17.5
cpinit_test1['iW'] = 10


def test_CP(args_cp, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            CP = factory_CP(args_cp)
            self.cp = CP()
            self.cp.dimensionar()   

            d = dict(args_cp, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.cp

        def test_W(self):
            self.assertTrue( abs(self.cp.W - self.W) < 10**(-1), 
            'A variavel W esta errada. O valor deveria ser W={}, mas é {}'
            .format(self.W, self.cp.W)) 

        def test_mu(self):
            self.assertTrue( abs(self.cp.mu - self.mu) < 10**(-1), 
            'A variavel mu esta errada. O valor deveria ser mu={}, mas é {}'
            .format(self.mu, self.cp.mu)) 

        def test_rho(self):
            self.assertTrue( abs(self.cp.rho - self.rho) < 10**(-2), 
            'A variavel rho esta errada. O valor deveria ser rho={}, mas é {}'
            .format(self.rho, self.cp.rho)) 

        def test_C(self):
            self.assertTrue( abs(self.cp.C - self.C) < 10**(-1), 
            'A variavel C esta errada. O valor deveria ser C={}, mas é {}'
            .format(self.C, self.cp.C)) 

        def test_D(self):
            self.assertTrue( abs(self.cp.D - self.D) < 10**(-1), 
            'A variavel D esta errada. O valor deveria ser D={}, mas é {}'
            .format(self.D, self.cp.D)) 

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

        def test_H0(self):
            self.assertTrue( abs(self.cp.H0 - self.H0) < 10**(-1), 
            'A variavel H0 esta errada. O valor deveria ser H0={}, mas é {}'
            .format(self.H0, self.cp.H0)) 

        def test_D0(self):
            self.assertTrue( abs(self.cp.D0 - self.D0) < 10**(-5), 
            'A variavel D0 esta errada. O valor deveria ser D0={}, mas é {}'
            .format(self.D0, self.cp.D0)) 

        def test_U0(self):
            self.assertTrue( abs(self.cp.U0 - self.U0) < 10**(-3), 
            'A variavel U0 esta errada. O valor deveria ser U0={}, mas é {}'
            .format(self.U0, self.cp.U0)) 

        def test_q(self):
            self.assertTrue( abs(self.cp.q - self.q) < 10**(-3), 
            'A variavel q esta errada. O valor deveria ser q={}, mas é {}'
            .format(self.q, self.cp.q)) 

        def test_E0(self):
            self.assertTrue( abs(self.cp.E0 - self.E0) < 10**(-2), 
            'A variavel E0 esta errada. O valor deveria ser E0={}, mas é {}'
            .format(self.E0, self.cp.E0)) 

        def test_U1(self):
            self.assertTrue( abs(self.cp.U1 - self.U1) < 10**(-2), 
            'A variavel U1 esta errada. O valor deveria ser U1={}, mas é {}'
            .format(self.U1, self.cp.U1)) 

        def test_h1(self):
            self.assertTrue( abs(self.cp.h1 - self.h1) < 10**(-3), 
            'A variavel h1 esta errada. O valor deveria ser h1={}, mas é {}'
            .format(self.h1, self.cp.h1)) 

        def test_F1(self):
            self.assertTrue( abs(self.cp.F1 - self.F1) < 10**(-2), 
            'A variavel F1 esta errada. O valor deveria ser F1={}, mas é {}'
            .format(self.F1, self.cp.F1)) 

        def test_h2(self):
            self.assertTrue( abs(self.cp.h2 - self.h2) < 10**(-1), 
            'A variavel h2 esta errada. O valor deveria ser h2={}, mas é {}'
            .format(self.h2, self.cp.h2)) 

        def test_h3(self):
            self.assertTrue( abs(self.cp.h3 - self.h3) < 10**(-1), 
            'A variavel h3 esta errada. O valor deveria ser h3={}, mas é {}'
            .format(self.h3, self.cp.h3)) 

        def test_U3(self):
            self.assertTrue( abs(self.cp.U3 - self.U3) < 10**(-1), 
            'A variavel U3 esta errada. O valor deveria ser U3={}, mas é {}'
            .format(self.U3, self.cp.U3)) 

        def test_L(self):
            self.assertTrue( abs(self.cp.L - self.L) < 10**(-2), 
            'A variavel L esta errada. O valor deveria ser L={}, mas é {}'
            .format(self.L, self.cp.L)) 

        def test_h(self):
            self.assertTrue( abs(self.cp.h - self.h) < 10**(-1), 
            'A variavel h esta errada. O valor deveria ser h={}, mas é {}'
            .format(self.h, self.cp.h)) 

        def test_Tm(self):
            self.assertTrue( abs(self.cp.Tm - self.Tm) < 10**(-2), 
            'A variavel Tm esta errada. O valor deveria ser Tm={}, mas é {}'
            .format(self.Tm, self.cp.Tm)) 

        def test_Gm(self):
            self.assertTrue( abs(self.cp.Gm - self.Gm) < 10**(1), 
            'A variavel Gm esta errada. O valor deveria ser Gm={}, mas é {}'
            .format(self.Gm, self.cp.Gm)) 
    
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)            
        



exemploLivro = test_CP(cpinit_test1, cpresults_test1)  


#n1 = unittest.TestLoader().loadTestsFromTestCase(exemplo)
#suite1=[exemploLivro, ]
suite1=[exemploLivro]

alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)
        



def myprint(cp):
    print("W = ", cp.out['W'])
    print("C = ", cp.out['C'])
    print("D = ", cp.out['D'])
    print("K = ", cp.out['K'])
    print("N = ", cp.out['N'])

    print("k = ", cp.out['k'])
    print("n = ", cp.out['n'])

    print("H0 = ", cp.out['H0'])
    print("D0 = ", cp.out['D0'])
    print("U0 = ", cp.out['U0'])

    print("q = ", cp.out['q'])
    print("E0 = ", cp.out['E0'])
    print("U1 = ", cp.out['U1'])
    print("h1 = ", cp.out['h1'])

    print("F1 = ", cp.out['F1'])

    print("h2 = ", cp.out['h2'])
    print("h3 = ", cp.out['h3'])
    print("U3 = ", cp.out['U3'])

    print("L = ", cp.out['L'])
    print("h = ", cp.out['h'])

    print("T = ", cp.out['Tm'])
    print("G = ", cp.out['Gm'])









