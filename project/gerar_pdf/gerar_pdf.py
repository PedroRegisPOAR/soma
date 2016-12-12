import os
import subprocess

from django.conf import settings

#   http://stackoverflow.com/questions/431684/how-do-i-cd-in-python/13197763#13197763


def write_variables(path, fname, d):
    s = 'soma/project/templates/project/triangulo/'    
    f = open(s + fname + '.tex', 'w')
#    f = open(os.path.join(os.path.dirname(__file__), fname + '.tex'), 'w')
    
    for key in d:
        line = newcommand(key, d[key])
        f.write(line)
    f.close()

def newcommand(name, value):
    return '\\newcommand{\\nc' + name + '}{' + value + '} \n'


def gerar_pdf(path, pdf_name, d):
    
    initial_path = os.getcwd()

    fname = 'constantes'
    write_variables(path, fname, d)
#    os.chdir(path)
#    os.chdir('project/templates/project/triangulo')

#    os.chdir(os.path.join(os.path.dirname(__file__)))
#    subprocess.call('pdflatex ' + pdf_name + '.tex')
    subprocess.call(['pdflatex', pdf_name])    
#    subprocess.check_call('pdflatex ' + pdf_name + '.tex')
    
    os.chdir(initial_path)

