import math

#import jinja2
#from jinja2 import Template

import os
import tempfile
import subprocess
from subprocess import Popen, PIPE
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

from django.template.loader import render_to_string

global cpinit

cpinit = {
    'Q':None,
    'g':None,
    'T':None,
    'c':None,
    'iW':None,
}

global cpresults
cpresults = {
    'mu':None,
    'rho':None,
    'W':None,
    'A':None,
    'B':None,
    'B23':None,
    'C':None,
    'D':None,
    'E':None,
    'F':None,
    'L':None,
    'K':None,
    'N':None,
    'k':None,
    'n':None,
    'H0':None,
    'D0':None,
    'U0':None,
    'q':None,
    'E0':None,
    'U1':None,
    'h1':None,
    'F1':None,
    'h2':None,
    'h3':None,
    'U3':None,
    'Lr':None,
    'h':None,
    'Tm':None,
    'Gm':None,
    'out':None,
    'restrição':None,
    'dimençõesPadronizadas':None,
    'valoreskn': None,
}


class TabelasCalhaParshall():
    __slots__=()

    def setTabelas(self):
        self.dimençõesPadronizadas = [
                    [ 229, 880, 864, 380, 575, 763, 305, 457, 76, 114],
                    [ 305, 1372, 1344, 610, 845, 915, 610, 915, 76, 229],
                    [ 457, 1449, 1420, 762, 1026, 915, 610, 915, 76, 229],
                    [ 610, 1525, 1496, 915, 1207, 915, 610, 915, 76, 229],
                    [ 915, 1677, 1645, 1220, 1572, 915, 610, 915, 76, 229],
                    [ 1220, 1830, 1795, 1525, 1938, 915, 610, 915, 76, 229],
                    [ 1525, 1983, 1941, 1830, 2303, 915, 610, 915, 76, 229],
                    [ 1830, 2135, 2090, 2135, 2667, 915, 610, 915, 76, 229],
                    [ 2135, 2288, 2240, 2440, 3030, 915, 610, 915, 76, 229],
                    [ 2440, 2440, 2392, 2745, 3400, 915, 610, 915, 76, 229]]

        self.valoreskn = [
                    [229, 1.486, 0.633],
                    [305, 1.276, 0.657],
                    [457, 0.966, 0.65],
                    [610, 0.795, 0.64],
                    [915, 0.608, 0.639],
                    [1220, 0.505, 0.634],
                    [1525, 0.436, 0.63],
                    [1830, 0.389, 0.627],
                    [2135, 0.355, 0.625],
                    [2440, 0.324, 0.623]]

"""
for linha in t:
    for e in linha:
    print('<td> ', e, ' </td>')
    print(" ")

    [[229, 880, 864, 380, 575, 763, 305, 457, 76, 114, 229, 1.486, 0.633],
    [305, 1372, 1344, 610, 845, 915, 610, 915, 76, 229, 305, 1.276, 0.657],
    [457, 1449, 1420, 762, 1026, 915, 610, 915, 76, 229, 457, 0.966, 0.65],
    [610, 1525, 1496, 915, 1207, 915, 610, 915, 76, 229, 610, 0.795, 0.64],
    [915, 1677, 1645, 1220, 1572, 915, 610, 915, 76, 229, 915, 0.608, 0.639],
    [1220, 1830, 1795, 1525, 1938, 915, 610, 915, 76, 229, 1220, 0.505, 0.634],
    [1525, 1983, 1941, 1830, 2303, 915, 610, 915, 76, 229, 1525, 0.436, 0.63],
    [1830, 2135, 2090, 2135, 2667, 915, 610, 915, 76, 229, 1830, 0.389, 0.627],
    [2135, 2288, 2240, 2440, 3030, 915, 610, 915, 76, 229, 2135, 0.355, 0.625],
    [2440, 2440, 2392, 2745, 3400, 915, 610, 915, 76, 229, 2440, 0.324, 0.623]]
"""
class DensidadeViscosidade():
    __slots__=()

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


