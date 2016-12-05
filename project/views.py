# -*- coding: utf-8 -*-

from django.http import HttpResponse

from django.shortcuts import render

from project.bhaskara.bhaskara import Bhaskara
from project.fator_de_atrito.fator_atrito_colebrock import solução_Colebrook_White

from project.triângulo.triângulo import generate_pdf


from project.calha_parshall.calha_parshall import CalhaParshall
from project.decantador_laminar.decantador_laminar import DecantadorLaminar
from project.uasb.uasb import factory_UASB, uasb_dict_inputs

from project.floculador_chicaneado.floculador_chicaneado import factory_FloculadorChicaneado, dict_inputs_FloculadorChicaneado



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


def inputs_triângulo(request):     
    return render(request,'project/triângulo/inputs_triângulo.html')

def results_triângulo(request):
    if request.method == "POST":
        a=str(request.POST["a"])
        b=str(request.POST["b"])
        c=str(request.POST["c"])

#        d = {'a':a,'b':b, 'c':c}

#        generate_pdf('ex03', d)
#        dic=eq_bhaskara.out
    else:
        inputs_triângulo(request)        
    return render(request,'project/triângulo/results_triângulo.html')

#   http://stackoverflow.com/questions/11779246/how-to-show-a-pdf-file-in-a-django-view/29718326#29718326
def pdf_view(request):
    with open('project/templates/project/triângulo/triangulo.pdf', 'rb') as pdf:
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



def inputs_crescimento_populacional(request):     
    return render(request,'project/crescimento_populacional/inputs_crescimento_populacional.html')

def results_crescimento_populacional(request):
    if request.method == "POST":
        d = {}
    else:
        inputs_crescimento_populacional(request)        
    return render(request,'project/crescimento_populacional/results_crescimento_populacional.html', d)

#
def inputs_fator_de_atrito(request):     
    return render(request,'project/viscosidade_absoluta/inputs_fator_de_atrito.html')
    


def inputs_vazões_água(request):     
    return render(request,'project/vazões_água/inputs_vazões_água.html')

def results_vazões_água(request):
    if request.method == "POST":
        d = {}
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
        Q=float(request.POST["Q"])
        g=float(request.POST["g"])
        T=float(request.POST["T"])
        GmMin=float(request.POST["GmMin"])
        GmMax=float(request.POST["GmMax"])
        FMin=float(request.POST["FMin"])
        
        cp=CalhaParshall(Q, g, T, GmMin, GmMax, FMin)
        cp.dimensiona_inteligente()
        
        d=cp.d

#        if cp.dimensionado_ok:
#            pass
#        for key in d:
#            d[key]=round(d[key],4)
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
        d = {}
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









