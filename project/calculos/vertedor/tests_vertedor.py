import unittest

from vertedor import factoryVertedor, vertedorinit, vertedorresults


V = factoryVertedor(vertedorinit)

class TestesEquaçõesSimples(unittest.TestCase):    
    def test_fyc(self):
        # fyc(Q, g, b)
        self.assertTrue( abs(V.fyc(1, 1, 1) - 1) < 10**(-3))

class TestesOtimização(unittest.TestCase):    
    def test_fPvr(self):
        # fyc(Q, g, b)
        g = 9.8
        b = 0.5
        Q = 0.08 
        F1 = 2.74
        Pvr = 0.70
        x = V.fPvr(Q, F1, g, b)
        self.assertTrue( abs(x - Pvr) < 10**(-2))


vertedorinit_test_níveis = dict(vertedorinit)
vertedorresults_test_níveis = dict(vertedorresults)

vertedorinit_test_níveis['Q'] = 0.08
vertedorinit_test_níveis['g'] = 9.81
vertedorinit_test_níveis['T'] = 17.5
vertedorinit_test_níveis['b'] = 0.5
vertedorinit_test_níveis['F1'] = 2.734

vertedorresults_test_níveis['Pvr'] = 0.70
vertedorresults_test_níveis['yc'] = 0.138
vertedorresults_test_níveis['y1'] = 0.070
vertedorresults_test_níveis['v1'] = 2.271
vertedorresults_test_níveis['F1c'] = 2.734
vertedorresults_test_níveis['y2'] = 0.239
vertedorresults_test_níveis['En'] = 0.079
vertedorresults_test_níveis['v2'] = 0.668
vertedorresults_test_níveis['Um'] = 1.470
vertedorresults_test_níveis['Lr'] = 0.845
vertedorresults_test_níveis['gamma'] = 9797
vertedorresults_test_níveis['mu'] = 0.001065
vertedorresults_test_níveis['Tm'] = 0.575
vertedorresults_test_níveis['Gm'] = 1069

def tests_Nível1(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_gamma(self):
            self.assertTrue( abs(self.v.gamma - self.gamma) < 10**(0), 
            """A variavel gamma esta errada. O valor deveria ser gamma={},
             mas é {}""".format(self.gamma, self.v.gamma)) 

        def test_mu(self):
            self.assertTrue( abs(self.v.mu - self.mu) < 10**(-5), 
            """A variavel mu esta errada. O valor deveria ser mu={},
             mas é {}""".format(self.mu, self.v.mu)) 

        def test_Pvr(self):
            self.assertTrue( abs(self.v.Pvr - self.Pvr) < 10**(-1), 
            """A variavel Pvr esta errada. O valor deveria ser Pvr={},
             mas é {}""".format(self.Pvr, self.v.Pvr)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível2(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_y1(self):
            self.assertTrue( abs(self.v.y1 - self.y1) < 10**(-3), 
            """A variavel y1 esta errada. O valor deveria ser y1={},
             mas é {}""".format(self.y1, self.v.y1)) 

        def test_yc(self):
            self.assertTrue( abs(self.v.yc - self.yc) < 10**(-3), 
            """A variavel yc esta errada. O valor deveria ser yc={},
             mas é {}""".format(self.yc, self.v.yc)) 
    
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível3(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_v1(self):
            self.assertTrue( abs(self.v.v1 - self.v1) < 10**(-2), 
            """A variavel v1 esta errada. O valor deveria ser v1={},
             mas é {}""".format(self.v1, self.v.v1)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível4(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_F1(self):
            self.assertTrue( abs(self.v.F1c - self.F1c) < 10**(-3), 
            """A variavel F1c esta errada. O valor deveria ser F1c={},
             mas é {}""".format(self.F1c, self.v.F1c)) 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível5(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_y2(self):
            self.assertTrue( abs(self.v.y2 - self.y2) < 10**(-3), 
            """A variavel y2 esta errada. O valor deveria ser y2={},
             mas é {}""".format(self.y2, self.v.y2)) 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível6(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_En(self):
            self.assertTrue( abs(self.v.En - self.En) < 10**(-2), 
            """A variavel En esta errada. O valor deveria ser En={},
             mas é {}""".format(self.En, self.v.En)) 

        def test_v2(self):
            self.assertTrue( abs(self.v.v2 - self.v2) < 10**(-3), 
            """A variavel v2 esta errada. O valor deveria ser v2={},
             mas é {}""".format(self.v2, self.v.v2)) 

        def test_Lr(self):
            self.assertTrue( abs(self.v.Lr - self.Lr) < 10**(-3), 
            """A variavel Lr esta errada. O valor deveria ser Lr={},
             mas é {}""".format(self.Lr, self.v.Lr)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível7(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_Um(self):
            self.assertTrue( abs(self.v.Um - self.Um) < 10**(-3), 
            """A variavel Um esta errada. O valor deveria ser Um={},
             mas é {}""".format(self.Um, self.v.Um)) 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível8(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_Tm(self):
            self.assertTrue( abs(self.v.Tm - self.Tm) < 10**(-3), 
            """A variavel Tm esta errada. O valor deveria ser Tm={},
             mas é {}""".format(self.Tm, self.v.Tm)) 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def tests_Nível9(args_v, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            V = factoryVertedor(args_v)
            self.v = V()
            self.v.dimensionar()   

            d = dict(args_v, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.v

        def test_Gm(self):
            self.assertTrue( abs(self.v.Gm - self.Gm) < 10**(0), 
            """A variavel Gm esta errada. O valor deveria ser Gm={},
             mas é {}""".format(self.Gm, self.v.Gm)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)



n1 = tests_Nível1(vertedorinit_test_níveis, vertedorresults_test_níveis)
n2 = tests_Nível2(vertedorinit_test_níveis, vertedorresults_test_níveis)
n3 = tests_Nível3(vertedorinit_test_níveis, vertedorresults_test_níveis)
n4 = tests_Nível4(vertedorinit_test_níveis, vertedorresults_test_níveis)
n5 = tests_Nível5(vertedorinit_test_níveis, vertedorresults_test_níveis)
n6 = tests_Nível6(vertedorinit_test_níveis, vertedorresults_test_níveis)
n7 = tests_Nível7(vertedorinit_test_níveis, vertedorresults_test_níveis)
n8 = tests_Nível8(vertedorinit_test_níveis, vertedorresults_test_níveis)
n9 = tests_Nível9(vertedorinit_test_níveis, vertedorresults_test_níveis)

testes_equações = unittest.TestLoader().loadTestsFromTestCase(
    TestesEquaçõesSimples)

testes_otmização = unittest.TestLoader().loadTestsFromTestCase(
    TestesOtimização)

suite1 = [testes_equações, testes_otmização]
suite2_níveis = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

suite = suite2_níveis
alltests = unittest.TestSuite(suite)
result = unittest.TextTestRunner(verbosity=2).run(alltests)

