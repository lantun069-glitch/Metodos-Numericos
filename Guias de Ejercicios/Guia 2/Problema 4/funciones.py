import math

def f(x):
    """Funcion f(x) = (10-2x)(16-2x)x - 100"""
    return (10 - 2*x) * (16 - 2*x) * x - 100

def df_dx(x):
    """Derivada de f(x) = 160x - 104x^2 + 4x^3 - 100"""
    return 160 - 104*x + 12*x**2

def calcular_error(x_nuevo, x_anterior, tipo_error):
    if tipo_error.lower() == 'absoluto':
        return abs(x_nuevo - x_anterior)
    elif tipo_error.lower() == 'porcentual':
        if x_nuevo == 0:
            return float('inf')
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100
    else:
        raise ValueError("Tipo de error debe ser 'absoluto' o 'porcentual'")