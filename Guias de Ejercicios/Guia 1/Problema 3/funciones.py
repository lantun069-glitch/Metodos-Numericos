import math

def f(m):
    """Ecuacion del paracaidista: f(m) = velocidad_calculada - velocidad_objetivo"""
    g = 9.81
    c = 14
    t = 7
    v_objetivo = 35 * (1000/3600)  # 35 km/h a m/s
    
    velocidad_calculada = (g * m / c) * (1 - math.exp(-c * t / m))
    return velocidad_calculada - v_objetivo

def calcular_error(x_nuevo, x_anterior, tipo_error):
    if tipo_error.lower() == 'absoluto':
        return abs(x_nuevo - x_anterior)
    elif tipo_error.lower() == 'porcentual':
        if x_nuevo == 0:
            return float('inf')
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100