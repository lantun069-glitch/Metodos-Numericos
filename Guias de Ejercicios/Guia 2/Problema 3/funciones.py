import math

def calcular_error(x_nuevo, x_anterior):
    return abs(x_nuevo - x_anterior)

def f_cuadratica(x, A):
    return x**2 - A

def df_cuadratica(x, A):
    return 2*x

def f_cubica(x, A):
    return x**3 - A

def df_cubica(x, A):
    return 3*x**2