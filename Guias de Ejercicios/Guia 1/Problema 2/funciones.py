import math

# Funcion principal
def f(x):
    """Funcion g(a) = a^10 - 1"""
    return x**10 - 1

def df_dx(x):
    """Derivada de f(x) = 10*x^9"""
    return 10 * x**9

def g(x):
    """Funcion g(x) para punto fijo"""
    return 4/x if x != 0 else 2

def calcular_error(x_nuevo, x_anterior, tipo_error):
    """Calcula el error segun el tipo especificado"""
    if tipo_error.lower() == 'absoluto':
        return abs(x_nuevo - x_anterior)
    elif tipo_error.lower() == 'porcentual':
        if x_nuevo == 0:
            return float('inf')
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100
    else:
        raise ValueError("Tipo de error debe ser 'absoluto' o 'porcentual'")