class CP_Methods():
    __slots__=()

    def fH0(self, k, Q, n):
        return k*Q**(n)
        
    def fD0(self, D, W):
        return (2/3)*(D - W) + W
    
    def fU0(self, Q, D0, H0):
        return Q/(D0*H0)

    def fq(self, Q, W):
        return Q/W

    def fE0(self, U0, g, H0, N):
        return (U0**2)/(2*g) + H0 + N

    def fU1(self, g, q, E0):
        x = -g*q/(((2/3)*g*E0)**(1.5))
        a = ((2*g*E0)/3)**(1/2)
        return 2*a*math.cos(math.acos(x)/3)

    def fh1(self, q, U1):
        return q/U1

    def froud(self, g, h, U):
        return U/(g*h)**(1/2)
    
    def fh2(self, h1, F1):
        return (h1/2)*((1 + 8*F1**2)**(1/2) - 1)

    def fh3(self, h2, N, K):
        return h2 - (N - K)

    def fU3(self, Q, C, h3):
        return Q/(C*h3)
        
    def fLr(self, c, h1, h2):
        return c*(h2 - h1)

    def fh(self, h1, h2):
        return ((h2 - h1)**3)/(4*h1*h2)

    def fTm(self, L, U1, U3):
        return (2*L)/(U1 + U3)

    def fGm(self, h, g, rho, mu, Tm):
        return ((g*rho*h)/(mu*Tm))**(1/2)


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


class Níveis():
    __slots__=()

    def setCDKN_kn(self, i):
        self.W = self.dimençõesPadronizadas[i][0]/1000
        self.A = self.dimençõesPadronizadas[i][1]/1000
        self.B = self.dimençõesPadronizadas[i][2]/1000
        self.C = self.dimençõesPadronizadas[i][3]/1000
        self.D = self.dimençõesPadronizadas[i][4]/1000
        self.E = self.dimençõesPadronizadas[i][5]/1000
        self.F = self.dimençõesPadronizadas[i][6]/1000
        self.L = self.dimençõesPadronizadas[i][7]/1000
        self.K = self.dimençõesPadronizadas[i][8]/1000
        self.N = self.dimençõesPadronizadas[i][9]/1000
        self.k = self.valoreskn[i][1]
        self.n = self.valoreskn[i][2]

    def pré_dimensionar(self):
        
        self.rho = self.frho(self.T)
        self.mu = self.fmu(self.T)
        self.H0 = self.fH0(self.k, self.Q, self.n)
        self.D0 = self.fD0(self.D, self.W)
        self.U0 = self.fU0(self.Q, self.D0, self.H0)
        self.q = self.fq(self.Q, self.W)
        self.E0 = self.fE0(self.U0, self.g, self.H0, self.N)
        self.U1 = self.fU1(self.g, self.q, self.E0)
        self.h1 = self.fh1(self.q, self.U1)
        self.F1 = self.froud(self.g, self.h1, self.U1)
        self.h2 = self.fh2(self.h1, self.F1)
        self.h3 = self.fh3(self.h2, self.N, self.K)
        self.U3 = self.fU3(self.Q, self.C, self.h3)
        self.Lr = self.fLr(self.c, self.h1, self.h2)
        self.h = self.fh(self.h1, self.h2)
        self.Tm = self.fTm(self.Lr, self.U1, self.U3)
        self.Gm = self.fGm(self.h, self.g, self.rho, self.mu, self.Tm)

    def checagem(self):
        assert self.T > 0 
        assert self.Q > 0 
        assert self.g > 0

    def dimensionar(self):
        self.iW -= 1
        if self.iW not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            assert False, 'O valor do indice da garganta da calha parshall é invalido!'
        else:
            #self.checagem()
            self.setTabelas()
            self.setCDKN_kn(self.iW)
            self.pré_dimensionar()
            self.make_out()
            self.arredondamento()


# https://books.google.com.br/books?id=uPSoCwAAQBAJ&pg=PA274&lpg=PA274&dq=save+render_to_string+file+django&source=bl&ots=igy7pOfeOy&sig=ZFgxmOitm8LHSICjQfWy5ZvdtTI&hl=pt-BR&sa=X&ved=0ahUKEwjfoO2FmLPSAhVDG5AKHXwjBrUQ6AEITDAG#v=onepage&q=save%20render_to_string%20file%20django&f=false            

