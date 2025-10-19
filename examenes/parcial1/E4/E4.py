import sys
import os
import math
import numpy as np
from typing import List, Tuple, Callable

def lagrange(x_vals: List[float], y_vals: List[float], x: float) -> float:
    """
    Interpolación de Lagrange para estimar un valor en el punto x
    
    Args:
        x_vals: Lista de valores x conocidos
        y_vals: Lista de valores y conocidos
        x: Punto donde interpolar
        
    Returns:
        Valor interpolado en el punto x
    """
    n = len(x_vals)
    resultado = 0.0
    
    for i in range(n):
        # Calcular el polinomio Li(x)
        termino = y_vals[i]
        for j in range(n):
            if i != j:
                # Fórmula del polinomio de Lagrange
                termino *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        resultado += termino
    
    return resultado

def lagrange_polinomio(x_vals: List[float], y_vals: List[float]) -> str:
    """
    Construye la expresión simbólica del polinomio de Lagrange
    
    Args:
        x_vals: Lista de valores x conocidos
        y_vals: Lista de valores y conocidos
        
    Returns:
        Expresión del polinomio en formato de string
    """
    n = len(x_vals)
    polinomio = "p(t) = "
    terminos = []
    
    for i in range(n):
        # Construir cada término del polinomio de Lagrange
        termino = f"{y_vals[i]}"
        factores = []
        for j in range(n):
            if i != j:
                numerador = f"(t - {x_vals[j]})"
                denominador = f"({x_vals[i] - x_vals[j]})"
                factores.append(f"{numerador}/{denominador}")
        
        if factores:
            factores_str = " * ".join(factores)
            termino += f" * ({factores_str})"
        
        terminos.append(termino)
    
    polinomio += " + ".join(terminos)
    return polinomio

def spline_cubica(xv: List[float], yv: List[float], x: float) -> float:
    """
    Interpolación mediante spline cúbica natural
    
    Args:
        xv: Lista de valores x conocidos (nodos)
        yv: Lista de valores y conocidos
        x: Punto a evaluar
        
    Returns:
        Valor interpolado S(x)
    """
    n = len(xv)
    if n != len(yv) or n < 2:
        raise ValueError("xv y yv deben tener misma longitud y n>=2")
    
    # Verificar que xv sea estrictamente creciente
    for i in range(n-1):
        if xv[i] >= xv[i+1]:
            raise ValueError("xv debe ser estrictamente creciente")

    # Paso 1: armar sistema tridiagonal para segundas derivadas M
    h = [xv[i+1] - xv[i] for i in range(n-1)]

    # Diagonales (condición natural: extremos fijos)
    a = [0.0] + h[:-1] + [0.0]                      # subdiagonal
    b = [1.0] + [2.0*(h[i-1]+h[i]) for i in range(1, n-1)] + [1.0]  # diagonal
    c = [0.0] + h[1:] + [0.0]                       # superdiagonal

    # Lado derecho del sistema (extremos en 0 por condición natural)
    d = [0.0]*n
    for i in range(1, n-1):
        d[i] = 6.0 * ((yv[i+1]-yv[i]) / h[i] - (yv[i]-yv[i-1]) / h[i-1])

    # Paso 2: resolver A*M = d con resolución tridiagonal paso a paso
    # Eliminación hacia adelante
    for i in range(1, n):
        w = a[i] / b[i-1]
        b[i] -= w * c[i-1]
        d[i] -= w * d[i-1]
    
    # Sustitución hacia atrás
    M = [0.0]*n
    M[-1] = d[-1] / b[-1]
    for i in range(n-2, -1, -1):
        M[i] = (d[i] - c[i]*M[i+1]) / b[i]

    # Paso 3: extrapolación lineal si x está fuera del rango
    if x < xv[0]:
        m0 = (yv[1]-yv[0])/(xv[1]-xv[0])
        return yv[0] + m0*(x - xv[0])
    if x > xv[-1]:
        mn = (yv[-1]-yv[-2])/(xv[-1]-xv[-2])
        return yv[-1] + mn*(x - xv[-1])

    # Paso 4: localizar intervalo [x_i, x_{i+1}] (búsqueda lineal simple)
    i = 0
    while i < n-1 and not (xv[i] <= x <= xv[i+1]):
        i += 1

    # Paso 5: evaluar la spline en el intervalo
    xi, xi1 = xv[i], xv[i+1]
    hi = xi1 - xi
    yi, yi1 = yv[i], yv[i+1]
    Mi, Mi1 = M[i], M[i+1]

    A = (xi1 - x) / hi
    B = (x - xi) / hi
    S = (A*yi + B*yi1 
         + ((A**3 - A) * (hi**2) * Mi) / 6.0 
         + ((B**3 - B) * (hi**2) * Mi1) / 6.0)
    
    return S

