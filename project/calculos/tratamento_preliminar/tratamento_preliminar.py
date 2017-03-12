import math
import os
import tempfile
import subprocess
from django.http import HttpResponse
from django.template.loader import render_to_string


global initTratamentoPreliminar
initTratamentoPreliminar = {
    'Qmáx':None,
    'Qméd':None,
    'Qmín':None,
    't':None, # Espessura da grade
    'a':None, # Espaçamento da grade
    'Vg':None,
    'g':None,
    'V':None,
    'AreiaAcu':None,
    'tl':None,
}

global resultsTratamentoPreliminar
resultsTratamentoPreliminar = {
    'tabela':None,
    'W':None,
    'n':None,
    'lamb':None,
    'Hmáx':None,
    'Hmín':None,
    'ymáx':None,
    'ymín':None,
    'Z':None,
    'Au':None,
    'E':None,
    'S':None,
    'b':None,
    'V0': None,
    'Deltah_limpa':None,
    'Deltah_50':None,
    'A':None,
    'B':None,
    'Vv':None,
    'L':None,
    'TESmáx':None,
    'QmédAreia':None,
    'VmédAreia':None,
    'A_P':None,
    'H_AreiaAc':None,
    'out':None,
}


class TabelaTratamentoPreliminar():
    __slots__=()

    def setTabelaTratamentoPreliminar(self):
        self.tabela = [
            [7.6,   0.85,   53.8,   1.547,   0.176],
            [15.2,  1.45,   110.4,  1.58,    0.381],
            [22.9,  2.55,   251.9,  1.53,    0.535],
            [30.5,  3.11,   455.6,  1.522,   0.690],
            [45.7,  4.25,   696.0,  1.538,   1.054],
            [61,    11.89,  936.7,  1.55,    1.426],
            [91.5,  17.89,  1426.3, 1.556,   2.182],
            [122,   36.79,  1921.3, 1.578,   2.935],
            [152.5, 45.3,   2422.0, 1.587,   3.728],
            [183.0, 73.6,   2929.0, 1.595,   4.515],
            [213.5, 84.95,  3440.0, 1.601,   5.306],
            [244.0, 99.1,   3950.0, 1.606,   6.101]
        ]


    def setWnlamb(self, Qmáx):
        assert Qmáx < 3.95, 'Erro na função setWnlamb.'
        i = 0
        while Qmáx >= self.tabela[i][2]/1000:
            i += 1
        self.W = self.tabela[i][0]
        self.n = self.tabela[i][3]
        self.lamb = self.tabela[i][4]            
        
class TratamentoPreliminarMethods():
    __slots__ = ()
    
    def fH(self, Q, n, lamb):
        return (Q/lamb)**(1/n)

    def fy(self, H, Z):
        return H - Z

    def fZ(self, Hmín, Hmáx, Qmín, Qmáx):
        num = Hmín*Qmáx - Qmín*Hmáx
        den = Qmáx - Qmín
        return num/den

    def fE(self, t, a):
        return a/(a + t)

    def fAu(self, Qmáx, Vg):
        return Qmáx/Vg

    def fS(self, Au, E):
        return Au/E

    def fb(self, S, Hmáx, Z):
        return S/(Hmáx - Z)

    def fV0(self, Qmáx, S):
        return Qmáx/S

    def  fDeltah_limpa(self, Vg, V0, g):
        num = 1.43*(Vg**2 - V0**2) 
        den = 2*g
        return num/den

    def  fDeltah_50(self, Vg, V0, g):
        num = 1.43*((2*Vg)**2 - V0**2)
        den = 2*g
        return num/den

    def fA(self, Qmáx, V):
        return Qmáx/V

    def fB(self, A, Hmáx, Z):
        return A/(Hmáx - Z)

    def fVv(self, Qmín, Hmín, Z, B):
        return Qmín/((Hmín - Z)*B)

    def fL(self, Hmáx, Z):
        return 22.5*(Hmáx - Z)

    def fTESmáx(self, Qmáx, B, L):
        return (60*60*24*Qmáx)/(B*L)

    def fQmédAreia(self, AreiaAcu, Qméd):
        return 3.6*24*AreiaAcu*Qméd/1000

    def fVmédAreia(self, QmédAreia, tl):
        return QmédAreia*tl

    def fA_P(self, L, B):
        return L*B

    def fH_AreiaAc(self, A_P, VmédAreia):
        return VmédAreia/A_P

