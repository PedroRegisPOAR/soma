# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^inputs_bhaskara', views.inputs_bhaskara, name="inputs_bhaskara"),
    url(r'^results_bhaskara/', views.results_bhaskara, name='results_bhaskara'),    
    url(r'^inputs_calha_parshall', views.inputs_calha_parshall, name="inputs_calha_parshall"),
    url(r'^results_calha_parshall/', views.results_calha_parshall, name='results_calha_parshall'),
    url(r'^inputs_decantador_laminar', views.inputs_decantador_laminar, name="inputs_decantador_laminar"),
    url(r'^results_decantador_laminar/', views.results_decantador_laminar, name="results_decantador_laminar"),	
	url(r'^results_decantador_laminar_complete/', views.results_decantador_laminar_complete, name="results_decantador_laminar_complete"),
	url(r'^inputs_fator_de_atrito/', views.inputs_fator_de_atrito, name="inputs_fator_de_atrito"),
	url(r'^results_fator_de_atrito/', views.results_fator_de_atrito, name='results_fator_de_atrito'),
]
