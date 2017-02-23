

def densidade_água(T):
    t0 = 3.9818
    A = 7.0134*10**(-8)
    B = 7.926504*10**(-6)
    C = -7.575677*10**(-8)
    D = 7.314894*10**(-10)
    E = -3.596458*10**(-12)
    rho = 999.97358
    L = [A, B, C, D, E]
    soma = 0
    for i in range(len(L)):
        soma += L[i]*(T - t0)**(i + 1)

    return rho*(1 - soma)