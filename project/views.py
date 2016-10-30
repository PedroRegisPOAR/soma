# -*- coding: utf-8 -*-
from django.shortcuts import render

from project.bhaskara.bhaskara import Bhaskara
from project.calha_parshall.calha_parshall import CalhaParshall
from project.decantador_laminar.decantador_laminar import DecantadorLaminar


# Create your views here.


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


#   Coisas da Calha Parshall
def inputs_calha_parshall(request):     
    return render(request,'project/calha_parshall/inputs_calha_parshall.html')


def results_calha_parshall(request):

    if request.method == "POST":

#        Q=float(request.POST.get("Q", False))
#        g=float(request.POST.get("g", False))
#        T=float(request.POST.get("T", False))
#        GmMin=float(request.POST.get("GmMin", False))
#        GmMax=float(request.POST.get("GmMax", False))
#        FMin=float(request.POST.get("FMin", False))


        Q=float(request.POST["Q"])
        g=float(request.POST["g"])
        T=float(request.POST["T"])
        GmMin=float(request.POST["GmMin"])
        GmMax=float(request.POST["GmMax"])
        FMin=float(request.POST["FMin"])
        

        Q1=0.05
        g1=9.8
        T1=17.5
        GmMin1=1050
        GmMax1=2000
        FMin1=4.5

#        cp=CalhaParshall(Q1, g1, T1, GmMin1, GmMax1, FMin1)
#        cp.dimensiona_inteligente()

        cp=CalhaParshall(Q, g, T, GmMin, GmMax, FMin)
        cp.dimensiona_inteligente()
        
        # TO Do. A operação d=dict(cp.d) não funciona porque no dicionario não 
        # apenas numeros, mas matrizes

        d=cp.d

#        d={"Q":Q, "g":g, "T":T, "GmMin":GmMin, "GmMax":GmMax, "FMin":FMin}
#        d={"Q":Q, "g":g, "T":T, "W":cp.W, "mu":cp.mu, "rho":cp.rho, "C":cp.C,
 #       "D":cp.D, "K":cp.K, "N":cp.N, "k":cp.k, "n":cp.n, 
 #       "H0":cp.H0, "D0":cp.D0, "U0":cp.U0, "q":cp.q,
 #       "E0":cp.E0, "U1":cp.U1, "h1":cp.h1, "F1":cp.F1, 
 #       "h2":cp.h2,"h3":cp.h3, "U3":cp.U3, "L":cp.L,
 #        "h":cp.h, "Tm":cp.Tm, "Gm":cp.Gm}

#        if cp.dimensionado_ok:
#            pass
#        for key in d:
#            d[key]=round(d[key],4)
    else:
        inputs_calha_parshall(request)
    return render(request,'project/calha_parshall/results_calha_parshall.html', d)    

def inputs_decantador_laminar(request):     
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