class Extras():
    __slots__ = ()

    def make_out(self):
        d = dict((name, getattr(self, name)) for name in dir(self) 
        if not name.startswith('__') and 
        not callable(getattr(self, name))) 
        self.out = d

    def arredondamento(self):
        for key in self.out:
            if type(self.out[key]) == float:
                if key == 'mu':
                    self.out[key] = round(self.out[key], 5)
                elif key == 'tl':
                    self.out[key] = int(self.out[key])
                else:
                    self.out[key] = round(self.out[key], 3)


class Níveis():
    __slots__=()

    def checagem(self):
        assert self.Qmín <= self.Qmáx 

    def nível1(self):
        self.checagem()

        self.setTabelaTratamentoPreliminar()

    def nível2(self):
        self.setWnlamb(self.Qmáx)

    def nível3(self):
        self.Hmín = self.fH(self.Qmín, self.n, self.lamb)
        self.Hmáx = self.fH(self.Qmáx, self.n, self.lamb)
        self.E = self.fE(self.t, self.a)
        self.Au = self.fAu(self.Qmáx, self.Vg)
        self.A = self.fA(self.Qmáx, self.V)
        self.QmédAreia = self.fQmédAreia(self.AreiaAcu, self.Qméd)

    def nível4(self):
        self.Z = self.fZ(self.Hmín, self.Hmáx, self.Qmín, self.Qmáx)
        self.S = self.fS(self.Au, self.E)
        self.B = self.fB(self.A, self.Hmáx, self.Z)
        self.VmédAreia = self.fVmédAreia(self.QmédAreia, self.tl)

    def nível5(self):
        self.b = self.fb(self.S, self.Hmáx, self.Z)
        self.V0 = self.fV0(self.Qmáx, self.S)    
        self.L = self.fL(self.Hmáx, self.Z)  
        self.Vv = self.fVv(self.Qmín, self.Hmín, self.Z, self.B)  
        self.ymín = self.fy(self.Hmín, self.Z) 
        self.ymáx = self.fy(self.Hmáx, self.Z)   

    def nível6(self):
        self.Deltah_50 = self.fDeltah_50(self.Vg, self.V0, self.g)
        self.Deltah_limpa = self.fDeltah_limpa(self.Vg, self.V0, self.g)
        self.TESmáx = self.fTESmáx(self.Qmáx, self.B, self.L)
        self.A_P = self.fA_P(self.L, self.B)

    def nível7(self):
        self.H_AreiaAc = self.fH_AreiaAc(self.A_P, self.VmédAreia)

    def calcularNíveis(self):
        self.nível1()
        self.nível2()
        self.nível3()
        self.nível4()
        self.nível5()
        self.nível6()
        self.nível7()


    def dimensionar(self):
        self.calcularNíveis()
        self.make_out()
        self.arredondamento()


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

    def figura_tratamento_preliminar(self):
        self.dimensionar()

        path = 'project/tratamento_preliminar/tratamento_preliminar_figura/'
        template_name = 'tratamento_preliminar_overlay_base'
        context = self.out
        rendered_templete = self.renderizar_template(path, template_name, context)

        path = 'project/templates/' + path
        template_name += '_rendered' 
        try:
            return self.gerarPDF(rendered_templete, path, template_name, root='soma/')
        except:        
            return self.gerarPDF(rendered_templete, path, template_name)
        
    def calculos_tratamento_preliminar(self):
        self.dimensionar()

        path = 'project/tratamento_preliminar/tratamento_preliminar_calculos/'
        template_name = 'tratamento_preliminar_calculos'
        context = self.out
        rendered_templete = self.renderizar_template(path, template_name, context)

        path = 'project/templates/' + path
        template_name += '_rendered' 
        try:
            return self.gerarPDF(rendered_templete, path, template_name, root='soma/')
        except:        
            return self.gerarPDF(rendered_templete, path, template_name) 


def factoryTratamentoPreliminar(initTratamentoPreliminar):
    global resultsTratamentoPreliminar

    d = dict(initTratamentoPreliminar, **resultsTratamentoPreliminar)

    class TP(TratamentoPreliminarMethods, Extras,
                Níveis, GerarPDF, TabelaTratamentoPreliminar):
        __slots__ = [key for key in d]
        def __init__(self):
            for key in d:
                setattr(self, key, d[key])
    return TP





