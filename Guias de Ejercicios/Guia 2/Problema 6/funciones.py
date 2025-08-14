import math

def f(d):
    """Funcion f(d) = 0 para encontrar profundidad de sumersion"""
    r = 10.0
    rho_madera = 0.638
    rho_agua = 1.0
    
    V_esfera = (4/3) * math.pi * r**3
    V_sumergido = math.pi * d**2 * (3*r - d) / 3
    
    return rho_madera * V_esfera - rho_agua * V_sumergido

def df_dx(d):
    """Derivada de f(d)"""
    r = 10.0
    return -math.pi * d * (2*r - d)

def calcular_error(x_nuevo, x_anterior, tipo_error):
    if tipo_error.lower() == 'absoluto':
        return abs(x_nuevo - x_anterior)
    else:
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100