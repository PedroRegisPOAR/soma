import math
import os
import matplotlib 
import numpy as np

import random
import time

# http://stackoverflow.com/questions/27147300/how-to-clean-images-in-python-django
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from matplotlib.legend_handler import HandlerLine2D

# Eu não entendo como e porque esse import funciona.
from project.models import ProjeçãoPopulacional
from io import StringIO, BytesIO
from django.core.files import File


ppinit = {	
		't0':None,
		't1':None,
		't2':None,
		't3':None,
		't4':None,
		't5':None,
		'P0':None,
		'P1':None,
		'P2':None,
	}


global ppresults
ppresults = {
	    'Ka': None,		
	    'Kg': None,		
	    'Ps': None,		
	    'Kd': None,		
	    'K1': None,		
	    'c': None,				
	    'P3_PA': None,		
	    'P3_PG': None,		
	    'P3_TD': None,		
	    'P3_CL': None,				
	    'P4_PA': None,		
	    'P4_PG': None,		
	    'P4_TD': None,		
	    'P4_CL': None,				
	    'P5_PA': None,		
	    'P5_PG': None,		
	    'P5_TD': None,		
	    'P5_CL': None,				
	    'y_PA': None,		
	    'y_PG': None,		
	    'y_TD': None,		
	    'y_CL': None,				
		'x_censo': None,
	    'y_censo': None, 		        	
	    'x_projeção': None,
	    'y_PA_projeção': None,		
	    'y_PG_projeção': None,		
	    'y_TD_projeção': None,		
	    'y_CL_projeção': None,
        'is_projetavél': None,
        'foi_dimensionado': None,
        'out':None,
	}


class PP_Methods():
    __slots__=()

    def fKa(self, P1, P2, t1 ,t2):
        return (P2 - P1)/(t2 - t1)

    def projeçãoAritimética(self, t, P0, Ka, t0):
        return P0 + Ka*(t - t0)

    def fKg(self, P0, P2, t0, t2):
        return (math.log(P2) - math.log(P0))/(t2 - t0)

    def projeçãoGeométrica(self, t, P0, Kg, t0):
        return P0*math.e**(Kg*(t - t0))        
    
    @classmethod
    def fPsNum(self, P0, P1, P2):
        return 2*P0*P1*P2 - (P1**2)*(P0 + P2)

    @classmethod
    def fPsDen(self, P0, P1, P2):
        return P0*P2 - P1**2

    @classmethod
    def fPs(self, P0, P1, P2):
        num = self.fPsNum(P0, P1, P2)
        den = self.fPsDen(P0, P1, P2)
        return num/den
    
    @classmethod
    def fKdArgLog(self, Ps, P0, P2):
        return (Ps - P2)/(Ps + P0)

    def fKd(self, Ps, P0, P2, t0, t2):
        x = self.fKdArgLog(Ps, P0, P2)
        num = - math.log(x)
        den = t2 - t0
        return num/den

    def taxaDecrescente(self, t, t0, Ps, P0, Kd):
        return P0 + (Ps - P0)*(1 - math.e**(-Kd*(t - t0)))    

    def fc(self, Ps, P0):
        return (Ps - P0)/P0

    @classmethod
    def fK1ArgLog(self, P0, P1, Ps):
        num = P0*(Ps - P1)
        den = P1*(Ps - P0)
        return num/den

    def fK1(self, t1, t2, P0, P1, Ps):
        a= (1/(t2 - t1))
        arg = self.fK1ArgLog(P0, P1, Ps)
        b = math.log(arg)
        return a*b

    def crescimentoLogístico(self, t, t0, Ps, c, K1):        
        return Ps/(1 + c*math.e**(K1*(t - t0)))


