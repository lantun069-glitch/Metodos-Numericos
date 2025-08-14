from funciones import calcular_error, f_cuadratica, df_cuadratica, f_cubica, df_cubica

def raiz_cuadrada_formula(A, p0, tolerancia=1e-6):
    """Formula: p_k = (1/2)(p_{k-1} + A/p_{k-1})"""
    print(f"Raiz cuadrada de {A} - Formula de recurrencia")
    pk = p0
    k = 0
    
    while True:
        pk_nuevo = 0.5 * (pk + A / pk)
        error = calcular_error(pk_nuevo, pk)
        k += 1
        print(f"k={k}: p_k = {pk_nuevo:.8f}, error = {error:.2e}")
        
        if error < tolerancia:
            break
        pk = pk_nuevo
    
    return pk_nuevo

def raiz_cubica_formula(A, p0, tolerancia=1e-6):
    """Formula: p_k = (2*p_{k-1} + A/p_{k-1}^2) / 3"""
    print(f"Raiz cubica de {A} - Formula de recurrencia")
    pk = p0
    k = 0
    
    while True:
        pk_nuevo = (2 * pk + A / (pk**2)) / 3
        error = calcular_error(pk_nuevo, pk)
        k += 1
        print(f"k={k}: p_k = {pk_nuevo:.8f}, error = {error:.2e}")
        
        if error < tolerancia:
            break
        pk = pk_nuevo
    
    return pk_nuevo

def newton_raphson_raiz(A, n, x0, tolerancia=1e-6):
    """Newton-Raphson para x^n - A = 0"""
    if n == 2:
        f = lambda x: f_cuadratica(x, A)
        df = lambda x: df_cuadratica(x, A)
        print(f"Raiz cuadrada de {A} - Newton-Raphson")
    else:
        f = lambda x: f_cubica(x, A)
        df = lambda x: df_cubica(x, A)
        print(f"Raiz cubica de {A} - Newton-Raphson")
    
    x = x0
    k = 0
    
    while True:
        fx = f(x)
        dfx = df(x)
        x_nuevo = x - fx / dfx
        error = calcular_error(x_nuevo, x)
        k += 1
        print(f"k={k}: x_k = {x_nuevo:.8f}, error = {error:.2e}")
        
        if error < tolerancia:
            break
        x = x_nuevo
    
    return x_nuevo