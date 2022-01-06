import numpy as np
from scipy.optimize import fmin


def error_func(abgamma, x, L):
    a, b, gamma = abgamma
    Lexpect = b + a*x**gamma
    return np.sum((Lexpect - L)**2)


def estimate_gamma(x, L):
    return fmin(error_func, [0, 1, 2], args=(x, L))[-1]
    
Gama_Encontrado = estimate_gamma([x for x in range(0, 255,10)],['''COLOQUE AQUI OS VALORES OUTPUT ANTES DA LINEARIZAÇÃO'''])

#O valor gama encontrado será colocado dentro da variável 'Gama_Encontrado'


