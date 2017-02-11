
vainit = {	
		'QPC': None,
		'K1': None,
		'K2': None,
		't3': None,
		't4': None,
		't5': None,
		'P3': None,
		'P4': None,
		'P5': None,
	}


global varesults
varesults = {
	    'QMín': None,
	    'QMéd': None,	
	    'QMáx': None,	
        'out':None,
	}


class VA_Methods():
	__slots__ = ()

	def fQ(self, K1, K2, QPC, P):
		return (K1*K2*QPC*P)/86400


class VA_Parte1():
	__slots__ = ()

	def vazões(self):
		self.QMín = self.fQ(self.K1, self.K2, self.QPC, self.P3)
		self.QMéd = self.fQ(self.K1, self.K2, self.QPC, self.P4)
		self.QMáx = self.fQ(self.K1, self.K2, self.QPC, self.P5)

class VA_Main():
	__slots__ = ()

	def calcular(self):
		self.vazões()
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
        for key in self.out:
            if type(self.out[key]) == float:
                self.out[key] = round(self.out[key], 4)


def factory_VA(vainit):
	global varesults

	d = dict(vainit, **varesults)

	class VA(VA_Methods, VA_Parte1, VA_Main,Extras):
	    __slots__ = [key for key in d]
	    def __init__(self):
	        for key in d:
	            setattr(self, key, d[key])
	return VA



