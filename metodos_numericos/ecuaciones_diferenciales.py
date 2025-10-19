"""
Métodos Numéricos para Ecuaciones Diferenciales Ordinarias (EDOs)
================================================================

Este módulo contiene implementaciones de métodos numéricos para resolver EDOs de primer orden
de la forma y' = f(x, y) con condición inicial y(x0) = y0.

Métodos implementados:
- Método de Euler (orden 1)
- Método de Heun (Euler mejorado, orden 2)
- Método del Punto Medio (orden 2)

Funciones disponibles:
- metodo_euler: Método básico de primer orden
- metodo_heun: Método predictor-corrector de segundo orden
- metodo_punto_medio: Método de segundo orden usando punto medio
"""

import numpy as np
from typing import Callable, Tuple, Union


def metodo_euler(f: Callable[[float, float], float], 
                 x0: float, 
                 xf: float, 
                 y0: float, 
                 h: float = None, 
                 n: int = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Resuelve una EDO usando el metodo de Euler
    
    Parametros:
    -----------
    f : Callable[[float, float], float]
        Funcion f(x, y) que define la EDO y' = f(x, y)
    x0 : float
        Valor inicial de x
    xf : float
        Valor final de x
    y0 : float
        Condicion inicial y(x0) = y0
    h : float, opcional
        Tamanio del paso. Si no se proporciona, usar n
    n : int, opcional
        Numero de subintervalos. Si no se proporciona, usar h
    
    Retorna:
    --------
    Tuple[np.ndarray, np.ndarray]
        Arrays con los valores de x e y calculados
        
    Ejemplo:
    --------
    >>> def f(x, y):
    ...     return -2 * x * y  # y' = -2xy
    >>> x, y = metodo_euler(f, 0, 1, 1, h=0.2)
    >>> print(f"y(1) ≈ {y[-1]:.6f}")
    """
    
    # Determinar h o n segun lo que se proporcione
    if h is None and n is None:
        raise ValueError("Debe proporcionar h o n")
    elif h is None:
        h = (xf - x0) / n
    else:
        n = int((xf - x0) / h)
    
    # Inicializar arrays para almacenar resultados
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    
    # Condiciones iniciales
    x[0] = x0
    y[0] = y0
    
    # Aplicar el metodo de Euler
    for i in range(1, n + 1):
        x[i] = x0 + i * h  # Siguiente punto en x
        y[i] = y[i-1] + h * f(x[i-1], y[i-1])  # Formula de Euler
    
    return x, y


def metodo_heun(f: Callable[[float, float], float],
                x0: float,
                xf: float,
                y0: float,
                h: float = None,
                n: int = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Resuelve una EDO usando el metodo de Heun (Euler mejorado)
    
    Parametros:
    -----------
    f : Callable[[float, float], float]
        Funcion f(x, y) que define la EDO y' = f(x, y)
    x0 : float
        Valor inicial de x
    xf : float
        Valor final de x
    y0 : float
        Condicion inicial y(x0) = y0
    h : float, opcional
        Tamanio del paso
    n : int, opcional
        Numero de subintervalos
    
    Retorna:
    --------
    Tuple[np.ndarray, np.ndarray]
        Arrays con los valores calculados
        
    Ejemplo:
    --------
    >>> def f(x, y):
    ...     return -2 * x * y  # y' = -2xy
    >>> x, y = metodo_heun(f, 0, 1, 1, h=0.2)
    >>> print(f"y(1) ≈ {y[-1]:.6f}")
    """
    
    # Determinar h o n
    if h is None and n is None:
        raise ValueError("Debe proporcionar h o n")
    elif h is None:
        h = (xf - x0) / n
    else:
        n = int((xf - x0) / h)
    
    # Inicializar arrays
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    
    # Condiciones iniciales
    x[0] = x0
    y[0] = y0
    
    # Aplicar metodo de Heun - segun pseudocodigo
    for i in range(1, n + 1):
        x[i] = x0 + i * h
        
        # Predictor usando Euler para estimar y_i+1
        xp = x[i-1] + h  # esto es x[i]
        yp = y[i-1] + h * f(x[i-1], y[i-1])  # predictor
        
        # Corrector usando promedio de pendientes
        y[i] = y[i-1] + h * (f(x[i-1], y[i-1]) + f(xp, yp)) / 2
    
    return x, y


def metodo_punto_medio(f: Callable[[float, float], float],
                       x0: float,
                       xf: float,
                       y0: float,
                       h: float = None,
                       n: int = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Resuelve una EDO usando el metodo del punto medio
    
    Parametros:
    -----------
    f : Callable[[float, float], float]
        Funcion f(x, y) que define la EDO y' = f(x, y)
    x0 : float
        Valor inicial de x
    xf : float
        Valor final de x
    y0 : float
        Condicion inicial y(x0) = y0
    h : float, opcional
        Tamanio del paso
    n : int, opcional
        Numero de subintervalos
    
    Retorna:
    --------
    Tuple[np.ndarray, np.ndarray]
        Arrays con los valores calculados
        
    Ejemplo:
    --------
    >>> def f(x, y):
    ...     return -2 * x * y  # y' = -2xy
    >>> x, y = metodo_punto_medio(f, 0, 1, 1, h=0.2)
    >>> print(f"y(1) ≈ {y[-1]:.6f}")
    """
    
    # Determinar h o n
    if h is None and n is None:
        raise ValueError("Debe proporcionar h o n")
    elif h is None:
        h = (xf - x0) / n
    else:
        n = int((xf - x0) / h)
    
    # Inicializar arrays
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    
    # Condiciones iniciales
    x[0] = x0
    y[0] = y0
    
    # Aplicar metodo del punto medio - VERSION CORREGIDA
    for i in range(1, n + 1):
        x[i] = x0 + i * h
        
        # Calcular punto medio - CORREGIDO
        xp = x[i-1] + h/2  # punto medio en x
        
        # Estimar y en el punto medio - CORREGIDO
        # Avanzamos h/2 usando la pendiente en (x[i-1], y[i-1])
        yp = y[i-1] + h * f(x[i-1], y[i-1]) / 2  # equivalente a h/2 * f(...)
        
        # Usar la pendiente en el punto medio para avanzar el paso completo
        y[i] = y[i-1] + h * f(xp, yp)
    
    return x, y


def calcular_error_convergencia(f: Callable[[float, float], float],
                                x0: float,
                                xf: float,
                                y0: float,
                                solucion_exacta: Callable[[float], float],
                                pasos: list) -> dict:
    """
    Analiza la convergencia de los metodos variando el tamanio del paso
    
    Parametros:
    -----------
    f : Callable[[float, float], float]
        Funcion que define la EDO
    x0, xf, y0 : float
        Condiciones del problema
    solucion_exacta : Callable[[float], float]
        Solucion analitica
    pasos : list
        Lista de tamanios de paso a probar
        
    Retorna:
    --------
    dict
        Errores para cada metodo y cada paso
    """
    
    errores = {
        'pasos': pasos,
        'euler': [],
        'heun': [],
        'punto_medio': []
    }
    
    valor_exacto = solucion_exacta(xf)
    
    for h in pasos:
        # Resolver con cada metodo
        _, y_euler = metodo_euler(f, x0, xf, y0, h=h)
        _, y_heun = metodo_heun(f, x0, xf, y0, h=h)
        _, y_pm = metodo_punto_medio(f, x0, xf, y0, h=h)
        
        # Calcular error absoluto en el punto final
        errores['euler'].append(abs(y_euler[-1] - valor_exacto))
        errores['heun'].append(abs(y_heun[-1] - valor_exacto))
        errores['punto_medio'].append(abs(y_pm[-1] - valor_exacto))
    
    return errores