class GerarPDF():
    __slots__=()

    # https://blog.sevenbyte.org/2014/09/23/generating-pdfs-with-django-and-latex.html
    def gerar_pdf(self):
        self.dimensionar()
        context = self.out

        template = get_template('project/calha_parshall2/calha_parshall_latex/mestre.tex')
        rendered_tpl = template.render(context).encode('utf-8')
        
        with tempfile.TemporaryDirectory() as tempdir:
            #import shutil
            #path = 'soma/project/templates/project/calha_parshall2/calha_parshall_latex/mestre.pdf'
            #path = 'project/templates/project/calha_parshall2/calha_parshall.pdf'
            #shutil.copy(path, tempdir)
            for i in range(2):
                process = Popen(
                    ['pdflatex', '-output-directory', tempdir],
                    stdin=PIPE,
                    stdout=PIPE,
                )
                process.communicate(rendered_tpl)
            with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
                pdf = f.read()

            r = HttpResponse(content_type='application/pdf')  
            # r['Content-Disposition'] = 'attachment; filename=texput.pdf'
            r.write(pdf)

        return r     

    def renderizar_template(self, path, template_name, context):    
        return render_to_string(path + template_name + '.tex', context) 

    def salvar_template_rederizado(self, rendered_templete, path, template_name):
        with open(path + template_name + '_rendered' + '.tex', 'w') as rt:
            rendered_templete.encode('utf-8')
            rt.write(rendered_templete)        

    def criar_pdf(self, path, template_name):
        initial_path = os.getcwd()
        os.chdir(path)
        subprocess.call(['pdflatex', template_name])    
        os.chdir(initial_path)

    def context_figura(self):
        d = {
            'H0':self.H0,
            'V0':self.U0,
            'N':self.N,
            'D':self.D,
            'D0':self.D0,
            'W':self.W,
            'B':self.B,
            'B23':(2*self.B)/3, # TODO: Criar uma função que calcula (2/3)*B
            'C':self.C,
            'F':self.F,
            'L':self.L,
            'N':self.N, 
            'k':self.k,
            'h1':self.h1,
            'h2':self.h2,
            'h3':self.h3,
            'k':self.k,
            'L':self.L,
            'D':self.D,
        }
        for key in d:
            d[key] = round(d[key], 3)
        return d

    def render_pdf(self, path):
        with open(path, 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=some_file.pdf'
        return response

    def gerar_figura_calha_parshal(self):
        self.dimensionar()
        
        path1 = 'project/calha_parshall2/calha_parshall_latex/'
        template_name = 'calha_parshall_builded'
        context = self.context_figura()
        rendered_templete = self.renderizar_template(path1, template_name, context)

        try:
            pathSTR = 'soma/project/templates/' + path1
            self.salvar_template_rederizado(rendered_templete, pathSTR, template_name)
            path2 = 'soma/project/templates/project/calha_parshall2/calha_parshall_latex/'
            template_name = 'calha_parshall_builded_rendered.tex'
            self.criar_pdf(path2, template_name)

            path2 = path2 + 'calha_parshall_builded_rendered.pdf'
            return self.render_pdf(path2)
        except:
            pathSTR = 'project/templates/' + path1
            self.salvar_template_rederizado(rendered_templete, pathSTR, template_name)            

            path2 = 'project/templates/project/calha_parshall2/calha_parshall_latex/'
            template_name = 'calha_parshall_builded_rendered.tex'
            self.criar_pdf(path2, template_name)

            path2 = path2 + 'calha_parshall_builded_rendered.pdf'
            return self.render_pdf(path2)
        



def factory_CP(cpinit):
    global cpresults

    d = dict(cpinit, **cpresults)

    class CP(CP_Methods, TabelasCalhaParshall, DensidadeViscosidade, Extras,
                Níveis, GerarPDF):
        __slots__ = [key for key in d]
        def __init__(self):
            for key in d:
                setattr(self, key, d[key])
    return CP



