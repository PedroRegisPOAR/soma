import unittest

import numpy as np

#from projeção_populacional import factory_PP
#from projeção_populacional import PP_Parte4

import random
import matplotlib 

from project.models import ProjeçãoPopulacional
from io import StringIO, BytesIO
from django.core.files import File

# http://stackoverflow.com/questions/27147300/how-to-clean-images-in-python-django
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def salva_imagem(plt, name):
	f = BytesIO()
	plt.savefig(f, format="png")
	content_file = File(f)
	model_object = ProjeçãoPopulacional()
	model_object.imagem.save(name + '.png', content_file)
	model_object.save()
	plt.close()

def cria_imagem():
	x = random.sample(range(1,9), 3)
	y = random.sample(range(1,9), 3)
	plt.axis([0, 10, 0, 10])
	plt.plot(x, y, 'o')

	return plt


def salva_projeções():
	plt1 = cria_imagem()
	salva_imagem(plt1, 'plt1')
	
	plt2 = cria_imagem()
	salva_imagem(plt2, 'plt2')


	"""
	plt2 = cria_imagem()
	salva_imagem(plt2, 'plt2')

	plt3 = cria_imagem()
	salva_imagem(plt3, 'plt3')

	plt4 = cria_imagem()
	salva_imagem(plt4, 'plt4')
	"""


	

