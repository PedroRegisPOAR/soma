from math import sin, cos, radians

class DecantadorLaminar():
	__slots__ = ("Q", "Vs", "l", "w", "theta", "NUnid",
		"Sc", "nu", "ql", "Esp", "APoço", "NPoçosAdot",
		"LDec", "BDec", "arred", 

		"out", "L", "QUnid", "V0PréDim", "AÚtil",  "ASupÚtil", 
		"Ne", "NPlac", "Lp", "NeArred", "NPoços", "Ld", "theta_degrees",
		"V0", "VsProjeto", "qv", "Dh", "Re", "Lv", "NCalha", 
		"NCalhaAdot", "qlProjeto", "LvProjeto", "EspCalhas")

	def __init__(self, Q, Vs, l, w, theta, NUnid, Sc, nu, ql,
	Esp, APoço, NPoçosAdot, LDec, BDec, arred):

		self.Q=Q
		self.Vs=Vs
		self.l=l
		self.w=w
		self.NUnid=NUnid
		self.theta_degrees=theta
#		self.theta_degrees=round(self.theta_degrees,0)
		self.theta=radians(theta)
		self.Sc=Sc
		self.nu=nu
		self.ql=ql
		self.Esp=Esp
		self.APoço=APoço
		self.NPoçosAdot=NPoçosAdot
		self.LDec=LDec
		self.BDec=BDec
		self.arred=arred

		self.L=None
		self.QUnid=None
		self.AÚtil=None
		self.ASupÚtil=None
		self.Ne=None
		self.NPlac=None
		self.Lp=None
		self.NeArred=None
		self.NPoços=None
		self.Ld=None
		self.V0PréDim=None
		self.V0=None
		self.VsProjeto=None
		self.Lv=None
		self.NCalha=None
		self.NCalhaAdot=None
		self.qlProjeto=None
		self.LvProjeto=None
		self.EspCalhas=None
		self.Dh=None
		self.Re=None
		self.qv=None
		self.out=None


	@classmethod
	def fL(self, l, w):
		assert l>0, "O método fL recebeu l negativo."
		assert w>0, "O método fL recebeu w negativo."
		return l/w

	@classmethod
	def fQUnid(self, Q, NUnid):
		assert Q>0, "O método fQUnid recebeu Q negativo."
		assert NUnid>0, "O método fQUnid recebeu NUnid negativo."
		return Q/NUnid

	@classmethod
	def fV0PréDim(self, L, Vs, theta, Sc):
		assert L>0, "O método fV0 recebeu L negativo."
		assert Vs>0, "O método fV0 recebeu Vs negativo."
		return Vs*(L*cos(theta) + sin(theta))/Sc

	@classmethod
	def fAÚtil(self, QUnid, V0):
		assert QUnid>0, "O método fAÚtil recebeu QUnid negativo."
		assert V0>0, "O método fAÚtil recebeu V0 negativo."
		return 86400*QUnid/V0 

	@classmethod
	def fASupÚtil(self, AÚtil, theta):
		assert AÚtil>0, "O método fASupÚTil recebeu AÚTil negativo."
		assert theta>0, "O método fASupÚTil recebeu theta negativo."
		return AÚtil/sin(theta)

	@classmethod
	def fNPoços(self, ASupÚTil, APoço):		
		return ASupÚTil/APoço

	@classmethod
	def fLd(self, LDec, l, theta):		
		return LDec - l*cos(theta)

	@classmethod
	def fLp(self, Ld, theta): 
		return  Ld*sin(theta)

	@classmethod
	def fNe(self, Lp, Esp, w):
		num=Lp + Esp
		den=w + Esp
		return num/den

	@classmethod
	def fNeArred(self, Ne):
		if abs(int(Ne)- Ne)<10**(-2):
			return  int(Ne)
		else:
			return  int(Ne) + 1

	@classmethod
	def fNPlac(self, NeArred): 
		"""NeArred"""
		return  NeArred + 1

	@classmethod
	def fV0(self, QUnid, NeArred, BDec, w):
		return 100*QUnid/(NeArred*BDec*w)

	@classmethod
	def fVs(self, V0, Sc, L, theta):
		num=V0*Sc
		den=L*cos(theta) + sin(theta)
		#convertendo para m/dia
		r=(num/den)*(86400/100)
		return r

	def fqv(self, QUnid, LDec, BDec):
		"""QUnid, ASupÚtil"""
		return 86400*QUnid/(LDec*BDec)

	@classmethod
	def fDh(self, B, h):		
		""" B, h 
			
			Esse h é o w
		"""
		num=4*B*h
		den=2*(B + h)
		return  num/den

	# Esse Vh é o V0 ...	
	@classmethod
	def fRe(self, Vh, Dh, nu):		
		return  (Vh*Dh)/(100*nu)

	@classmethod
	def fLv(self, QUnid, ql):		
		return  1000*QUnid/ql

	@classmethod
	def fNCalha(self, Lv, LCalha):		
		return  Lv/(2*LCalha)

	@classmethod
	def fNCalhaAdot(self, NCalha, arred):
		if NCalha - int(NCalha)<arred:
			return int(NCalha)
		else:
			return int(NCalha) + 1

	@classmethod
	def fLvProjeto(self, NCalhaAdot, LDec):		
		return  2*NCalhaAdot*LDec

	@classmethod
	def fqlProjeto(self, QUnid, LvProjeto):		
		return  1000*QUnid/LvProjeto

	@classmethod
	def fEspCalhas(self, BDec, NCalhaAdot):		
		return  BDec/NCalhaAdot

	def make_out(self):
		d=dict((name, getattr(self, name)) for name in dir(self) 
        if not name.startswith('__') and 
        not callable(getattr(self,name)) and 
        type(getattr(self,name))==float) 
