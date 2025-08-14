import math

# ========================================
# DEFINIR FUNCIONES ACA:
# ========================================

def f(x):
    """Funcion principal - CAMBIA ESTA LINEA"""
    return math.sin(x) + math.log(2*x) + 2

def df_dx(x):
    """Derivada de f(x) - CAMBIA ESTA LINEA (solo para Newton-Raphson)"""
    return 2*x

def g(x):
    """Funcion g(x) para punto fijo - CAMBIA ESTA LINEA (solo para punto fijo)"""
    return 4/x if x != 0 else 2

# ========================================
# NO TOCAR EL CODIGO DE ABAJO
# ========================================

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

def solicitar_tipo_error():
    """Solicita al usuario el tipo de error a utilizar"""
    print("\nTipo de error:")
    print("1. Error absoluto")
    print("2. Error porcentual")
    
    while True:
        opcion = input("Selecciona el tipo de error (1 o 2): ").strip()
        if opcion == "1":
            return 'absoluto'
        elif opcion == "2":
            return 'porcentual'
        else:
            print("Opcion invalida. Elegi 1 o 2.")

def solicitar_tolerancia(tipo_error):
    """Solicita la tolerancia segun el tipo de error"""
    if tipo_error.lower() == 'absoluto':
        tolerancia = float(input("Ingresa la tolerancia (ej: 1e-3): "))
        return tolerancia
    elif tipo_error.lower() == 'porcentual':
        tolerancia = float(input("Ingresa el porcentaje de error (ej: 0.1): "))
        return tolerancia
    else:
        raise ValueError("Tipo de error debe ser 'absoluto' o 'porcentual'")
