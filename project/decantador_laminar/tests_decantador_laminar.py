import unittest
from decantador_laminar import DecantadorLaminar

from math import radians

class DecantadorLaminarTestsMethodos(unittest.TestCase):
	def test_fL(self):
		l=120
		w=6
		fL=DecantadorLaminar.fL(l,w)
		L=20
		self.assertTrue( abs(fL - L) < 10**(-5), "O método fL esta errado. O valor deveria ser: {}, mas é {}".format(L, fL))

	def test_fV0(self):
		L=20
		Vs=40
		theta=radians(60)
		Sc=1
		fV0PréDim=DecantadorLaminar.fV0PréDim(L, Vs, theta, Sc)
		V0=434.6
		self.assertTrue( abs(fV0PréDim - V0) < 10**(-1), "O método fV0PréDim esta errado. O valor deveria ser: {}, mas é {}".format(V0, fV0PréDim))

	def test_fAÚtil(self):
		QUnid=0.25
		V0=434.6
		fAÚtil=DecantadorLaminar.fAÚtil(QUnid, V0)
		AÚtil=49.7
		self.assertTrue( abs(fAÚtil - AÚtil) < 10**(-1), "O método fAÚtil esta errado. O valor deveria ser: {}, mas é {}".format(AÚtil, fAÚtil))
	
	def test_fASupÚTil(self):
		AÚtil=49.7
		theta=radians(60)
		fASupÚtil=DecantadorLaminar.fASupÚtil(AÚtil, theta)
		ASupÚtil=57.4
		self.assertTrue( abs(fASupÚtil - ASupÚtil) < 10**(-1), "O método ASupÚtil esta errado. O valor deveria ser: {}, mas é {}".format(ASupÚtil, fASupÚtil))

#	def test_fB(self):
#		ASupÚTil=57.4
#		LporB=3/2
#		fB=DecantadorLaminar.fB(ASupÚTil, LporB)
#		B=6.2
#		self.assertTrue( abs(fB - B) < 10**(-1), "O método ASupÚTil esta errado. O valor deveria ser: {}, mas é {}".format(B, fB))

	
"""
class DecantadorLaminarTestsResultados(unittest.TestCase):
	def setUp(self):
		Q=1
		Vs=40 
		l=1.2
		w=0.06 
		theta=60
		NUnidSed=4 
		LporB=3/2
		Sc=1
		nu=10**(-6)
		Lv=1.5
		Esp=0.005
		APoço=2.5
		NPoçosAdot=12
		LDec=10
		BDec=7.5

		self.dl=DecantadorLaminar(Q, Vs, l, w, theta, NUnidSed, LporB, Sc, nu, Lv, Esp,
		 APoço, NPoçosAdot, LDec, BDec)
		self.dl.dimensionar()

	def tearDown(self):
		del self.dl
	
	# Primeiro passo:
	def test_L(self):
		L=20
		dl_L=self.dl.L
		self.assertTrue( abs(dl_L - L) < 10**(-5), "O L esta errado. O valor deveria ser: {}, mas é {}".format(L, dl_L))

	def test_QUnid(self):
		QUnid=0.25
		dl_QUnid=self.dl.QUnid
		self.assertTrue( abs(dl_QUnid - QUnid) < 10**(-5), "O QUnid esta errado. O valor deveria ser: {}, mas é {}".format(QUnid, dl_QUnid))

	def test_V0(self):
		V0=434.6
		dl_V0PréDim=self.dl.V0PréDim
		self.assertTrue( abs(dl_V0PréDim - V0) < 10**(-1), "O V0PréDim esta errado. O valor deveria ser: {}, mas é {}".format(V0, dl_V0PréDim))

	def test_AÚtil(self):
		AÚtil=49.7
		dl_AÚtil=self.dl.AÚtil
		self.assertTrue( abs(dl_AÚtil - AÚtil) < 10**(-1), "O AÚtil esta errado. O valor deveria ser: {}, mas é {}".format(AÚtil, dl_AÚtil))

	def test_fASupÚTil(self):
		ASupÚTil=57.4
		dl_ASupÚTil=self.dl.ASupÚTil
		self.assertTrue( abs(dl_ASupÚTil - ASupÚTil) < 10**(-1), "O ASupÚTil esta errado. O valor deveria ser: {}, mas é {}".format(ASupÚTil, dl_ASupÚTil))

	def test_fB(self):
		B=6.2
		dl_B=self.dl.B
		self.assertTrue( abs(dl_B - B) < 10**(-1), "O B esta errado. O valor deveria ser: {}, mas é {}".format(B, dl_B))

	def test_fLÚtil(self):
		LÚtil=7.65
		dl_LÚtil=self.dl.LÚtil
		self.assertTrue( abs(dl_LÚtil - LÚtil) < 10**(0), "O LÚtil esta errado. O valor deveria ser: {}, mas é {}".format(LÚtil, dl_LÚtil))

	def test_fNe(self):
		Ne=127.5
		dl_Ne=self.dl.Ne
		self.assertTrue( abs(dl_Ne - Ne) < 10**(1), "O Ne esta errado. O valor deveria ser: {}, mas é {}".format(Ne, dl_Ne))

	# TO DO: Modificar a precisão desse teste. Por conta doa erros de arredondamento o valor da muito diferente.
	def test_fNeArred(self):
		NeArred=128
		dl_NeArred=self.dl.NeArred
		self.assertTrue( abs(dl_NeArred - NeArred) < 10**(1), "O NeArred esta errado. O valor deveria ser: {}, mas é {}".format(NeArred, dl_NeArred))

	def test_fNPlac(self):
		NPlac=129
		dl_NPlac=self.dl.NPlac
		self.assertTrue( abs(dl_NPlac - NPlac) < 10**(1), "O NPlac esta errado. O valor deveria ser: {}, mas é {}".format(NPlac, dl_NPlac))

## Teste obsoleto
#	def test_fLp(self):
#		Lp=8.325
#		dl_Lp=self.dl.Lp
#		self.assertTrue( abs(dl_Lp - Lp) < 10**(-0.1), "O Lp esta errado. O valor deveria ser: {}, mas é {}".format(Lp, dl_Lp))

	def test_fLargDec(self):
		LargDec=10.21
		dl_LargDec=self.dl.LargDec
		self.assertTrue( abs(dl_LargDec - LargDec) < 10**(-0.3), "O LargDec esta errado. O valor deveria ser: {}, mas é {}".format(LargDec, dl_LargDec))
"""