class PP_Parte1():
    __slots__=()

    def inicializaConstantesDasCurvasPsKd(self):
        self.Ps = self.fPs(self.P0, self.P1, self.P2)
        self.Kd = self.fKd(self.Ps, self.P0, self.P2, self.t0, self.t2)

    def inicializaConstantesDasCurvasK1c(self):
        # TODO: verificar se é necessario calcular Ps aqui
        # self.Ps = self.fPs(self.P0, self.P1, self.P2)
        self.c  = self.fc(self.Ps, self.P0)
        self.K1 = self.fK1(self.t1, self.t2, self.P0, self.P1, self.Ps)

    def inicializaConstantesDasCurvas(self):
        self.inicializaConstantesDasCurvasPAPG()
        self.inicializaConstantesDasCurvasPsKd()
        self.inicializaConstantesDasCurvasK1c()
    
    def inicializaConstantesDasCurvasPAPG(self):
        self.Ka = self.fKa(self.P1, self.P2, self.t1 ,self.t2)
        self.Kg = self.fKg(self.P0, self.P2, self.t0, self.t2)

    def inicializaConstantesDasCurvasPAPGTD(self):
        self.inicializaConstantesDasCurvasPAPG()
        self.inicializaConstantesDasCurvasPsKd()        

    def inicializaConstantesDasCurvasPAPGCL(self):
        self.inicializaConstantesDasCurvasPAPG()
        self.inicializaConstantesDasCurvasK1c()


    def incializaCensoProjeção(self):
        self.x_projeção = list(np.arange( (1 - 0.005 )*self.t0, self.t5, 0.1))
        self.x_censo = [self.t0, self.t1, self.t2]
        self.y_censo = [self.P0, self.P1, self.P2]


class PP_Parte2():
    __slots__=()

    def projeções(self, t):
        tpapg = self.projeçõesPAPG(t)
        c = self.taxaDecrescente(t, self.t0, self.Ps, self.P0, self.Kd)
        d = self.crescimentoLogístico(t, self.t0, self.Ps,
                                                self.c, self.K1)
        return tpapg + (c, d)

    def calculaPopulações(self):
        self.P3_PA, self.P3_PG, self.P3_TD, self.P3_CL = self.projeções(self.t3)
        self.P4_PA, self.P4_PG, self.P4_TD, self.P4_CL = self.projeções(self.t4)
        self.P5_PA, self.P5_PG, self.P5_TD, self.P5_CL = self.projeções(self.t5)

    def projeçõesPAPG(self, t):
        a = self.projeçãoAritimética(t, self.P0, self.Ka, self.t0)
        b = self.projeçãoGeométrica(t, self.P0, self.Kg, self.t0)
        return a, b

    def calculaPopulaçõesPAPG(self):
        self.P3_PA, self.P3_PG = self.projeçõesPAPG(self.t3)
        self.P4_PA, self.P4_PG = self.projeçõesPAPG(self.t4)
        self.P5_PA, self.P5_PG = self.projeçõesPAPG(self.t5)

    def projeçõesPAPGTD(self, t):
        tpapg = projeçõesPAPG(self, t)
        c = self.taxaDecrescente(t, self.t0, self.Ps, self.P0, self.Kd)
        return tpapg + c

    def calculaPopulaçõesPAPGTD(self):
        self.P3_PA, self.P3_PG, self.P3_TD = self.projeções(self.t3)
        self.P4_PA, self.P4_PG, self.P4_TD = self.projeções(self.t4)
        self.P5_PA, self.P5_PG, self.P5_TD = self.projeções(self.t5)

    def projeçõesPAPGCL(self, t):
        tpapg = projeçõesPAPG(self, t)
        c = self.crescimentoLogístico(t, self.t0, self.Ps,
                                                self.c, self.K1)
        return tpapg + c

    def calculaPopulaçõesPAPGCL(self):
        self.P3_PA, self.P3_PG, self.P3_CL = self.projeções(self.t3)
        self.P4_PA, self.P4_PG, self.P4_CL = self.projeções(self.t4)
        self.P5_PA, self.P5_PG, self.P5_CL = self.projeções(self.t5)        


class PP_Parte3():
    __slots__=()

    def preenche_y_projeçõe(self, key=None):
        def f1(t):
            return self.projeçãoAritimética(t, self.P0, self.Ka, self.t0)
        def f2(t):
            return self.projeçãoGeométrica(t, self.P0, self.Kg, self.t0)
        def f3(t):
            return self.taxaDecrescente(t, self.t0, self.Ps, self.P0, self.Kd)
        def f4(t):
            return self.crescimentoLogístico(t, self.t0, self.Ps, self.c, self.K1)

        def gPAPG():
            self.y_PA_projeção = [f1(t) for t in self.x_projeção]
            self.y_PG_projeção = [f2(t) for t in self.x_projeção]            

        if key is None:
            gPAPG()
            self.y_TD_projeção = [f3(t) for t in self.x_projeção]
            self.y_CL_projeção = [f4(t) for t in self.x_projeção]
        elif key=='PAPG':
            gPAPG()            
        elif key=='PAPGTD':
            gPAPG()
            self.y_TD_projeção = [f3(t) for t in self.x_projeção]
        elif key=='PAPGCL':
            gPAPG()
            self.y_CL_projeção = [f4(t) for t in self.x_projeção]
        else:
            assert False, ''' Erro na função preenche_y_projeçõe,
                                o parametro key esta errado'''