#		print(d)
		self.out=d

	def arredondamento(self):
		for key in self.out:
			if type(self.out[key]) == float:
				self.out[key]=round(self.out[key],4)

	def pré_dimensionar(self):
		self.L=self.fL(self.l, self.w)
		self.QUnid=self.fQUnid(self.Q, self.NUnid)
		self.V0PréDim=self.fV0PréDim(self.L, self.Vs, self.theta, self.Sc)
		self.AÚtil=self.fAÚtil(self.QUnid, self.V0PréDim)
		self.ASupÚtil=self.fASupÚtil(self.AÚtil, self.theta)
		self.NPoços=self.fNPoços(self.ASupÚtil, self.APoço)

		self.make_out()
		self.arredondamento()

	def dimensionar(self):

		self.pré_dimensionar()

		self.Ld=self.fLd(self.LDec, self.l, self.theta)		
		self.Lp=self.fLp(self.Ld, self.theta)
		self.Ne=self.fNe(self.Lp,self.Esp,self.w)
		self.NeArred=self.fNeArred(self.Ne)
		self.NPlac=self.fNPlac(self.NeArred)
		self.V0=self.fV0(self.QUnid, self.NeArred, self.BDec, self.w)
		self.VsProjeto=self.fVs(self.V0, self.Sc, self.L, self.theta)
		self.qv=self.fqv(self.QUnid, self.LDec, self.BDec)
		self.Dh=self.fDh(self.BDec, self.w)
		self.Re=self.fRe(self.V0, self.Dh, self.nu)		
		self.Lv=self.fLv(self.QUnid, self.ql)
		self.NCalha=self.fNCalha(self.Lv, self.LDec)
		self.NCalhaAdot=self.fNCalhaAdot(self.NCalha,self.arred)
		self.LvProjeto=self.fLvProjeto(self.NCalhaAdot, self.LDec)				
		self.qlProjeto=self.fqlProjeto(self.QUnid, self.LvProjeto)
		self.EspCalhas=self.fEspCalhas(self.BDec, self.NCalhaAdot)
		
		self.make_out()
		self.arredondamento()

"""

	@classmethod
	def fB(self, ASupÚTil, LporB):
		assert ASupÚTil>0, "O método fB recebeu ASupÚTil negativo."
		assert LporB>0, "O método fB recebeu LporB negativo."
		return (ASupÚTil/LporB)**(1/2)
	
	@classmethod
	def fLÚtil(self, AÚTil, B):
		return  AÚTil/B

#	@classmethod
#	def fLp(self, NEspArred, w, NPlac, Esp): 
#		return  NEspArred*w + NPlac*Esp

	@classmethod
	def fLargDec(self, l, theta, Lp):
		return  l*cos(theta) + Lp/sin(theta)

	@classmethod
	def fAd(self, Lpoço, Bpoço):
		return  Lpoço*Bpoço

	@classmethod
	def fqv(self, QUnid, A):
		return  QUnid/A
	  		
	@classmethod
	def fAPoço(self, Lpoço):		
		return  Lpoço*Lpoço # Verificar!

#	@classmethod
#	def fNPoços(self, b, L, APoço):		
#		return  B*L/APoço 

	@classmethod
	def fLl(self, QUnid, ql):		
		return   QUnid/ql



	def dimensionar(self):
		# Passo: 1
		self.L=self.fL(self.l, self.w)
		self.QUnid=self.fQUnid(self.Q, self.NUnid)

		# Passo: 2
		self.V0=self.fV0(self.L, self.Vs, self.theta, self.Sc)

		# Passo: 3
		self.AÚtil=self.fAÚtil(self.QUnid, self.V0)
		
		# Passo: 4
		self.ASupÚTil=self.fASupÚTil(self.AÚtil, self.theta)

		# Passo: 5
		self.B=self.fB(self.ASupÚTil, self.LporB)

		self.LÚtil=self.fLÚtil(self.AÚtil, self.B)
		self.Ne=self.fNe(self.LÚtil, self.w)
		self.NeArred=self.fNeArred(self.Ne)
		self.NPlac=self.fNPlac(self.NeArred)
		self.Lp=self.fLp(self.NeArred, self.w, self.NPlac, self.Esp)	
		self.LargDec=self.fLargDec(self.l, self.theta, self.Lp)
"""