class DecantadorLaminarTestsOtimizaçãoOrdem_ETA_USP(unittest.TestCase):
	def setUp(self):
		Q=1
		Vs=40 
		l=1.2
		w=0.06 
		theta=60
		NUnidSed=4 
		Sc=1
		nu=10**(-6)
		ql=1.5
		Esp=0.005
		APoço=2.5**2
		NPoçosAdot=12
		LDec=10
		BDec=7.5
		arred=0.5

		self.dl=DecantadorLaminar(Q, Vs, l, w, theta, NUnidSed, Sc, nu, ql, Esp,
		 APoço, NPoçosAdot, LDec, BDec, arred)
		
		self.dl.pré_dimensionar()

		self.dl.dimensionar()

	def tearDown(self):
		del self.dl
	
	# Primeiro passo:
	def test_L(self):
		L=20
		dl_L=self.dl.L
		self.assertTrue( abs(dl_L - L) < 10**(-5), "O L esta errado. O valor deveria ser: {}, mas é {}".format(L, dl_L))

	def test_QUnid(self):
		QUnid=0.25
		dl_QUnid=self.dl.QUnid
		self.assertTrue( abs(dl_QUnid - QUnid) < 10**(-5), "O QUnid esta errado. O valor deveria ser: {}, mas é {}".format(QUnid, dl_QUnid))

	def test_V0(self):
		V0PréDim=434.6
		dl_V0PréDim=self.dl.V0PréDim
		self.assertTrue( abs(dl_V0PréDim - V0PréDim) < 10**(-1), "O V0PréDim esta erra do. O valor deveria ser: {}, mas é {}".format(V0PréDim, dl_V0PréDim))

	def test_AÚtil(self):
		AÚtil=49.7
		dl_AÚtil=self.dl.AÚtil
		self.assertTrue( abs(dl_AÚtil - AÚtil) < 10**(-1), "O AÚtil esta errado. O valor deveria ser: {}, mas é {}".format(AÚtil, dl_AÚtil))

	def test_fASupÚtil(self):
		ASupÚtil=57.4
		dl_ASupÚtil=self.dl.ASupÚtil
		self.assertTrue( abs(dl_ASupÚtil - ASupÚtil) < 10**(-1), "O ASupÚtil esta errado. O valor deveria ser: {}, mas é {}".format(ASupÚtil, dl_ASupÚtil))

	def test_fNPoços(self):
		NPoços=10.6
		dl_NPoços=self.dl.NPoços
		self.assertTrue( abs(dl_NPoços - NPoços) < 10**(0.3), "O NPoços esta errado. O valor deveria ser: {}, mas é {}".format(NPoços, dl_NPoços))

	def test_fLd(self):
		Ld=9.4
		dl_Ld=self.dl.Ld
		self.assertTrue( abs(dl_Ld - Ld) < 10**(-2), "O Ld esta errado. O valor deveria ser: {}, mas é {}".format(Ld, dl_Ld))

	def test_fLp(self):
		Lp=8.14
		dl_Lp=self.dl.Lp
		self.assertTrue( abs(dl_Lp - Lp) < 10**(-2), "O Lp esta errado. O valor deveria ser: {}, mas é {}".format(Lp, dl_Lp))

	def test_fNe(self):
		Ne=125.2
		dl_Ne=self.dl.Ne
		self.assertTrue( abs(dl_Ne - Ne) < 10**(-0.5), "O Lp esta errado. O valor deveria ser: {}, mas é {}".format(Ne, dl_Ne))

	def test_fNeArred(self):
		NeArred=126
		dl_NeArred=self.dl.NeArred
		self.assertTrue( abs(dl_NeArred - NeArred) < 10**(-0.5), "O NeArred esta errado. O valor deveria ser: {}, mas é {}".format(NeArred, dl_NeArred))

	def test_fNPlac(self):
		NPlac=127
		dl_NPlac=self.dl.NPlac
		self.assertTrue( abs(dl_NPlac - NPlac) < 10**(-0.5), "O NPlac esta errado. O valor deveria ser: {}, mas é {}".format(NPlac, dl_NPlac))

	def test_fV0(self):
		V0=0.441
		dl_V0=self.dl.V0
		self.assertTrue( abs(dl_V0 - V0) < 10**(-2), "O V0 esta errado. O valor deveria ser: {}, mas é {}".format(V0, dl_V0))

	def test_fVsProjeto(self):
		VsProjeto=0.041 # em cm/s
		VsProjeto=35.06 # m/dia
		dl_VsProjeto=self.dl.VsProjeto
		self.assertTrue( abs(dl_VsProjeto - VsProjeto) < 10**(-2), "O VsProjeto esta errado. O valor deveria ser: {}, mas é {}".format(VsProjeto, dl_VsProjeto))

	def test_fqv(self):
		qv=288
		dl_qv=self.dl.qv
		self.assertTrue( abs(dl_qv - qv) < 10**(-2), "O qv esta errado. O valor deveria ser: {}, mas é {}".format(qv, dl_qv))

	def test_fDh(self):
		Dh=0.12
		dl_Dh=self.dl.Dh
		self.assertTrue( abs(dl_Dh - Dh) < 10**(-2), "O Dh esta errado. O valor deveria ser: {}, mas é {}".format(Dh, dl_Dh))

	def test_fRe(self):
		Re=525
		dl_Re=self.dl.Re
		self.assertTrue( abs(dl_Re - Re) < 10**(0.2), "O Re esta errado. O valor deveria ser: {}, mas é {}".format(Re, dl_Re))

	def test_fLv(self):
		Lv=166.7
		dl_Lv=self.dl.Lv
		self.assertTrue( abs(dl_Lv - Lv) < 10**(-1), "O Lv esta errado. O valor deveria ser: {}, mas é {}".format(Lv, dl_Lv))

	def test_fNCalha(self):
		NCalha=8.3
		dl_NCalha=self.dl.NCalha
		self.assertTrue( abs(dl_NCalha - NCalha) < 10**(-1), "O NCalha esta errado. O valor deveria ser: {}, mas é {}".format(NCalha, dl_NCalha))

	def test_fNCalhaAdot(self):
		NCalhaAdot=8
		dl_NCalhaAdot=self.dl.NCalhaAdot
		self.assertTrue( abs(dl_NCalhaAdot - NCalhaAdot) < 10**(-2), "O NCalhaAdot esta errado. O valor deveria ser: {}, mas é {}".format(NCalhaAdot, dl_NCalhaAdot))

	def test_fLvProjeto(self):
		LvProjeto=160
		dl_LvProjeto=self.dl.LvProjeto
		self.assertTrue( abs(dl_LvProjeto - LvProjeto) < 10**(-2), "O LvProjeto esta errado. O valor deveria ser: {}, mas é {}".format(LvProjeto, dl_LvProjeto))

	def test_fqlProjeto(self):
		qlProjeto=1.56
		dl_qlProjeto=self.dl.qlProjeto
		self.assertTrue( abs(dl_qlProjeto - qlProjeto) < 10**(-2), "O qlProjeto esta errado. O valor deveria ser: {}, mas é {}".format(qlProjeto, dl_qlProjeto))
	def test_fEspCalhas(self):
		EspCalhas=0.94
		dl_EspCalhas=self.dl.EspCalhas
		self.assertTrue( abs(dl_EspCalhas - EspCalhas) < 10**(-2), "O EspCalhas esta errado. O valor deveria ser: {}, mas é {}".format(EspCalhas, dl_EspCalhas))


