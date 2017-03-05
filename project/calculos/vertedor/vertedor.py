import os
import subprocess 
from scipy.optimize import minimize
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html
# from scipy.optimize import minimize_scalar


from django.template.loader import render_to_string
from django.http import HttpResponse

global vertedorinit
vertedorinit = {
    'Q':None,
    'g':None,
    'T':None,
    'b':None,
    'F1':None,
    'c':None,
}

global vertedorresults
vertedorresults = {
    'Pvr':None,
    'yc':None,
    'y1':None,
    'v1':None,
    'F1c':None,
    'y2':None,
    'y216':None,
    'y256':None,
    'Lm':None,
    'Hvr':None,
    'En':None,
    'v2':None,
    'Um':None,
    'Lr':None,
    'gamma':None,
    'mu':None,
    'Tm':None,
    'Gm':None,
    'out':None,
}


class VertedorMethods():
    __slots__ = ()

    @classmethod
    def fHvr(self, Q, b):
        return (Q/(1.848*b))**(3/2)

    @classmethod
    def fLm(self, Hvr, Pvr):
        a = 1.45*Hvr
        b = (Pvr/Hvr)**(0.54)
        return a*b

    @classmethod
    def fyc(self, Q, g, b):
        assert Q > 0 and g > 0 and b > 0
        return ((Q**2)/(g*b**2))**(1/3)
    
    @classmethod
    def fy1(self, yc, Pvr):
        assert yc > 0 and Pvr > 0
        num = 1.414*yc
        den = (2.56 + Pvr/yc)**(0.5)
        return num/den

    @classmethod
    def fV(self, Q, y, b):
        return Q/(y*b)

    @classmethod
    def Froud(self, V, y, g):
        return V/(g*y)**(1/2)

    @classmethod
    def fy2(self, y1, F1):
        return (y1/2)*( (1 + 8*F1**2)**(0.5) - 1)
    
    @classmethod
    def fy216(self, y2):
        return y2/6

    @classmethod
    def fy256(self, y2):
        return 5*y2/6

    @classmethod
    def fEn(self, y1, y2):
        return ((y2 - y1)**3)/(4*y1*y2)
    
    @classmethod
    def fUm(self, U1, U2):
        return (U1 + U2)/2

    @classmethod
    def fLr(self, c, y1, y2):
        return c*(y2 - y1)

    @classmethod
    def fTm(self, Lr, Um):
        return Lr/Um

    @classmethod
    def fGm(self, gamma, En, Tm, mu ):
        return ((gamma*En)/(mu*Tm))**(0.5)


class VertedorOtimização():
    __slots__ = ()        

    @classmethod
    def f(self, Pvr, Q, F1, g, b):
        yc = self.fyc(Q, g, b)
        y1 = self.fy1(yc, Pvr)
        v1 = self.fV(Q, y1, b)
        
        return (F1 - v1/(g*y1)**(1/2))**2

    @classmethod
    def fPvr(self, Q, F1, g, b):
        x0 = 0.5
        t = (Q, F1, g, b)
        resposta = minimize(self.f, x0, args=t, method='nelder-mead',
                    options={'xtol': 10**-5, 'disp': False})
        return float(resposta.x)


class DensidadeViscosidade():
    __slots__ = ()

    def fgamma(self, g, T):
        return g*self.frho(T)

    def frho(self, T):
        t0 = 3.9818
        A = 7.0134*10**(-8)
        B = 7.926504*10**(-6)
        C = -7.575677*10**(-8)
        D = 7.314894*10**(-10)
        E = -3.596458*10**(-12)
        rho = 999.97358
        L = [A, B, C, D, E]
        soma = 0
        for i in range(len(L)):
            soma += L[i]*(T - t0)**(i + 1)

        return rho*(1 - soma)

    def fmu(self, T):
        a = 2.414*10**(-5)
        b = 247.8
        c = 140 - 273.15 # Conversão para graus Celsius
        return a*10**(b/(T - c)) 


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


