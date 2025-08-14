import math

def f(C):
    """Ecuacion: C*cosh(12/C) - C - 5 = 0"""
    return C * math.cosh(12/C) - C - 5

def df_dx(C):
    """Derivada de f(C)"""
    return math.cosh(12/C) - (12/C) * math.sinh(12/C) - 1

def calcular_error(x_nuevo, x_anterior, tipo_error):
    if tipo_error == 'absoluto':
        return abs(x_nuevo - x_anterior)
    return abs((x_nuevo - x_anterior) / x_nuevo) * 100