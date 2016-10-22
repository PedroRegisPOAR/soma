# -*- coding: utf-8 -*-
from django.shortcuts import render

from project.bhaskara.bhaskara import Bhaskara

#from project.bhaskara.bhaskara import Bhaskara

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
        eq_bhaskara.roots()
        r1=eq_bhaskara.r1
        r2=eq_bhaskara.r2

        dic={"a":a, "b":b, "c":c, "r1":r1, "r2":r2}
        
    else:
        inputs_bhaskara(request)        
#    return render(request,'personal/resultado.html', dic)
    return render(request,'project/bhaskara/results_bhaskara.html', dic)


#   Coisas da Calha Parshall


def inputs_calha_parshall(request):     
    return render(request,'project/calha_parshall/inputs_calha_parshall.html')


def results_calha_parshall(request):

#    if request.method == "POST":
#        Q=int(request.POST["Q"])
#        g=int(request.POST["g"])
#        T=int(request.POST["T"])

#        cp=Bhaskara(a,b,c)
#        cp.dimensiona()

#        dic={"a":a, "b":b, "c":c, "r1":r1, "r2":r2}
        
#    else:
#        inputs_calha_parshall(request)
#    return render(request,'project/calha_parshall/results_calha_parshall.html', dic)    
    return render(request,'project/calha_parshall/results_calha_parshall.html')    

