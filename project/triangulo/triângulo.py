"""
http://blog.livecoding.tv/2016/08/19/python-como-chamar-um-comando-externo/
http://stackoverflow.com/questions/8085520/generating-pdf-latex-with-python-script
http://stackoverflow.com/questions/19683123/compile-latex-from-python

Bom
http://stackoverflow.com/questions/4519736/how-to-run-a-standalone-application-from-the-current-one
"""
def generate_pdf(pdfname, d):
    import subprocess
    
    write_variables('contantes', d)
    
    subprocess.call('pdflatex ' + pdfname + '.tex')


def write_variables(fname, d):
    f = open(fname + '.tex', 'w')
    for key in d:
        line = newcommand(key, d[key])
        f.write(line)
    f.close()

def newcommand(name, value):
    return '\\newcommand{\\nc' + name + '}{' + value + '} \n'

#d = {'a':'123','b':'456'}
#write_variables('contantes', d)
#pdfname="ex03"
#generate_pdf(pdfname, d)
