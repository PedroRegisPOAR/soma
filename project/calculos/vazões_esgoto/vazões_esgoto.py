
veinit = {	
		'CR': None,
		'r':None,
		'K1':None,
		'K2':None,
		'K3':None,
		'TInf':None, # Taxa de infiltração
		'QPC':None, # Vazão percapita 
		't3':None,
		't4':None,
		't5':None,
		'P3':None,
		'P4':None,
		'P5':None,
	}


global veresults
veresults = {
		'Km': None,
	    'Lt3': None,		
	    'Lt4': None,		
	    'Lt5': None,		
	    'QInft3': None,		
	    'QInft4': None,	
	    'QInft5': None,	
	    'QMínt3': None,
	    'QMínt4': None,
	    'QMínt5': None,
	    'QMédt3': None,	
	    'QMédt4': None,	
	    'QMédt5': None,	
	    'QMáxt3': None,	
	    'QMáxt4': None,	
	    'QMáxt5': None,	
        'out':None,
	}


class VE_Methods():
	__slots__ = ()

	@classmethod
	def fL(self, r, P):
		return r*P

	@classmethod
	def fQInf(self, TInf, L):
		return TInf*L/1000
	
	@classmethod
	def fKm(self, K2, K3):
		return (K2 + K3)/2

	@classmethod
	def fQMín(self, CR, K3, QPC, P, QInf):
		return (CR*K3*QPC*P)/86400 + QInf
	
	@classmethod
	def fQMéd(self, CR, Km, QPC, P, QInf):
		return (CR*Km*QPC*P)/86400 + QInf
	
	@classmethod
	def fQMáx(self, K1, K2, QMéd):
		return K1*K2*QMéd

class VE_Parte1():
	__slots__ = ()

	@classmethod
	def fKmédio(self, K2, K3):
		self.Km = self.fKm(K2, K3)
		return self.Km
	
	@classmethod
	def comprimentos(self, r, P3, P4, P5):
		self.Lt3 = self.fL(r, P3)
		self.Lt4 = self.fL(r, P4)
		self.Lt5 = self.fL(r, P5)
		return self.Lt3, self.Lt4, self.Lt5
	
	@classmethod
	def vazõesInfiltração(self, TInf, Lt3, Lt4, Lt5):
		self.QInft3 = self.fQInf(TInf, Lt3)
		self.QInft4 = self.fQInf(TInf, Lt4)
		self.QInft5 = self.fQInf(TInf, Lt5)
		return self.QInft3, self.QInft4, self.QInft5
	
	@classmethod
	def vazõesMínimas(self, CR, K3, QPC, P3, P4, P5, QInft3,
						QInft4, QInft5):

		self.QMínt3	= self.fQMín(CR, K3, QPC, P3, QInft3)
		self.QMínt4	= self.fQMín(CR, K3, QPC, P4, QInft4)
		self.QMínt5	= self.fQMín(CR, K3, QPC, P5, QInft5)

		return self.QMínt3, self.QMínt4, self.QMínt5

	@classmethod
	def vazõesMédias(self, CR, Km, QPC, P3, P4, P5, QInft3,
						QInft4, QInft5):

		self.QMédt3	= self.fQMéd(CR, Km, QPC, P3, QInft3)
		self.QMédt4	= self.fQMéd(CR, Km, QPC, P4, QInft4)
		self.QMédt5	= self.fQMéd(CR, Km, QPC, P5, QInft5)		

		return self.QMédt3, self.QMédt4, self.QMédt5

	@classmethod
	def vazõesMáximas(self, K1, K2, QMédt3, QMédt4, QMédt5):
		self.QMáxt3 = self.fQMáx(K1, K2, QMédt3)
		self.QMáxt4 = self.fQMáx(K1, K2, QMédt4)
		self.QMáxt5 = self.fQMáx(K1, K2, QMédt5)
		return self.QMáxt3, self.QMáxt4, self.QMáxt5

class VE_Parte2():
	__slots__ = ()

	def n1(self):
		self.fKmédio(self.K2, self.K3)
		self.comprimentos(self.r, self.P3, self.P4, self.P5)

	def n2(self):
		self.vazõesInfiltração(self.TInf, self.Lt3, self.Lt4, self.Lt5)

	def n3(self):
		self.vazõesMínimas(self.CR, self.K3, self.QPC, self.P3, self.P4, self.P5,
								self.QInft3, self.QInft4, self.QInft5)

		self.vazõesMédias(self.CR, self.Km, self.QPC, self.P3, self.P4, self.P5,
							self.QInft3, self.QInft4, self.QInft5)

	def n4(self):
		self.vazõesMáximas(self.K1, self.K2, self.QMédt3, self.QMédt4, self.QMédt5)

		

class VE_Main():
	__slots__ = ()

	def calcular(self):
		self.n1()
		self.n2()
		self.n3()
		self.n4()
		self.make_out()
		self.arredondamento()

class Extras():
	__slots__=()

	def make_out(self):
		d = dict((name, getattr(self, name)) for name in dir(self) 
		if not name.startswith('__') and 
		not callable(getattr(self, name))) 
		self.out = d

	def arredondamento(self):
		key_integers = ['P3', 'P4', 'P5', 't3', 't4', 't5']
		for key in self.out:
			if type(self.out[key]) == float:
				if key in key_integers:
					self.out[key] = int(self.out[key])
				else: 
					self.out[key] = round(self.out[key], 2)


def factory_VE(veinit):
	global veresults

	d = dict(veinit, **veresults)

	class VE(VE_Methods, VE_Parte1, VE_Parte2,
				VE_Main,Extras):
	    __slots__ = [key for key in d]
	    def __init__(self):
	        for key in d:
	            setattr(self, key, d[key])
	return VE


