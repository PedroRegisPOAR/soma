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
]
