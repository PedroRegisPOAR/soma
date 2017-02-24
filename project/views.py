# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from project.calculos.bhaskara.bhaskara import Bhaskara
from project.calculos.fator_de_atrito.fator_atrito_colebrock import solução_Colebrook_White

from project.calculos.densidade_água.densidade_água import densidade_água
from project.calculos.viscosidade_absoluta.viscosidade_absoluta import viscosidade_absoluta

from project.calculos.gerar_pdf.gerar_pdf import gerar_pdf
from project.calculos.calha_parshall.calha_parshall import factory_CP, cpinit
from project.calculos.decantador_laminar.decantador_laminar import DecantadorLaminar
from project.calculos.uasb.uasb import factory_UASB, uasb_dict_inputs
from project.calculos.floculador_chicaneado.floculador_chicaneado import factory_FloculadorChicaneado, dict_inputs_FloculadorChicaneado

from . models import ProjeçãoPopulacional

from project.calculos.projeção_populacional.projeção_populacional import (
    factory_PP, ppinit)

from project.calculos.vazões_esgoto.vazões_esgoto import factory_VE, veinit
from project.calculos.vazões_água.vazões_água import factory_VA, vainit

def index(request):
    return render(request, "project/home.html")


def inputs_bhaskara(request):     
    return render(request,'project/bhaskara/inputs_bhaskara.html')

def results_bhaskara(request):
    if request.method == "POST":
        a=int(request.POST["a"])
        b=int(request.POST["b"])
        c=int(request.POST["c"])

        eq_bhaskara=Bhaskara(a,b,c)
        eq_bhaskara.calculate_roots()
        dic=eq_bhaskara.out
    else:
        inputs_bhaskara(request)        
    return render(request,'project/bhaskara/results_bhaskara.html', dic)


def inputs_triangulo(request):     
    return render(request,'project/triangulo/inputs_triangulo.html')

def results_triangulo(request):
    if request.method == "POST":
        a=str(request.POST["a"])
        b=str(request.POST["b"])
        c=str(request.POST["c"])

        d = {'a':a,'b':b, 'c':c}
#        d = { 'a':'12'}

#        generate_pdf('ex03', d)
        path = 'project\\templates\\project\\triangulo\\'
        pdf_name = 'gerar_pdf_triangulo'
        d = { 'a':'12'}
        gerar_pdf(path, pdf_name, d)


#        gerar_pdf(path, pdf_name, None)
#        dic=eq_bhaskara.out
    else:
        inputs_triangulo(request)        
    return render(request,'project/triangulo/results_triangulo.html')

#   http://stackoverflow.com/questions/11779246/how-to-show-a-pdf-file-in-a-django-view/29718326#29718326
def pdf_view(request):
    a=str(request.POST["a"])
    b=str(request.POST["b"])
    c=str(request.POST["c"])

    d = {'a':a,'b':b, 'c':c}

    pdf_name = 'gerar_pdf_triangulo'
    path = 'soma/project/templates/project/triangulo/'
    gerar_pdf(path, pdf_name, d)
    
    s = 'soma/project/templates/project/triangulo/gerar_pdf_triangulo.pdf'