class PP_Parte4():
    __slots__=()	

    def salva_imagem(self, plt, name):
        from project.models import ProjeçãoPopulacional
        f = BytesIO()
        plt.savefig(f, format="png")
        content_file = File(f)
        model_object = ProjeçãoPopulacional()
        model_object.imagem.save(name + '.png', content_file)
        model_object.save()
        plt.close()

    def criaGráfico(self, label_image, y_projeção,
                        ls_projeção='-', ls_censo='o'):

        x = self.x_projeção + self.x_censo
        y = y_projeção + self.y_censo
        p = 0.005
        x_min = min(x) - p*( (max(x)**2 + min(x)**2)**(1/2) )
        y_min = min(y) - p*( (max(y)**2 + min(y)**2)**(1/2) )
        x_max = max(x) + p*( (max(x)**2 + min(x)**2)**(1/2) )
        y_max = max(y) + p*( (max(y)**2 + min(y)**2)**(1/2) )

        plt.axis([x_min, x_max, y_min, y_max])
        line1, = plt.plot(self.x_projeção, y_projeção, ls_projeção, color='blue', label=label_image)
        line2, = plt.plot(self.x_censo, self.y_censo, ls_censo, color='green', label='Censo')

        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

        return plt

    def cria_e_salva_PAPG(self):
        plt = self.criaGráfico('Projeção Aritmética', self.y_PA_projeção)
        self.salva_imagem(plt, 'projeção_aritmética')
        plt = self.criaGráfico('Projeção Geométrica', self.y_PG_projeção)
        self.salva_imagem(plt, 'projeção_geométrica')

    def cria_e_salva_TD(self):
        plt = self.criaGráfico('Taxa Decrescente', self.y_TD_projeção)
        self.salva_imagem(plt, 'taxa_decrescente')

    def cria_e_salva_CL(self):
        plt = self.criaGráfico('Crescimento Logístico', self.y_CL_projeção)
        self.salva_imagem(plt, 'crescimento_logistico')        
    
    def cria_e_salva_graficos(self):
        self.cria_e_salva_PAPG()
        self.cria_e_salva_TD()
        self.cria_e_salva_CL()

    def cria_e_salva_graficos_PAPG(self):
        self.cria_e_salva_PAPG()

    def cria_e_salva_graficos_PAPGTD(self):
        self.cria_e_salva_PAPG()
        self.cria_e_salva_TD()

    def cria_e_salva_graficos_PAPGCL(self):
        self.cria_e_salva_PAPG()
        self.cria_e_salva_CL()

    def deleta_projeções(self):
        from project.models import ProjeçãoPopulacional
        for imagem in ProjeçãoPopulacional.objects.all():
            imagem.delete()

    def carrega_projeções(self):
        from project.models import ProjeçãoPopulacional
        d = dict( (img.imagem.name.replace('.png', ''), img) 
            for img in ProjeçãoPopulacional.objects.all())
        self.out = dict(self.out, **d)


