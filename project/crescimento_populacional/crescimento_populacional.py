
import matplotlib.pyplot as plt


def fexemplo(x, y):
	plt.plot([x], [y], 'o')
	plt.axis([0, 10, 0, 20])
	plt.savefig('nome_figura.png')
	#plt.show()