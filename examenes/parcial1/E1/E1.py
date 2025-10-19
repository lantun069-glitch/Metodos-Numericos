import sys
import os
import math

def funcion(x):
    """f(x) = (x+1)/(x+4) - 0.25x"""
    return (x+1)/(x+4) - 0.25*x

def derivada(x):
    """f'(x) = 3/(x+4)^2 - 0.25"""
    return 3/((x+4)**2) - 0.25

def calcular_error_porcentual(x_nuevo, x_viejo):
    """Calcula el error porcentual según la fórmula dada:
    e = abs(xnuevo - xviejo)/((1/2)*abs(xnuevo+xviejo)) * 100"""
    return abs(x_nuevo - x_viejo) / (0.5 * abs(x_nuevo + x_viejo)) * 100

def biseccion_personalizado(f, a, b, tol=0.01, max_iter=100):
    """
    Método de bisección con criterio de error personalizado:
    e = abs(xnuevo - xviejo)/((1/2)*abs(xnuevo+xviejo)) * 100
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo")
    
    iteracion = 0
    c_viejo = None
    historial = []
    
    while iteracion < max_iter:
        c = (a + b) / 2
        fc = f(c)
        
        error = None
        if c_viejo is not None:
            error = calcular_error_porcentual(c, c_viejo)
        
        historial.append({
            'iteracion': iteracion + 1, 
            'a': a, 
            'b': b, 
            'c': c, 
            'fc': fc, 
            'error': error
        })
        
        if c_viejo is not None and error <= tol:
            return c, fc, error, iteracion + 1, historial
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        c_viejo = c
        iteracion += 1
    
    return c, f(c), calcular_error_porcentual(c, c_viejo), iteracion, historial

def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    """Método de Newton-Raphson con seguimiento de iteraciones"""
    x = x0
    historial = []
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-12:
            return None, None, None, i, historial
        
        x_nuevo = x - fx / dfx
        
        error = calcular_error_porcentual(x_nuevo, x) if i > 0 else None
        
        historial.append({
            'iteracion': i + 1, 
            'x': x, 
            'fx': fx, 
            'dfx': dfx, 
            'x_nuevo': x_nuevo, 
            'error': error
        })
        
        if error is not None and error <= tol:
            return x_nuevo, f(x_nuevo), error, i + 1, historial
        
        x = x_nuevo
    
    return x, f(x), error, max_iter, historial

def calcular_raiz_analitica():
    return 2.0

def main():    
    # a)
    raiz_analitica = calcular_raiz_analitica()
    print(f"a) Raiz calculada: {raiz_analitica}")
    
    # b)
    a, b = 1.75, 3.2
    tolerancia_porcentual = 0.01 
    
    print(f"\nb) biseccion con intervalo [{a}, {b}]")
    print(f"   Tolerancia: {tolerancia_porcentual}% (error porcentual)")
    
    try:
        raiz_bis, valor_bis, error_bis, iteraciones_bis, historial_bis = biseccion_personalizado(
            funcion, a, b, tolerancia_porcentual, max_iter=100
        )
        
        error_exacto = abs((raiz_bis - raiz_analitica) / raiz_analitica) * 100
        
        print(f"   raiz: {raiz_bis:.10f}")
        print(f"   f(raíz) = {valor_bis:.10e}")
        print(f"   Error estimado: {error_bis:.10f}%")
        print(f"   Error porcentual: {error_exacto:.10f}%")
        print(f"   Iteraciones: {iteraciones_bis}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # c1) 
    
    print("\nc1)")
    print(f"    Se encuentra en la hoja")

    
    # c2) Valor en la cuarta iter
    print("\nc2)")
    raiz_nr, valor_nr, error_nr, iteraciones_nr, historial_nr = newton_raphson(
        funcion, derivada, x0=1.0, tol=1e-12, max_iter=10
    )
    
    # Mostramos la cuarta iter
    if len(historial_nr) >= 4:
        iter4 = historial_nr[3]  # Ponemos 3 para mostrar la 4ta iter
        print(f"    x4 = {iter4['x_nuevo']:.10f}")
        print(f"    Error estimado: {iter4['error']:.10f}%")
        error_exacto_nr4 = abs((iter4['x_nuevo'] - raiz_analitica) / raiz_analitica) * 100
        print(f"    Error exacto: {error_exacto_nr4:.10f}%")
    else:
        print("    No se pudo completar 4 iteraciones.")

if __name__ == "__main__":
    main()