#    s = 'project/templates/project/triangulo/gerar_pdf_triangulo.pdf'
    with open(s, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=some_file.pdf'
        return response


def inputs_fator_de_atrito(request):     
    return render(request,'project/fator_de_atrito/inputs_fator_de_atrito.html')

def results_fator_de_atrito(request):
    if request.method == "POST":
        epsilon=float(request.POST["epsilon"])
        Re=float(request.POST["Re"])
        D=float(request.POST["D"])

        d=solução_Colebrook_White(epsilon, Re, D)
    else:
        inputs_fator_de_atrito(request)
    return render(request,'project/fator_de_atrito/results_fator_de_atrito.html', d)    



def inputs_densidade_água(request):     
    return render(request,'project/densidade_água/inputs_densidade_água.html')


def results_densidade_água(request):
    if request.method == "POST":
        T = float(request.POST['T'])
        rho = round(densidade_água(T), 3)
        d = {'rho':rho, 'T':T}
    else:
        inputs_projeção_populacional(request)
    return render(request, 'project/densidade_água/results_densidade_água.html', d)


def inputs_viscosidade_absoluta(request):     
    return render(request,'project/viscosidade_absoluta/inputs_viscosidade_absoluta.html')


def results_viscosidade_absoluta(request):
    if request.method == "POST":
        T = float(request.POST['T'])
        mu = round(viscosidade_absoluta(T), 7)
        d = {'mu':mu, 'T':T}
    else:
        inputs_viscosidade_absoluta(request)
    return render(request, 'project/viscosidade_absoluta/results_viscosidade_absoluta.html', d)




def inputs_projeção_populacional(request):     
    return render(request,'project/projeção_populacional/inputs_projeção_populacional.html')

"""
def results_projeção_populacional(request):
    
    for plt in ProjeçãoPopulacional.objects.all():
        plt.delete()

    create_image()

    last_plot = ProjeçãoPopulacional.objects.latest('id')
    context = {'last_plot':last_plot}

    return render(request,'project/projeção_populacional/results_projeção_populacional.html', context)
"""

def results_projeção_populacional(request):

    path_page = 'project/projeção_populacional/results_projeção_populacional.html'

    if request.method == "POST":
        for key in ppinit:
            ppinit[key]=float(request.POST[key])
        PP=factory_PP(ppinit)
        pp=PP()
        #pp.projetar()      
        pp.verificação()
        
        c = {}
        projeções =  ProjeçãoPopulacional.objects.all()
        for p in []:
            if p.imagem.name == 'projeção_aritmética.png':
                c.update({'projeção_aritmética2':p})
            elif p.imagem.name == 'projeção_geométrica.png':
                c.update({'projeção_geométrica':p.imagem})
            elif p.imagem.name == 'taxa_decrescente.png':
                c.update({'taxa_decrescente':p.imagem})
            elif p.imagem.name == 'crescimento_logístico.png':
                c.update({'crescimento_logístico':p.imagem})
        
        c.update({'is_projetavél':True})
        c.update({'foi_dimensionado':'TUDO'})
        
        ultimos =  ProjeçãoPopulacional.objects.order_by('-id')[:4]
        
        c.update({'crescimento_logístico':ultimos[0].imagem})
        c.update({'taxa_decrescente':ultimos[1].imagem})
        c.update({'projeção_geométrica':ultimos[2].imagem})
        c.update({'projeção_aritmética':ultimos[3].imagem})
    
        d = dict(pp.out, **c)
    else:
        inputs_projeção_populacional(request)

    return render(request, path_page, d)


"""
def results_projeção_populacional(request):
    #path_imagem = 'project/static/projeção_populacional/'

    path_imagem = 'project/templates/project/projeção_populacional/'
    
    path_page = 'project/projeção_populacional/results_projeção_populacional.html'

    if request.method == "POST":
        for key in ppinit:
            ppinit[key]=float(request.POST[key])
        PP=factory_PP(ppinit)
        pp=PP()
        #Se eu comentar essa linha funciona no pythonanywhere
        pp.projetar(path_imagem)      

    else:
        inputs_projeção_populacional(request)

    return render(request, path_page)
"""

'''
def results_projeção_populacional(request):
    path_imagem = 'project/static/projeção_populacional/'
    path_page = 'project/projeção_populacional/results_projeção_populacional.html'
    
    if request.method == "POST":
        for key in ppinit:
            ppinit[key]=float(request.POST[key])
        PP=factory_PP(ppinit)
        pp=PP()
        #Se eu comentar essa linha funciona no pythonanywhere
        #pp.projetar(path_imagem)      

    else:
        inputs_projeção_populacional(request)

    return render(request, path_page)
'''

"""    
def results_projeção_populacional(request):
    path_imagem = 'static/projeção_populacional/nome_figura.png'
    #image_data = open(path, "rb").read()
    #return HttpResponse(image_data, content_type="image/png")
    #d = {"imagem":image_data}
    path_page = 'project/projeção_populacional/results_projeção_populacional.html'
    return render(request, path_page, {"imagem":path_imagem})
"""


def inputs_fator_de_atrito(request):     
    return render(request,'project/viscosidade_absoluta/inputs_fator_de_atrito.html')
    

def inputs_vazões_água(request):     
    return render(request,'project/vazões_água/inputs_vazões_água.html')

def results_vazões_água(request):
    if request.method == "POST":
        for key in vainit:
            vainit[key] = float(request.POST[key])
        VA = factory_VA(vainit)
        va = VA()
        va.calcular()
        d = va.out        
    else:
        inputs_vazões_água(request)        
    return render(request,'project/vazões_água/results_vazões_água.html', d)


def inputs_vertedor(request):       
    return render(request,'project/vertedor/inputs_vertedor.html')

def results_vertedor(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_vertedor(request)        
    return render(request,'project/vertedor/results_vertedor.html', d)

def inputs_calha_parshall(request):     
    return render(request,'project/calha_parshall/inputs_calha_parshall.html')


def results_calha_parshall(request):

    if request.method == "POST":
        for key in cpinit:
            if key == 'iW':
                cpinit[key] = int(request.POST[key])
            else:
                cpinit[key] = float(request.POST[key])

        CP = factory_CP(cpinit)
        cp = CP()
        cp.dimensionar()
        d = cp.out
    else:
        inputs_calha_parshall(request)
    return render(request,'project/calha_parshall/results_calha_parshall.html', d)    


def inputs_floculador_chicaneado(request):     
    return render(request,'project/floculador_chicaneado/inputs_floculador_chicaneado.html')

def results_floculador_chicaneado(request):
    if request.method == "POST":
        for key in dict_inputs_FloculadorChicaneado:
            dict_inputs_FloculadorChicaneado[key]=float(request.POST[key])

        FloculadorChicaneado = factory_FloculadorChicaneado(dict_inputs_FloculadorChicaneado)
        fc = FloculadorChicaneado()
        fc.dimensionar()      
        d = fc.out
    else:
        inputs_floculador_chicaneado(request)        
    return render(request,'project/floculador_chicaneado/results_floculador_chicaneado.html', d)


def inputs_decantador_alta_taxa(request):     
    return render(request,'project/decantador_laminar/inputs_decantador_laminar.html')

def results_decantador_laminar(request):
    if request.method == "POST":

        Q       =float(request.POST["Q"])
        theta   =float(request.POST["theta"]) 
        Vs      =float(request.POST["Vs"])
        l       =float(request.POST["l"])
        w       =float(request.POST["w"])
        APoço   =float(request.POST["APoço"])
        NUnid   =float(request.POST["NUnid"])
        Sc      =float(request.POST["Sc"])

        nu          =None
        ql          =None
        Esp         =None
        NPoçosAdot  =None
        LDec        =None
        BDec        =None
        arred       =None

        dl=DecantadorLaminar(Q, Vs, l, w, theta, NUnid, Sc, nu, ql,
        Esp, APoço, NPoçosAdot, LDec, BDec, arred)
        dl.pré_dimensionar()
        d=dl.out
    else:
        inputs_decantador_laminar(request)
    return render(request,'project/decantador_laminar/results_decantador_laminar.html', d)    


def results_decantador_laminar_complete(request):
    if request.method == "POST":
        Q           =float(request.POST["Q"])
        theta       =float(request.POST["theta"]) 
        Vs          =float(request.POST["Vs"])
        l           =float(request.POST["l"])
        w           =float(request.POST["w"])
        APoço       =float(request.POST["APoço"])
        NUnid       =float(request.POST["NUnid"])
        Sc          =float(request.POST["Sc"])

        nu          =float(request.POST["nu"])
        ql          =float(request.POST["ql"])
        Esp         =float(request.POST["Esp"])
        NPoçosAdot  =float(request.POST["NPoçosAdot"])
        LDec        =float(request.POST["LDec"])
        BDec        =float(request.POST["BDec"])
        arred       =float(request.POST["arred"])

        dl=DecantadorLaminar(Q, Vs, l, w, theta, NUnid, Sc, nu, ql,
        Esp, APoço, NPoçosAdot, LDec, BDec, arred)
        dl.dimensionar()
        d=dl.out
    else:
        inputs_decantador_laminar(request)
    return render(request,'project/decantador_laminar/results_decantador_laminar_complete.html', d)    


def inputs_filtro_rápido_descendente(request):     
    return render(request,'project/filtro_rápido_descendente/inputs_filtro_rápido_descendente.html')

def results_filtro_rápido_descendente(request):
    if request.method == "POST":
        d={}
        pass
    else:
        inputs_filtro_rápido_descendente(request)
    return render(request,'project/filtro_rápido_descendente/results_filtro_rápido_descendente.html', d)    




def inputs_vazões_esgoto(request):     
    return render(request,'project/vazões_esgoto/inputs_vazões_esgoto.html')

def results_vazões_esgoto(request):
    if request.method == "POST":
        for key in veinit:
            veinit[key] = float(request.POST[key])
        VE = factory_VE(veinit)
        ve = VE()
        ve.calcular()
        d = ve.out
    else:
        inputs_vazões_esgoto(request)        
    return render(request,'project/vazões_esgoto/results_vazões_esgoto.html', d)


def inputs_tratamento_preliminar(request):     
    return render(request,'project/tratamento_preliminar/inputs_tratamento_preliminar.html')

def results_tratamento_preliminar(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_tratamento_preliminar(request)        
    return render(request,'project/tratamento_preliminar/results_tratamento_preliminar.html', d)


def inputs_decantador_dortmund(request):     
    return render(request,'project/decantador_dortmund/inputs_decantador_dortmund.html')

def results_decantador_dortmund(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_decantador_dortmund(request)        
    return render(request,'project/decantador_dortmund/results_decantador_dortmund.html', d)


def inputs_decantador_primário(request):     
    return render(request,'project/decantador_primário/inputs_decantador_primário.html')

def results_decantador_primário(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_decantador_primário(request)        
    return render(request,'project/decantador_primário/results_decantador_primário.html', d)


def inputs_lagoa_facultativa(request):     
    return render(request,'project/lagoa_facultativa/inputs_lagoa_facultativa.html')

def results_lagoa_facultativa(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_lagoa_facultativa(request)        
    return render(request,'project/lagoa_facultativa/results_lagoa_facultativa.html', d)


def inputs_lagoa_de_maturação(request):     
    return render(request,'project/lagoa_de_maturação/inputs_lagoa_de_maturação.html')

def results_lagoa_de_maturação(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_lagoa_de_maturação(request)        
    return render(request,'project/lagoa_de_maturação/results_lagoa_de_maturação.html', d)


def inputs_uasb(request):     
    return render(request,'project/uasb/inputs_uasb.html')

def results_uasb(request):
    if request.method == "POST":
        '''
        args_uasb={
            "B":float(request.POST["B"]),
            "L":float(request.POST["L"]),
            "T":float(request.POST["T"]),
            "TDH":float(request.POST["TDH"]),
            "Qméd":float(request.POST["Qméd"]),
            "Qmáx":float(request.POST["Qmáx"]),
            "DQOaf":float(request.POST["DQOaf"]),
            "DBOaf":float(request.POST["DBOaf"]),
            "NMód":float(request.POST["NMód"]),
            "H":float(request.POST["H"]),
            "COVMáx":float(request.POST["COVMáx"]),
            "CHVMáx":float(request.POST["CHVMáx"]),
            "AInfTub":float(request.POST["AInfTub"]),
            "NTubAdot":float(request.POST["NTubAdot"]),
            "YObs":float(request.POST["YObs"]),
            "Y":float(request.POST["Y"]),
            "P":float(request.POST["P"]),
            "R":float(request.POST["R"]),
            "PCH4":float(request.POST["PCH4"]),
            "Vg":float(request.POST["Vg"]),
            "NCol":float(request.POST["NCol"]),
            "LAS":float(request.POST["LAS"]),
            "e":float(request.POST["e"]),
            "gamma":float(request.POST["gamma"]),
            "c":float(request.POST["c"])
            }
        '''
        
        '''
        args_uasb={
            "B":None,
            "L":None,
            "T":None,
            "TDH":None,
            "Qméd":None,
            "Qmáx":None,
            "DQOaf":None,
            "DBOaf":None,
            "NMód":None,
            "H":None,
            "COVMáx":None,
            "CHVMáx":None,
            "AInfTub":None,
            "NTubAdot":None,
            "YObs":None,
            "Y":None,
            "P":None,             
            "R":None,
            "PCH4":None,
            "Vg":None,
            "NCol":None,
            "LAS":None,
            "e":None,
            "gamma":None,
            "c":None
            }
        '''
        for key in uasb_dict_inputs:
            uasb_dict_inputs[key]=float(request.POST[key])


        UASB=factory_UASB(uasb_dict_inputs)
        u=UASB()
        u.dimensionar()      
        d=u.out
    else:
        inputs_uasb(request)
    return render(request,'project/uasb/results_uasb.html', d)    


def inputs_lodos_ativados(request):     
    return render(request,'project/lodos_ativados/inputs_lodos_ativados.html')

def results_lodos_ativados(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_lodos_ativados(request)        
    return render(request,'project/lodos_ativados/results_lodos_ativados.html', d)