class VertedorNíveis():
    __slots__ = ()

    def nível1(self):
        self.Hvr = self.fHvr(self.Q, self.b)
        self.gamma = self.fgamma(self.g, self.T)
        self.mu = self.fmu(self.T)
        self.Pvr = self.fPvr(self.Q, self.F1, self.g, self.b)

    def nível2(self):
        self.yc = self.fyc(self.Q, self.g, self.b)
        self.y1 = self.fy1(self.yc, self.Pvr)
        self.Lm = self.fLm(self.Hvr, self.Pvr)

    def nível3(self):
        self.v1 = self.fV(self.Q, self.y1, self.b)

    def nível4(self):
        self.F1c = self.Froud(self.v1, self.y1, self.g)
    
    def nível5(self):
        self.y2 = self.fy2(self.y1, self.F1)
        self.y216 = self.fy216(self.y2)
        self.y256 = self.fy256(self.y2)

    def nível6(self):        
        self.En = self.fEn(self.y1, self.y2)
        self.v2 = self.fV(self.Q, self.y2, self.b)
        self.Lr = self.fLr(self.c, self.y1, self.y2)

    def nível7(self):
        self.Um = self.fUm(self.v1, self.v2)

    def nível8(self):
        self.Tm = self.fTm(self.Lr, self.Um)

    def nível9(self):
        self.Gm = self.fGm(self.gamma, self.En, self.Tm, self.mu)

    def calcularNíveis(self):
        self.nível1()
        self.nível2()
        self.nível3()
        self.nível4()
        self.nível5()
        self.nível6()
        self.nível7()
        self.nível8()
        self.nível9()


class GerarPDF():
    __slots__=()   

    def renderizar_template(self, path, template_name, context):    
        return render_to_string(path + template_name + '.tex', context) 

    def salvar_template_rederizado(self, rendered_templete, path, template_name):
        with open(path + template_name + '.tex', 'w') as rt:
            rendered_templete.encode('utf-8')
            rt.write(rendered_templete)        

    def criar_pdf(self, path, template_name):
        initial_path = os.getcwd()
        os.chdir(path)
        subprocess.call(['pdflatex', template_name])    
        os.chdir(initial_path)

    def render_pdf(self, complete_path):
        with open(complete_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=some_file.pdf'
        return response


    def gerarPDF(self, rendered_templete, path, template_name, root=''):
        complete_path = root + path
        self.salvar_template_rederizado(rendered_templete,
                                        complete_path, template_name)
        self.criar_pdf(complete_path, template_name)

        path_pdf = complete_path + template_name + '.pdf'
        return self.render_pdf(path_pdf)        

    def figura_vertedor(self):
        self.dimensionar()

        path = 'project/vertedor/vertedor_figura/'
        template_name = 'vertedor_overlay_base'
        context = self.out
        rendered_templete = self.renderizar_template(path, template_name, context)

        path = 'project/templates/' + path
        template_name += '_rendered' 
        try:
            return self.gerarPDF(rendered_templete, path, template_name, root='soma')
        except:        
            return self.gerarPDF(rendered_templete, path, template_name)

    def calculos_vertedor(self):
        self.dimensionar()

        path = 'project/vertedor/vertedor_calculos/'
        template_name = 'vertedor_calculos'
        context = self.out
        rendered_templete = self.renderizar_template(path, template_name, context)

        path = 'project/templates/' + path
        template_name += '_rendered' 
        try:
            return self.gerarPDF(rendered_templete, path, template_name, root='soma')
        except:        
            return self.gerarPDF(rendered_templete, path, template_name)        

class VertedorMain():

    def dimensionar(self):
        self.calcularNíveis()
        self.make_out()
        self.arredondamento()



def factoryVertedor(vertedorinit):
    global vertedorresults

    d = dict(vertedorinit, **vertedorresults)

    class V(VertedorMethods, DensidadeViscosidade, Extras,
            VertedorOtimização, VertedorNíveis, VertedorMain, GerarPDF):
        __slots__ = [key for key in d]
        def __init__(self):
            for key in d:
                setattr(self, key, d[key])
    return V