class DecantadorLaminarTestsOtimizaçãoOrdem_Lucas(unittest.TestCase):
	def setUp(self):
		Q=0.02343
		Vs=40
		l=1.2
		w=0.06 
		theta=60
		NUnidSed=2
		LporB=3/2		# Será eliminada...
		Sc=1
		nu=10**(-6)
		ql=1.5
		Esp=0.005
		APoço=1.2**2

		NPoçosAdot=3
		LDec=3.6
		BDec=1.2
		arred=0.01

		self.dl=DecantadorLaminar(Q, Vs, l, w, theta, NUnidSed, Sc, nu, ql, Esp,
		 APoço, NPoçosAdot, LDec, BDec, arred)

		self.dl.dimensionar()

	def tearDown(self):
		del self.dl
	
	# Primeiro passo:
	def test_L(self):
		L=20
		dl_L=self.dl.L
		self.assertTrue( abs(dl_L - L) < 10**(-5), "O L esta errado. O valor deveria ser: {}, mas é {}".format(L, dl_L))

	def test_QUnid(self):
		QUnid=0.011715
		dl_QUnid=self.dl.QUnid
		self.assertTrue( abs(dl_QUnid - QUnid) < 10**(-5), "O QUnid esta errado. O valor deveria ser: {}, mas é {}".format(QUnid, dl_QUnid))

	def test_V0(self):
		V0PréDim=434.64
		dl_V0PréDim=self.dl.V0PréDim
		self.assertTrue( abs(dl_V0PréDim - V0PréDim) < 10**(-1), "O V0PréDim esta erra do. O valor deveria ser: {}, mas é {}".format(V0PréDim, dl_V0PréDim))

	def test_AÚtil(self):
		AÚtil=2.33
		dl_AÚtil=self.dl.AÚtil
		self.assertTrue( abs(dl_AÚtil - AÚtil) < 10**(-1), "O AÚtil esta errado. O valor deveria ser: {}, mas é {}".format(AÚtil, dl_AÚtil))

	def test_fASupÚtil(self):
		ASupÚtil=2.7
		dl_ASupÚtil=self.dl.ASupÚtil
		self.assertTrue( abs(dl_ASupÚtil - ASupÚtil) < 10**(-1), "O ASupÚtil esta errado. O valor deveria ser: {}, mas é {}".format(ASupÚtil, dl_ASupÚtil))

	def test_fNPoços(self):
		NPoços=3
		dl_NPoços=self.dl.NPoços
		self.assertTrue( abs(dl_NPoços - NPoços) < 10**(0.3), "O NPoços esta errado. O valor deveria ser: {}, mas é {}".format(NPoços, dl_NPoços))

	def test_fLd(self):
		Ld=3
		dl_Ld=self.dl.Ld
		self.assertTrue( abs(dl_Ld - Ld) < 10**(-2), "O Ld esta errado. O valor deveria ser: {}, mas é {}".format(Ld, dl_Ld))

	def test_fLp(self):
		Lp=2.6
		dl_Lp=self.dl.Lp
		self.assertTrue( abs(dl_Lp - Lp) < 10**(-2), "O Lp esta errado. O valor deveria ser: {}, mas é {}".format(Lp, dl_Lp))

	def test_fNe(self):
		Ne=42.6		# O valor calculado por Lucas esta errado
		dl_Ne=self.dl.Ne
		self.assertTrue( abs(dl_Ne - Ne) < 10**(0.5), "O Lp esta errado. O valor deveria ser: {}, mas é {}".format(Ne, dl_Ne))

	def test_fNeArred(self):
		NeArred=43
		dl_NeArred=self.dl.NeArred
		self.assertTrue( abs(dl_NeArred - NeArred) < 10**(0.5), "O NeArred esta errado. O valor deveria ser: {}, mas é {}".format(NeArred, dl_NeArred))

	def test_fNPlac(self):
		NPlac=44
		dl_NPlac=self.dl.NPlac
		self.assertTrue( abs(dl_NPlac - NPlac) < 10**(0.5), "O NPlac esta errado. O valor deveria ser: {}, mas é {}".format(NPlac, dl_NPlac))

	def test_fV0(self):
		V0=0.378
		dl_V0=self.dl.V0
		self.assertTrue( abs(dl_V0 - V0) < 10**(-1), "O V0 esta errado. O valor deveria ser: {}, mas é {}".format(V0, dl_V0))

	def test_fVsProjeto(self):
		VsProjeto=30.24 # m/dia
		dl_VsProjeto=self.dl.VsProjeto
		self.assertTrue( abs(dl_VsProjeto - VsProjeto) < 10**(0.2), "O VsProjeto esta errado. O valor deveria ser: {}, mas é {}".format(VsProjeto, dl_VsProjeto))

	def test_fqv(self):
		qv=234.3
		dl_qv=self.dl.qv
		self.assertTrue( abs(dl_qv - qv) < 10**(-2), "O qv esta errado. O valor deveria ser: {}, mas é {}".format(qv, dl_qv))

	def test_fDh(self):
		Dh=0.114
		dl_Dh=self.dl.Dh
		self.assertTrue( abs(dl_Dh - Dh) < 10**(-2), "O Dh esta errado. O valor deveria ser: {}, mas é {}".format(Dh, dl_Dh))

	def test_fRe(self):
		Re=431
		dl_Re=self.dl.Re
		self.assertTrue( abs(dl_Re - Re) < 10**(1.5), "O Re esta errado. O valor deveria ser: {}, mas é {}".format(Re, dl_Re))

	def test_fLv(self):
		Lv=7.81
		dl_Lv=self.dl.Lv
		self.assertTrue( abs(dl_Lv - Lv) < 10**(-1), "O Lv esta errado. O valor deveria ser: {}, mas é {}".format(Lv, dl_Lv))

	def test_fNCalha(self):
		NCalha=1.08
		dl_NCalha=self.dl.NCalha
		self.assertTrue( abs(dl_NCalha - NCalha) < 10**(-1), "O NCalha esta errado. O valor deveria ser: {}, mas é {}".format(NCalha, dl_NCalha))

	def test_fNCalhaAdot(self):
		NCalhaAdot=2
		dl_NCalhaAdot=self.dl.NCalhaAdot
		self.assertTrue( abs(dl_NCalhaAdot - NCalhaAdot) < 10**(-2), "O NCalhaAdot esta errado. O valor deveria ser: {}, mas é {}".format(NCalhaAdot, dl_NCalhaAdot))

	def test_fLvProjeto(self):
		LvProjeto=14.4
		dl_LvProjeto=self.dl.LvProjeto
		self.assertTrue( abs(dl_LvProjeto - LvProjeto) < 10**(-2), "O LvProjeto esta errado. O valor deveria ser: {}, mas é {}".format(LvProjeto, dl_LvProjeto))

	def test_fqlProjeto(self):
		qlProjeto=0.813
		dl_qlProjeto=self.dl.qlProjeto
		self.assertTrue( abs(dl_qlProjeto - qlProjeto) < 10**(-2), "O qlProjeto esta errado. O valor deveria ser: {}, mas é {}".format(qlProjeto, dl_qlProjeto))
	
	def test_fEspCalhas(self):
		EspCalhas=0.6
		dl_EspCalhas=self.dl.EspCalhas
		self.assertTrue( abs(dl_EspCalhas - EspCalhas) < 10**(-2), "O EspCalhas esta errado. O valor deveria ser: {}, mas é {}".format(EspCalhas, dl_EspCalhas))




