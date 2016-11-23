class KlassName_Methods():
    __slots__=()

    def f(self):
        pass


class KlassName_Parte1():
    __slots__=()

    def parte1(self):
        pass

class KlassName_Parte2():
    __slots__=()

    def parte2(self):
        pass


class Extras():
    __slots__=()

    def make_out(self):
        d=dict((name, getattr(self, name)) for name in dir(self) 
        if not name.startswith('__') and 
        not callable(getattr(self,name))) 
        self.out=d

    def arredondamento(self):
        for key in self.out:
            if type(self.out[key]) == float:
                self.out[key]=round(self.out[key],4)


class KlassName_Main():
    __slots__=()

    def dimensionar(self):    
        self.parte1()
        self.parte2()
        
        self.make_out()
        self.arredondamento()


klassName_dict_inputs={
    "B":None,
} 

def factory_KlassName(inp):  
    r={
        "L0":None,
        
        "out":None
    }

    d=dict(inp, **r)

    class KlassName(KlassName_Methods, KlassName_Part1, KlassName_Part2, KlassName_Part3,
                Extras, KlassName_Main):
        __slots__ = [key for key in d]
        def __init__(self):
            for key in d:
                setattr(self, key, d[key])

    return KlassName