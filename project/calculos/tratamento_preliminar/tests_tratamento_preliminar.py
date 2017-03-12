import unittest

from tratamento_preliminar import (factoryTratamentoPreliminar,
                initTratamentoPreliminar, resultsTratamentoPreliminar)


init_test1 = dict(initTratamentoPreliminar)
results_test1 = dict(resultsTratamentoPreliminar)


init_test1['Qmáx'] = 1.73
init_test1['Qméd'] = 0.96
init_test1['Qmín'] = 0.23
init_test1['t'] = 5
init_test1['a'] = 20
init_test1['Vg'] = 1
init_test1['g'] = 9.81
init_test1['V'] = 0.3
init_test1['AreiaAcu'] = 35
init_test1['tl'] = 15



results_test1['W'] = 122
results_test1['n'] = 1.578
results_test1['lamb'] = 2.935
results_test1['Hmáx'] = 0.72
results_test1['Hmín'] = 0.2
results_test1['ymáx'] = 0.59
results_test1['ymín'] = 0.07
results_test1['Z'] = 0.12
results_test1['E'] = 0.8
results_test1['Au'] = 1.73
results_test1['S'] = 2.16
results_test1['b'] = 3.63
results_test1['V0'] = 0.8
results_test1['Deltah_limpa'] = 0.026
results_test1['Deltah_50'] = 0.245
results_test1['L'] = 13.39
results_test1['A'] = 5.76
results_test1['B'] = 9.68
results_test1['Vv'] = 0.3
results_test1['TESmáx'] = 1152
results_test1['QmédAreia'] = 2.9
results_test1['VmédAreia'] = 43.5
results_test1['A_P'] = 129.75
results_test1['H_AreiaAc'] = 0.33


