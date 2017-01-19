import os
#import matplotlib.pyplot as plt




def fexemplo(x, y):
	plt.plot([x], [y], 'o')
	plt.axis([0, 10, 0, 20])

	return plt
	
	"""
	# Truque para mudar o lugar onde a figura será criada.
	initial_path = os.getcwd()
	path = 'project/templates/project/crescimento_populacional/'
	os.chdir(path)
	plt.savefig('nome_figura.png')
	#plt.show()

	# Não sei se isso é realmente necessario.
	os.chdir(initial_path)
	"""