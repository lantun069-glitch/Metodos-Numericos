import math

def f(x):
    """f(x) = eta - 0.3 donde x = T2/T1"""
    gamma = 1/x
    ln_x = math.log(x)
    eta = (ln_x - (1 - gamma)) / (ln_x + gamma)
    return eta - 0.3

def calcular_error(x_nuevo, x_anterior, tipo_error):
    if tipo_error == 'absoluto':
        return abs(x_nuevo - x_anterior)
    else:
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100