suite1 = unittest.TestLoader().loadTestsFromTestCase(DecantadorLaminarTestsMethodos)
#suite2 = unittest.TestLoader().loadTestsFromTestCase(DecantadorLaminarTestsResultados)

suite3 = unittest.TestLoader().loadTestsFromTestCase(DecantadorLaminarTestsOtimizaçãoOrdem_ETA_USP)
suite4 = unittest.TestLoader().loadTestsFromTestCase(DecantadorLaminarTestsOtimizaçãoOrdem_Lucas)
#alltests = unittest.TestSuite([suite1])
#alltests = unittest.TestSuite([suite2])
#alltests = unittest.TestSuite([suite1, suite2])

alltests = unittest.TestSuite([suite1, suite3, suite4])

#alltests = unittest.TestSuite([suite4])

result = unittest.TextTestRunner(verbosity=2).run(alltests)


Q=1
Vs=40 
l=1.2
w=0.06 
theta=60
NUnidSed=4 
Sc=1
nu=10**(-6)
ql=1.5
Esp=0.005
APoço=2.5**2
NPoçosAdot=12
LDec=10
BDec=7.5
arred=0.5

dl=DecantadorLaminar(Q, Vs, l, w, theta, NUnidSed, Sc, nu, ql, Esp,
APoço, NPoçosAdot, LDec, BDec, arred)

#dl.pré_dimensionar()

dl.dimensionar()
print("ced", dl.out)

print("cedfdczvsdz")