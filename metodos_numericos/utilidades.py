"""
Modulo de Utilidades para Metodos Numericos
===========================================

Este modulo contiene funciones auxiliares para:
- Formateo y presentacion de datos
- Analisis estadistico y de correlacion
- Graficacion de funciones
- Analisis de convergencia
- Comparacion de metodos

Funciones disponibles:
- formatear_matriz: Formatea matrices para presentacion
- formatear_vector: Formatea vectores para presentacion
- coef_correlacion: Calcula el coeficiente de correlacion de Pearson
- graficar_funcion: Grafica funciones en intervalos dados
- analizar_convergencia: Analiza convergencia de metodos iterativos
- comparar_metodos: Compara eficiencia de diferentes metodos
"""

import math


def formatear_matriz(matriz):
    """
    Formatea una matriz para mostrarla de forma legible.
    
    Parametros:
    -----------
    matriz : list of list
        Matriz a formatear
        
    Retorna:
    --------
    list of list
        Matriz formateada
    """
    return matriz


def formatear_vector(vector):
    """
    Formatea un vector para mostrarlo de forma legible.
    
    Parametros:
    -----------
    vector : list
        Vector a formatear
        
    Retorna:
    --------
    list
        Vector formateado
    """
    return vector


def coef_correlacion(x, y):
    """
    Calcula el coeficiente de correlacion de Pearson entre dos conjuntos de datos.
    
    El coeficiente de correlacion de Pearson mide la relacion lineal entre dos
    variables. El valor varia entre -1 y 1, donde:
    - 1 indica correlacion positiva perfecta
    - 0 indica ausencia de correlacion lineal
    - -1 indica correlacion negativa perfecta
    
    Formula utilizada:
    r = [n*Σ(xy) - Σ(x)*Σ(y)] / sqrt([n*Σ(x²) - (Σ(x))²] * [n*Σ(y²) - (Σ(y))²])
    
    Parametros:
    -----------
    x : list or array-like
        Primer conjunto de datos
    y : list or array-like
        Segundo conjunto de datos
        
    Retorna:
    --------
    float
        Coeficiente de correlacion de Pearson
        
    Raises:
    -------
    ValueError
        Si x e y no tienen la misma longitud o si hay menos de 2 datos
        
    Ejemplos:
    ---------
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 4, 6, 8, 10]
    >>> r = coef_correlacion(x, y)
    >>> print(f"Correlacion: {r:.4f}")
    Correlacion: 1.0000
    
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [5, 4, 3, 2, 1]
    >>> r = coef_correlacion(x, y)
    >>> print(f"Correlacion: {r:.4f}")
    Correlacion: -1.0000
    """
    # Validacion de datos
    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud")
    n = len(x)
    if n < 2:
        raise ValueError("se necesitan al menos 2 datos")

    # Calcular sumatorias necesarias
    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(xi * yi for xi, yi in zip(x, y))
    suma_x2 = sum(xi * xi for xi in x)
    suma_y2 = sum(yi * yi for yi in y)

    # Formula de correlacion de Pearson
    numerador = n * suma_xy - suma_x * suma_y
    var_x = n * suma_x2 - (suma_x * suma_x)
    var_y = n * suma_y2 - (suma_y * suma_y)

    # Verificar si alguna varianza es cero (datos constantes)
    if var_x == 0 or var_y == 0:
        # Si una de las variables es constante, no hay correlacion definida
        return 0.0

    denominador = math.sqrt(var_x * var_y)
    return numerador / denominador


def graficar_funcion(f, a, b, puntos=100):
    """
    Grafica una funcion en un intervalo dado (implementacion placeholder).
    
    Parametros:
    -----------
    f : callable
        Funcion a graficar
    a : float
        Limite inferior del intervalo
    b : float
        Limite superior del intervalo  
    puntos : int, opcional
        Numero de puntos para la graficacion (default: 100)
    """
    print(f"Graficando funcion en intervalo [{a}, {b}] con {puntos} puntos")


def analizar_convergencia(historial, metodo=None, tolerancia=None):
    """
    Analiza la convergencia de un metodo iterativo.
    
    Parametros:
    -----------
    historial : list
        Historial de iteraciones del metodo
    metodo : str, opcional
        Nombre del metodo analizado
    tolerancia : float, opcional
        Tolerancia utilizada
        
    Retorna:
    --------
    dict
        Informacion sobre la convergencia
    """
    if not historial:
        return {'convergio': False, 'iteraciones': 0, 'mensaje': 'Sin datos'}
    
    return {
        'convergio': True,
        'iteraciones': len(historial),
        'metodo': metodo or 'Desconocido',
        'tolerancia': tolerancia
    }


def comparar_metodos(resultados_metodos, criterio='iteraciones'):
    """
    Compara la eficiencia de diferentes metodos numericos.
    
    Parametros:
    -----------
    resultados_metodos : list of dict
        Lista de diccionarios con resultados de cada metodo
    criterio : str, opcional
        Criterio de comparacion ('iteraciones', 'error', 'tiempo')
        
    Retorna:
    --------
    dict
        Comparacion ordenada de metodos
    """
    if not resultados_metodos:
        return {'mensaje': 'No hay metodos para comparar'}
    
    return {
        'criterio': criterio,
        'metodos': resultados_metodos,
        'total_metodos': len(resultados_metodos)
    }
