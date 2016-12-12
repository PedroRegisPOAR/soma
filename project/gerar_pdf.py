import os
import subprocess

def write_variables(path, fname, d):
    f = open(path +fname + '.tex', 'w')
    for key in d:
        line = newcommand(key, d[key])
        f.write(line)
    f.close()

def newcommand(name, value):
    return '\\newcommand{\\nc' + name + '}{' + value + '} \n'


def gerar_pdf(path, pdf_name, d):
    fname = 'constantes'
    write_variables(path, fname, d)
    os.chdir(path)
    subprocess.call('pdflatex ' + pdf_name + '.tex')


path = 'templates\\project\\triângulo\\'
pdf_name = 'gerar_pdf_triangulo'
d = { 'a':'12'}

gerar_pdf(path, pdf_name, d)
