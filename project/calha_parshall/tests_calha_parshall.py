import unittest
import calha_parshall


#######
#######
#W=2440/1000
Q=90/1000
g=9.807
T=17.5
GmMáx=2000
GmMín=1000
FMín=5
#rho=998.68
#mu=0.001071                  
#######
       
cp=calha_parshall.CalhaParshall(Q, g, T, GmMín, GmMáx, FMín)
cp.dimensiona_inteligente()

#######
# Esses valores que são usados nos testes são baseados no exemplo do livro
# do Richter.
#######
mu=0.001065
rho=998.68
H0=0.363
D0=3.08
U0=1.073
q=0.492
E0=0.651
U1=3.108
h1=0.158
F1=2.5
h3=0.331
U3=1.318
L=1.962
h=0.113
Tm=0.89
Gm=1078
#######

class TestCalhaParshall(unittest.TestCase):
    pass

    # TO DO. Usar a função abs nos testes, e format.
#    def test_W(self):
#        self.assertTrue(cp.W==W, "A variavel de entrada W esta errada.")
"""       
    def test_Q(self):
        self.assertTrue(cp.Q==Q, "A variavel de entrada Q esta errada.")        

    def test_g(self):
        self.assertTrue(cp.g==g, "A variavel de entrada g esta errada.")                

    def test_rho(self):
        self.assertTrue((cp.rho - rho)**2 < 10**(-2), "A variavel de entrada rho esta errada.")
            
    def test_mu(self):
        self.assertTrue( (cp.mu - mu)**2 < 10**(-2), "A variavel de entrada mu esta errada.")

    def test_fH0(self):
        self.assertTrue((cp.H0 - H0)**2 < 10**(-5), "A variavel H0 esta errada.")

    def test_fD0(self):
        self.assertTrue((cp.D0 - D0)**2 < 10**(-5), "A variavel D0 esta errada.")
    def test_fU0(self):
        self.assertTrue((cp.U0 - U0)**2 < 10**(-5), "A variavel U0 esta errada.")

    def test_fq(self):
        self.assertTrue((cp.q - q)**2 < 10**(-5), "A variavel q esta errada.")

    def test_fE0(self):
        self.assertTrue((cp.E0 - E0)**2 < 10**(-5), "A variavel E0 esta errada.")

    def test_fU1(self):
        self.assertTrue((cp.U1 - U1)**2 < 10**(-5), "A variavel U1 esta errada.")

    def test_fh1(self):
        self.assertTrue((cp.h1 - h1)**2 < 10**(-5), "A variavel h1 esta errada.")

    def test_Froud(self):
        self.assertTrue((cp.F1 - F1)**2 < 10**(-2), "A variavel F1 esta errada.")

    def test_fh3(self):
        self.assertTrue((cp.h3 - h3)**2 < 10**(-5), "A variavel h3 esta errada.")

    def test_fU3(self):
        self.assertTrue((cp.U3 - U3)**2 < 10**(-5), "A variavel U3 esta errada.")

    def test_fL(self):
        self.assertTrue((cp.L - L)**2 < 10**(-5), "A variavel L esta errada.")

    def test_fh(self):
        self.assertTrue((cp.h - h)**2 < 10**(-5), "A variavel h esta errada.O valor deveria ser h={}, mas é {}".format(cp.h, h))
        
    def test_fTm(self):
        self.assertTrue((cp.Tm - Tm)**2 < 10**(-2), "A variavel Tm esta errada. O valor deveria ser Tm={}, mas é {}".format(cp.Tm, Tm))

    def test_fGm(self):
        self.assertTrue( abs(cp.Gm - Gm) < 10**(1), "A variavel Gm esta errada. O valor deveria ser Gm={}, mas é {}".format(cp.Gm, Gm))
"""
        
        

if __name__ == '__main__':
    unittest.main()







