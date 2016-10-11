from django.shortcuts import render

from personal.contas.soma import minhasoma

from personal.contas.bhaskara import Bhaskara
#from personal.contas.bhaskara import *

# Create your views here.


def index(request):
    return render(request, 'personal/home.html')


def contas(request):
    res=0
    if request.method == "POST":
        a=int(request.POST["a"])
        b=int(request.POST["b"])
        c=int(request.POST["c"])

        res=minhasoma(a, b)
        res2=minhasoma(a, b)
        r={"res":res, "res2":res2}
        l=[1,2]
#        dic={"k1":(-1)**(1/2), "k2":2}

        eq_bhaskara=Bhaskara(a,b,c)
        eq_bhaskara.roots()
        r1=eq_bhaskara.r1
        r2=eq_bhaskara.r2

        dic={"a":a, "b":b, "c":c, "r1":r1, "r2":r2}
        
        
    else:
        index(request)
        
    return render(request,'personal/resultado.html', dic)