def spline_ecuacion_tramo(xv: List[float], yv: List[float], tramo: int) -> str:
    """
    Devuelve la ecuación del polinomio cúbico para un tramo específico
    
    Args:
        xv: Lista de valores x conocidos (nodos)
        yv: Lista de valores y conocidos
        tramo: Índice del tramo (0 a n-2)
        
    Returns:
        Expresión del polinomio cúbico en formato de string
    """
    n = len(xv)
    
    # Calcular las segundas derivadas (coeficientes M)
    h = [xv[i+1] - xv[i] for i in range(n-1)]
    
    a = [0.0] + h[:-1] + [0.0]                      # subdiagonal
    b = [1.0] + [2.0*(h[i-1]+h[i]) for i in range(1, n-1)] + [1.0]  # diagonal
    c = [0.0] + h[1:] + [0.0]                       # superdiagonal
    
    d = [0.0]*n
    for i in range(1, n-1):
        d[i] = 6.0 * ((yv[i+1]-yv[i]) / h[i] - (yv[i]-yv[i-1]) / h[i-1])
    
    # Resolución tridiagonal
    for i in range(1, n):
        w = a[i] / b[i-1]
        b[i] -= w * c[i-1]
        d[i] -= w * d[i-1]
    
    M = [0.0]*n
    M[-1] = d[-1] / b[-1]
    for i in range(n-2, -1, -1):
        M[i] = (d[i] - c[i]*M[i+1]) / b[i]
    
    # Obtener los coeficientes para el tramo especificado
    i = tramo
    xi, xi1 = xv[i], xv[i+1]
    yi, yi1 = yv[i], yv[i+1]
    Mi, Mi1 = M[i], M[i+1]
    hi = h[i]
    
    # Coeficientes del polinomio cúbico S(x) = a + b(x-xi) + c(x-xi)² + d(x-xi)³
    a = yi
    b = (yi1 - yi) / hi - hi * (2*Mi + Mi1) / 6.0
    c = Mi / 2.0
    d = (Mi1 - Mi) / (6.0 * hi)
    
    ecuacion = f"S_{i}(t) = {a:.4f} + {b:.6f}(t-{xi}) + {c:.6f}(t-{xi})² + {d:.6f}(t-{xi})³"
    return ecuacion

def main():
    # datos
    tiempos = [1, 3, 5, 7, 13]
    velocidades = [800, 2310, 3090, 3940, 4755]  
    
    print("\na)")
    
    vel_4s = lagrange(tiempos, velocidades, 4)
    vel_6s = lagrange(tiempos, velocidades, 6)
    
    print(f"  vel en t = 4s: {vel_4s:.2f} cm/s")
    print(f"  vel en t = 6s: {vel_6s:.2f} cm/s")
    
    # b)
    print("\nb)")
    polinomio = lagrange_polinomio(tiempos, velocidades)
    print("  " + polinomio.replace(" + -", " - "))
    
    # c) 
    print("\nc)")
    vel_10s = spline_cubica(tiempos, velocidades, 10)
    print(f"  velocidad en t = 10s: {vel_10s:.2f} cm/s")
    print(f"  Lo de mas esta en la hoja")
    


if __name__ == "__main__":
    main()