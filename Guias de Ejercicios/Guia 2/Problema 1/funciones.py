def g(x):
    return x**2 + x - 4

def dg_dx(x):
    return 2*x + 1

def calcular_error(x_nuevo, x_anterior, tipo_error):
    if tipo_error.lower() == 'absoluto':
        return abs(x_nuevo - x_anterior)
    elif tipo_error.lower() == 'porcentual':
        if x_nuevo == 0:
            return float('inf')
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100