def testsNível1(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            TP = factoryTratamentoPreliminar(args)
            self.tp = TP()
            self.tp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.tp
        
        def test_tabela(self):
            self.assertTrue( True) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível2(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            TP = factoryTratamentoPreliminar(args)
            self.tp = TP()
            self.tp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.tp
        
        def test_W(self):
            self.assertTrue( abs(self.tp.W - self.W) < 10**(-1), 
            'A variavel W esta errada. O valor deveria ser W={}, mas é {}'
            .format(self.W, self.tp.W)) 

        def test_n(self):
            self.assertTrue( abs(self.tp.n - self.n) < 10**(-3), 
            'A variavel n esta errada. O valor deveria ser n={}, mas é {}'
            .format(self.n, self.tp.n)) 

        def test_lamb(self):
            self.assertTrue( abs(self.tp.lamb - self.lamb) < 10**(-3), 
            'A variavel lamb esta errada. O valor deveria ser lamb={}, mas é {}'
            .format(self.lamb, self.tp.lamb))             

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível3(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            TP = factoryTratamentoPreliminar(args)
            self.tp = TP()
            self.tp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.tp

        def test_Hmín(self):
            self.assertTrue( abs(self.tp.Hmín - self.Hmín) < 10**(-2), 
            'A variavel Hmín esta errada. O valor deveria ser Hmín={}, mas é {}'
            .format(self.Hmín, self.tp.Hmín))             

        def test_Hmáx(self):
            self.assertTrue( abs(self.tp.Hmáx - self.Hmáx) < 10**(-2), 
            'A variavel Hmáx esta errada. O valor deveria ser Hmáx={}, mas é {}'
            .format(self.Hmáx, self.tp.Hmáx))

        def test_E(self):
            self.assertTrue( abs(self.tp.E - self.E) < 10**(-2), 
            'A variavel E esta errada. O valor deveria ser E={}, mas é {}'
            .format(self.E, self.tp.E))

        def test_A(self):
            self.assertTrue( abs(self.tp.A - self.A) < 10**(-2), 
            'A variavel A esta errada. O valor deveria ser A={}, mas é {}'
            .format(self.A, self.tp.A))

        def test_B(self):
            self.assertTrue( abs(self.tp.B - self.B) < 10**(-2), 
            'A variavel B esta errada. O valor deveria ser B={}, mas é {}'
            .format(self.B, self.tp.B))

        def test_Au(self):
            self.assertTrue( abs(self.tp.Au - self.Au) < 10**(-2), 
            'A variavel Au esta errada. O valor deveria ser Au={}, mas é {}'
            .format(self.Au, self.tp.Au))

        def test_QmédAreia(self):
            self.assertTrue( abs(self.tp.QmédAreia - self.QmédAreia) < 10**(-2), 
            'A variavel QmédAreia esta errada. O valor deveria ser QmédAreia={}, mas é {}'
            .format(self.QmédAreia, self.tp.QmédAreia))


    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível4(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            TP = factoryTratamentoPreliminar(args)
            self.tp = TP()
            self.tp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.tp

        def test_Z(self):
            self.assertTrue( abs(self.tp.Z - self.Z) < 10**(-2), 
            'A variavel Z esta errada. O valor deveria ser Z={}, mas é {}'
            .format(self.Z, self.tp.Z))             

        def test_S(self):
            self.assertTrue( abs(self.tp.S - self.S) < 10**(-2), 
            'A variavel S esta errada. O valor deveria ser S={}, mas é {}'
            .format(self.S, self.tp.S))

        def test_VmédAreia(self):
            self.assertTrue( abs(self.tp.VmédAreia - self.VmédAreia) < 10**(-1), 
            'A variavel VmédAreia esta errada. O valor deveria ser VmédAreia={}, mas é {}'
            .format(self.VmédAreia, self.tp.VmédAreia)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível5(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            TP = factoryTratamentoPreliminar(args)
            self.tp = TP()
            self.tp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.tp

        def test_b(self):
            self.assertTrue( abs(self.tp.b - self.b) < 10**(-2), 
            'A variavel b esta errada. O valor deveria ser b={}, mas é {}'
            .format(self.b, self.tp.b)) 

        def test_V0(self):
            self.assertTrue( abs(self.tp.V0 - self.V0) < 10**(-2), 
            'A variavel V0 esta errada. O valor deveria ser V0={}, mas é {}'
            .format(self.V0, self.tp.V0)) 

        def test_L(self):
            self.assertTrue( abs(self.tp.L - self.L) < 10**(-2), 
            'A variavel L esta errada. O valor deveria ser L={}, mas é {}'
            .format(self.L, self.tp.L)) 
        
        def test_Vv(self):
            self.assertTrue( abs(self.tp.Vv - self.Vv) < 10**(-2), 
            'A variavel Vv esta errada. O valor deveria ser Vv={}, mas é {}'
            .format(self.Vv, self.tp.Vv)) 

        def test_ymín(self):
            self.assertTrue( abs(self.tp.ymín - self.ymín) < 10**(-2), 
            'A variavel ymín esta errada. O valor deveria ser ymín={}, mas é {}'
            .format(self.ymín, self.tp.ymín)) 

        def test_ymáx(self):
            self.assertTrue( abs(self.tp.ymáx - self.ymáx) < 10**(-2), 
            'A variavel ymáx esta errada. O valor deveria ser ymáx={}, mas é {}'
            .format(self.ymáx, self.tp.ymáx))             

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível6(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            TP = factoryTratamentoPreliminar(args)
            self.tp = TP()
            self.tp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.tp

        def test_Deltah_limpa(self):
            self.assertTrue( abs(self.tp.Deltah_limpa - self.Deltah_limpa) < 10**(-3), 
            'A variavel Deltah_limpa esta errada. O valor deveria ser Deltah_limpa={}, mas é {}'
            .format(self.Deltah_limpa, self.tp.Deltah_limpa)) 

        def test_Deltah_50(self):
            self.assertTrue( abs(self.tp.Deltah_50 - self.Deltah_50) < 10**(-3), 
            'A variavel Deltah_50 esta errada. O valor deveria ser Deltah_50={}, mas é {}'
            .format(self.Deltah_50, self.tp.Deltah_50)) 

        def test_TESmáx(self):
            self.assertTrue( abs(self.tp.TESmáx - self.TESmáx) < 10**(-3), 
            'A variavel TESmáx esta errada. O valor deveria ser TESmáx={}, mas é {}'
            .format(self.TESmáx, self.tp.TESmáx)) 

        def test_A_P(self):
            self.assertTrue( abs(self.tp.A_P - self.A_P) < 10**(-3), 
            'A variavel A_P esta errada. O valor deveria ser A_P={}, mas é {}'
            .format(self.A_P, self.tp.A_P)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

def testsNível7(args, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            TP = factoryTratamentoPreliminar(args)
            self.tp = TP()
            self.tp.dimensionar()   

            d = dict(args, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.tp

        def test_H_AreiaAc(self):
            self.assertTrue( abs(self.tp.H_AreiaAc - self.H_AreiaAc) < 10**(-2), 
            'A variavel H_AreiaAc esta errada. O valor deveria ser H_AreiaAc={}, mas é {}'
            .format(self.H_AreiaAc, self.tp.H_AreiaAc)) 

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)



n1 = testsNível1(init_test1, results_test1)  
n2 = testsNível2(init_test1, results_test1)  
n3 = testsNível3(init_test1, results_test1)  
n4 = testsNível4(init_test1, results_test1)  
n5 = testsNível5(init_test1, results_test1) 
n6 = testsNível6(init_test1, results_test1) 
n7 = testsNível7(init_test1, results_test1)

exemploLivro = [n1, n2, n3, n4, n5, n6, n7]

alltests = unittest.TestSuite(exemploLivro)
result = unittest.TextTestRunner(verbosity=2).run(alltests)
        