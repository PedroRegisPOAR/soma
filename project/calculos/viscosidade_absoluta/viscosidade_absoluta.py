
def viscosidade_absoluta(T):
    a = 2.414*10**(-5)
    b = 247.8
    c = 140 - 273.15 # Conversão para graus Celsius
    return a*10**(b/(T - c)) 