class Verificações():
    __slots__=()

    def verificação(self):
        self.is_projetavél = True
        
        if self.checaTemposRepetidos():
            self.is_projetavél = False
            self.make_out()
        else:
            if self.checaTD(self.P0, self.P1, self.P2) and self.checaCL(self.P0, self.P1, self.P2):            
                self.projetar()
                print('$$$$ self.projetar()')
            elif self.checaTD(self.P0, self.P1, self.P2) == True:        
                self.projetar_PAPGTD()
                print('$$$$ self.projetar_PAPGTD()')
            elif self.checaCL(self.P0, self.P1, self.P2) == True:                
                self.projetar_PAPGCL()
                print('$$$$ self.projetar_PAPGCL()')
            else:                
                self.projetar_PAPG()
                print('$$$$ self.projetar_PAPG()')
    
    def checaTemposRepetidos(self):
        lista_tempos = [self.t0, self.t1, self.t2, self.t3, self.t4, self.t5]
        return any(i for i in lista_tempos if lista_tempos.count(i) > 1)

    @classmethod
    def checaCL(self, P0, P1, P2):
        try:
            Ps = self.fPs(P0, P1, P2)
            if P0 > P1 > P2:        
                return False
            elif not P0*P2 < P1**2:
                return False
            elif self.fK1ArgLog(P0, P1, Ps) < 0:
                return False
            else:
                return True
        except:
            return False

    @classmethod
    def checaTD(self, P0, P1, P2):
        try:            
            Ps = self.fPs(P0, P1, P2)
            if P0*P2==P1**2:
                return False
            elif self.fKdArgLog(Ps, P0, P2) < 0:
                return False
            else:
                return True
        except:
            return False


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
            if key not in ['Ka', 'Kb', 'Kd', 'K1', 'Kg', 'c'] and type(self.out[key]) == float:
                self.out[key] = int(self.out[key]) 

class PP_Main():
    __slots__=()

    def projetar(self):        
        self.foi_dimensionado = 'TUDO'
        self.inicializaConstantesDasCurvas()  
        self.incializaCensoProjeção()
        self.calculaPopulações()
        self.preenche_y_projeçõe()
        self.deleta_projeções()
        self.cria_e_salva_graficos()
        self.make_out()
        self.arredondamento()
        self.carrega_projeções()
        
    def projetar_PAPG(self):    
        self.foi_dimensionado = 'PAPG'    
        self.inicializaConstantesDasCurvasPAPG()
        self.incializaCensoProjeção()
        self.calculaPopulaçõesPAPG()
        self.preenche_y_projeçõe(key='PAPG')
        self.deleta_projeções()
        self.cria_e_salva_graficos_PAPG()
        self.make_out()
        self.arredondamento()
        self.carrega_projeções()        

    def projetar_PAPGTD(self):        
        self.foi_dimensionado = 'PAPGTD'
        self.inicializaConstantesDasCurvasPAPGTD()
        self.incializaCensoProjeção()
        self.calculaPopulaçõesPAPGTD()
        self.preenche_y_projeçõe(key='PAPGTD')
        self.deleta_projeções()
        self.cria_e_salva_graficos_PAPGTD()
        self.make_out()
        self.arredondamento()
        self.carrega_projeções()
        
    def projetar_PAPGCL(self):        
        self.foi_dimensionado = 'PAPGCL'
        self.inicializaConstantesDasCurvasPAPGCL()
        self.incializaCensoProjeção()
        self.calculaPopulaçõesPAPGCL()
        self.preenche_y_projeçõe(key='PAPGCL')
        self.deleta_projeções()
        self.cria_e_salva_graficos_PAPGCL()
        self.make_out()
        self.arredondamento()
        self.carrega_projeções()        


def factory_PP(ppinit):
	global ppresults

	d=dict(ppinit, **ppresults)

	class PP(PP_Methods, PP_Parte1, PP_Parte2, PP_Parte3,
	            PP_Parte4, Verificações, Extras, PP_Main):
	    __slots__ = [key for key in d]
	    def __init__(self):
	        for key in d:
	            setattr(self, key, d[key])
	return PP


def dynamic_name_image():
    return 'name_of_image' + str(time.time()).replace('.','_') + '.png'

def create_image():
    x = random.sample(range(1,9), 3)
    y = random.sample(range(1,9), 3)
    plt.axis([0, 10, 0, 10])
    plt.plot(x, y, 'o')

    f = BytesIO()
    plt.savefig(f, format="png")

    content_file = File(f)
    model_object = ProjeçãoPopulacional()
    model_object.imagem.save(dynamic_name_image(), content_file)
    model_object.save()
    plt.close()



"""
def fexemplo(x, y): 
    
    l = list(np.arange(0, 10, 0.1))
    a = [y*t for t in l]

    plt.plot(l, a, 'o', color='r')
    plt.axis([0, 10, 0, 20])
    #return plt

    # Truque para mudar o lugar onde a figura será criada.
    initial_path = os.getcwd()
    path = 'project/static/crescimento_populacional/'
    os.chdir(path)

    plt.savefig('nome_figura.png')
    plt.close()
    #plt.show()

    # Não sei se isso é realmente necessario.
    os.chdir(initial_path)
"""