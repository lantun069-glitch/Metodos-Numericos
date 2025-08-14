import math

def calcular_error(x_nuevo, x_anterior, tipo_error):
    if tipo_error.lower() == 'absoluto':
        return abs(x_nuevo - x_anterior)
    else:
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100

def g1(x):
    return x**5 - 3*x**3 - 2*x**2 + 2

def g2(x):
    return math.cos(math.sin(x))

def g3(x):
    return x**(x - math.cos(x))