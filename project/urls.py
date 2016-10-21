# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^results_bhaskara/', views.results_bhaskara, name='results_bhaskara'),
    url(r'^inputs_bhaskara', views.inputs_bhaskara, name="inputs_bhaskara"),
    url(r'^inputs_calha_parshall', views.inputs_calha_parshall, name="inputs_calha_parshall"),
]
