# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    
    url(r'^inputs_bhaskara', views.inputs_bhaskara, name="inputs_bhaskara"),
    url(r'^results_bhaskara/', views.results_bhaskara, name='results_bhaskara'),    
	
    url(r'^inputs_triangulo', views.inputs_triangulo, name="inputs_triangulo"),
    url(r'^results_triangulo/', views.results_triangulo, name='results_triangulo'),    
    url(r'^pdf_view/', views.pdf_view, name='pdf_view'),    

	url(r'^inputs_fator_de_atrito/', views.inputs_fator_de_atrito, name="inputs_fator_de_atrito"),
	url(r'^results_fator_de_atrito/', views.results_fator_de_atrito, name='results_fator_de_atrito'),	
        

#	url(r'^inputs_viscosidade_absoluta/', views.inputs_viscosidade_absoluta, name="inputs_viscosidade_absoluta"),
#	url(r'^results_viscosidade_absoluta/', views.results_viscosidade_absoluta, name='results_viscosidade_absoluta'),	

#	url(r'^inputs_densidade_água/', views.inputs_densidade_água, name="inputs_densidade_água"),
#	url(r'^results_densidade_água/', views.results_densidade_água, name='results_densidade_água'),	


    url(r'^inputs_crescimento_populacional', views.inputs_crescimento_populacional, name='inputs_crescimento_populacional'),
    url(r'^results_crescimento_populacional/', views.results_crescimento_populacional, name='results_crescimento_populacional'),


	url(r'^inputs_vazões_água/', views.inputs_vazões_água, name='inputs_vazões_água'),
   	url(r'^results_vazões_água/', views.results_vazões_água, name='results_vazões_água'),

	url(r'^inputs_vertedor/', views.inputs_vertedor, name='inputs_vertedor'),
   	url(r'^results_vertedor/', views.results_vertedor, name='results_vertedor'),

    url(r'^inputs_calha_parshall', views.inputs_calha_parshall, name="inputs_calha_parshall"),
    url(r'^results_calha_parshall/', views.results_calha_parshall, name='results_calha_parshall'),

    url(r'^inputs_floculador_chicaneado', views.inputs_floculador_chicaneado, name="inputs_floculador_chicaneado"),
    url(r'^results_floculador_chicaneado/', views.results_floculador_chicaneado, name='results_floculador_chicaneado'),

    url(r'^inputs_decantador_alta_taxa', views.inputs_decantador_alta_taxa, name="inputs_decantador_alta_taxa"),
    url(r'^results_decantador_laminar/', views.results_decantador_laminar, name="results_decantador_laminar"),	
	url(r'^results_decantador_laminar_complete/', views.results_decantador_laminar_complete, name="results_decantador_laminar_complete"),

	url(r'^inputs_filtro_rápido_descendente', views.inputs_filtro_rápido_descendente, name="inputs_filtro_rápido_descendente"),	
	url(r'^results_filtro_rápido_descendente', views.results_filtro_rápido_descendente, name="results_filtro_rápido_descendente"),


	url(r'^inputs_vazões_esgoto/', views.inputs_vazões_esgoto, name='inputs_vazões_esgoto'),
   	url(r'^results_vazões_esgoto/', views.results_vazões_esgoto, name='results_vazões_esgoto'),
	
	url(r'^inputs_tratamento_preliminar/', views.inputs_tratamento_preliminar, name='inputs_tratamento_preliminar'),
   	url(r'^results_tratamento_preliminar/', views.results_tratamento_preliminar, name='results_tratamento_preliminar'),

	url(r'^inputs_tratamento_preliminar/', views.inputs_tratamento_preliminar, name='inputs_tratamento_preliminar'),
   	url(r'^results_tratamento_preliminar/', views.results_tratamento_preliminar, name='results_tratamento_preliminar'),

	url(r'^inputs_decantador_dortmund/', views.inputs_decantador_dortmund, name='inputs_decantador_dortmund'),
   	url(r'^results_decantador_dortmund/', views.results_decantador_dortmund, name='results_decantador_dortmund'),

	url(r'^inputs_decantador_primário/', views.inputs_decantador_primário, name='inputs_decantador_primário'),
   	url(r'^results_decantador_primário/', views.results_decantador_primário, name='results_decantador_primário'),

	url(r'^inputs_lagoa_facultativa/', views.inputs_lagoa_facultativa, name='inputs_lagoa_facultativa'),
   	url(r'^results_lagoa_facultativa/', views.results_lagoa_facultativa, name='results_lagoa_facultativa'),

	url(r'^inputs_lagoa_de_maturação/', views.inputs_lagoa_de_maturação, name='inputs_lagoa_de_maturação'),
   	url(r'^results_lagoa_de_maturação/', views.results_lagoa_de_maturação, name='results_lagoa_de_maturação'),

	url(r'^inputs_uasb', views.inputs_uasb, name="inputs_uasb"),
	url(r'^results_uasb', views.results_uasb, name="results_uasb"),	

	url(r'^inputs_lodos_ativados/', views.inputs_lodos_ativados, name='inputs_lodos_ativados'),
   	url(r'^results_lodos_ativados/', views.results_lodos_ativados, name='results_lodos_ativados'),
]
