import math

def f(x):
    """Funcion principal"""
    return -2 + 7*x - 5*x**2 + 6*x**3

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