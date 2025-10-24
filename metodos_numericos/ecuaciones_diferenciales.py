"""
Métodos Numéricos para Ecuaciones Diferenciales Ordinarias (EDOs)
================================================================

Este módulo contiene implementaciones de métodos numéricos para resolver EDOs de primer orden
de la forma y' = f(x, y) con condición inicial y(x0) = y0.

Métodos implementados:
- Método de Euler (orden 1)
- Método de Heun (Euler mejorado, orden 2)
- Método del Punto Medio (orden 2)
- Método de Runge-Kutta de 4to orden (RK4, orden 4)

Funciones disponibles:
- metodo_euler: Método básico de primer orden
- metodo_heun: Método predictor-corrector de segundo orden
- metodo_punto_medio: Método de segundo orden usando punto medio
- metodo_rk4: Método de Runge-Kutta de 4to orden (alta precisión)
- calcular_error_convergencia: Analiza convergencia comparando con solución exacta
- calcular_factor_convergencia_Q: Calcula factor Q para verificar orden empírico
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


def metodo_rk4(f: Callable[[float, float], float],
               x0: float,
               xf: float,
               y0: float,
               h: float = None,
               n: int = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Resuelve una EDO usando el metodo de Runge-Kutta de 4to orden (RK4 clasico)
    
    El metodo RK4 es el mas utilizado en la practica por su excelente precision
    y estabilidad. Utiliza 4 evaluaciones de la funcion por paso para lograr
    un error de orden O(h^5).
    
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
        
    Raises:
    -------
    ValueError
        Si no se proporciona ni h ni n
    
    Ejemplo:
    --------
    >>> def f(x, y):
    ...     return -2 * x * y  # y' = -2xy
    >>> x, y = metodo_rk4(f, 0, 1, 1, h=0.1)
    >>> print(f"y(1) = {y[-1]:.6f}")
    >>> # Solucion exacta: exp(-x^2) = exp(-1) = 0.367879
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
    
    # Aplicar el metodo RK4 clasico
    # Basado en el pseudocodigo del PDF de la profesora
    for i in range(n):
        # Calcular las 4 pendientes (k1, k2, k3, k4)
        # k1: pendiente al inicio del intervalo
        k1 = f(x[i], y[i])
        
        # k2: pendiente en el punto medio usando k1
        k2 = f(x[i] + h/2, y[i] + k1 * h/2)
        
        # k3: pendiente en el punto medio usando k2
        k3 = f(x[i] + h/2, y[i] + k2 * h/2)
        
        # k4: pendiente al final del intervalo usando k3
        k4 = f(x[i] + h, y[i] + k3 * h)
        
        # Promedio ponderado de las pendientes
        # Los pesos son 1/6, 2/6, 2/6, 1/6
        y[i+1] = y[i] + h * (k1 + 2*k2 + 2*k3 + k4) / 6
        x[i+1] = x[i] + h
    
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
        'punto_medio': [],
        'rk4': []
    }
    
    valor_exacto = solucion_exacta(xf)
    
    for h in pasos:
        # Resolver con cada metodo
        _, y_euler = metodo_euler(f, x0, xf, y0, h=h)
        _, y_heun = metodo_heun(f, x0, xf, y0, h=h)
        _, y_pm = metodo_punto_medio(f, x0, xf, y0, h=h)
        _, y_rk4 = metodo_rk4(f, x0, xf, y0, h=h)
        
        # Calcular error absoluto en el punto final
        errores['euler'].append(abs(y_euler[-1] - valor_exacto))
        errores['heun'].append(abs(y_heun[-1] - valor_exacto))
        errores['punto_medio'].append(abs(y_pm[-1] - valor_exacto))
        errores['rk4'].append(abs(y_rk4[-1] - valor_exacto))
    
    return errores


def calcular_factor_convergencia_Q(metodo: Callable,
                                   f: Callable[[float, float], float],
                                   x0: float,
                                   xf: float,
                                   y0: float,
                                   h_inicial: float = 0.1,
                                   graficar: bool = True,
                                   nombre_metodo: str = None) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    Calcula el factor de convergencia Q para verificar el orden de un metodo numerico
    
    El factor Q se calcula usando tres mallas con pasos h, h/2 y h/4, siguiendo
    la formula:
        Q = log(|y1 - y2| / |y2 - y3|) / log(2)
    
    donde y1, y2, y3 son las aproximaciones con pasos h, h/2, h/4 respectivamente.
    
    Parametros:
    -----------
    metodo : Callable
        Funcion del metodo numerico a evaluar (euler, heun, rk4, etc.)
    f : Callable[[float, float], float]
        Funcion que define la EDO y' = f(x, y)
    x0 : float
        Valor inicial de x
    xf : float
        Valor final de x
    y0 : float
        Condicion inicial y(x0) = y0
    h_inicial : float, default=0.1
        Tamanio de paso inicial (se usara h, h/2, h/4)
    graficar : bool, default=True
        Si True, genera un grafico del factor Q vs x
    nombre_metodo : str, optional
        Nombre del metodo para el titulo del grafico
        
    Retorna:
    --------
    Tuple[np.ndarray, np.ndarray, float]
        - x_comun: puntos x donde se calculo Q
        - Q_valores: valores del factor Q en cada punto
        - Q_promedio: promedio de Q (estimacion del orden)
        
    Ejemplo:
    --------
    >>> def f(x, y):
    ...     return -2 * x * y
    >>> x_q, Q, Q_prom = calcular_factor_convergencia_Q(metodo_euler, f, 0, 1, 1)
    >>> print(f"Orden empirico: {Q_prom:.2f}")  # Deberia ser cercano a 1
    """
    
    # Definir los tres tamanios de paso segun la teoria
    h1 = h_inicial
    h2 = h1 / 2.0
    h3 = h1 / 4.0
    
    print(f"\n{'='*50}")
    print(f"CALCULO DEL FACTOR DE CONVERGENCIA Q")
    print(f"{'='*50}")
    print(f"Metodo: {nombre_metodo if nombre_metodo else 'Sin especificar'}")
    print(f"Intervalo: [{x0}, {xf}]")
    print(f"Condicion inicial: y({x0}) = {y0}")
    print(f"Pasos utilizados: h={h1:.4f}, h/2={h2:.4f}, h/4={h3:.4f}")
    
    # Resolver la EDO con los tres pasos diferentes
    try:
        x1, y1 = metodo(f, x0, xf, y0, h=h1)
        x2, y2 = metodo(f, x0, xf, y0, h=h2)
        x3, y3 = metodo(f, x0, xf, y0, h=h3)
    except Exception as e:
        print(f"Error al ejecutar el metodo: {e}")
        return np.array([]), np.array([]), np.nan
    
    print(f"Puntos calculados: n1={len(y1)}, n2={len(y2)}, n3={len(y3)}")
    
    # Calcular Q en los puntos comunes de las tres mallas
    Q_valores = []
    x_comun = []
    
    # Iterar sobre los puntos de la malla mas gruesa (h1)
    for i in range(len(x1)):
        # Encontrar los indices correspondientes en las otras mallas
        idx2 = i * 2
        idx3 = i * 4
        
        # Verificar que los indices esten dentro del rango
        if idx2 < len(y2) and idx3 < len(y3):
            # Calcular las diferencias entre aproximaciones sucesivas
            diff_12 = abs(y1[i] - y2[idx2])  # diferencia entre h y h/2
            diff_23 = abs(y2[idx2] - y3[idx3])  # diferencia entre h/2 y h/4
            
            # Evitar division por cero y valores muy pequenos
            if diff_23 > 1e-14 and diff_12 > 1e-14:
                # Aplicar la formula del factor Q
                q = np.log(diff_12 / diff_23) / np.log(2.0)
                
                # Filtrar valores anomalos
                if 0 < q < 10:
                    Q_valores.append(q)
                    x_comun.append(x1[i])
    
    # Convertir a arrays numpy
    x_comun = np.array(x_comun)
    Q_valores = np.array(Q_valores)
    
    # Calcular estadisticas de Q
    if len(Q_valores) > 0:
        Q_promedio = np.median(Q_valores)  # mediana mas robusta que promedio
        Q_mean = np.mean(Q_valores)
        Q_std = np.std(Q_valores)
        
        print(f"\n{'='*50}")
        print(f"RESULTADOS:")
        print(f"{'='*50}")
        print(f"Q promedio (media):  {Q_mean:.3f}")
        print(f"Q promedio (mediana): {Q_promedio:.3f}")
        print(f"Desviacion estandar:  {Q_std:.3f}")
        print(f"Rango Q: [{np.min(Q_valores):.3f}, {np.max(Q_valores):.3f}]")
        
        # Interpretacion del orden
        ordenes_teoricos = {1: 'Euler', 2: 'Heun/Punto Medio', 4: 'RK4'}
        orden_cercano = min(ordenes_teoricos.keys(), 
                          key=lambda x: abs(x - Q_promedio))
        print(f"\nInterpretacion: Orden empirico ≈ {Q_promedio:.2f}")
        print(f"Metodo mas cercano: {ordenes_teoricos[orden_cercano]} (orden {orden_cercano})")
    else:
        Q_promedio = np.nan
        print("\nAdvertencia: No se pudo calcular Q (posible error numerico)")
    
    # Graficar si se solicita
    if graficar and len(Q_valores) > 0:
        import matplotlib.pyplot as plt
        
        # Crear figura con mejor diseno
        fig, ax = plt.subplots(figsize=(12, 7))
        
        # Graficar Q vs x con estilo mejorado
        ax.plot(x_comun, Q_valores, 'b.-', label=f'Q(x)', 
                linewidth=2, markersize=8, markerfacecolor='white', 
                markeredgewidth=2, markeredgecolor='blue')
        
        # Linea horizontal con el promedio
        ax.axhline(y=Q_promedio, color='red', linestyle='--', 
                   label=f'Q mediana = {Q_promedio:.3f}', alpha=0.8, linewidth=2)
        
        # Agregar lineas de referencia para ordenes teoricos
        colores_ref = {'1': 'orange', '2': 'green', '4': 'purple'}
        for orden, color in zip([1, 2, 4], ['orange', 'green', 'purple']):
            ax.axhline(y=orden, color=color, linestyle=':', alpha=0.6, linewidth=1.5)
            ax.text(x_comun[-1] + 0.01*(x_comun[-1]-x_comun[0]), orden, 
                   f'  Orden {orden}', va='center', fontsize=10, color=color)
        
        # Configuracion del grafico
        ax.set_xlabel('x', fontsize=13)
        ax.set_ylabel('Factor de Convergencia Q', fontsize=13)
        titulo = f'Factor de Convergencia Q'
        if nombre_metodo:
            titulo += f' - Metodo: {nombre_metodo}'
        ax.set_title(titulo, fontsize=15, fontweight='bold')
        
        # Mejorar la leyenda
        ax.legend(loc='upper right', framealpha=0.95, shadow=True, fontsize=11)
        
        # Grid y limites
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.set_ylim([0, min(6, max(Q_valores) + 1)])
        ax.set_xlim([x_comun[0] - 0.02*(x_comun[-1]-x_comun[0]), 
                     x_comun[-1] + 0.02*(x_comun[-1]-x_comun[0])])
        
        # Agregar caja de informacion
        info_text = (f'h inicial: {h_inicial:.3f}\n'
                    f'Puntos analizados: {len(Q_valores)}\n'
                    f'Q promedio: {Q_promedio:.3f}')
        props = dict(boxstyle='round,pad=0.5', facecolor='lightgray', 
                    alpha=0.8, edgecolor='black')
        ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=props)
        
        # Sombrear region de confianza (promedio +/- std)
        if len(Q_valores) > 1:
            Q_std = np.std(Q_valores)
            ax.fill_between(x_comun, Q_promedio - Q_std, Q_promedio + Q_std, 
                           alpha=0.2, color='red', label=f'±σ')
        
        plt.tight_layout()
        plt.show()
        
        print(f"\n✓ Grafico generado exitosamente")
    elif graficar:
        print("\n✗ No se pudo generar el grafico (datos insuficientes)")
    
    print(f"{'='*50}\n")
    
    return x_comun, Q_valores, Q_promedio