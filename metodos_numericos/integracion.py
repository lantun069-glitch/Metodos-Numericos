"""
Métodos de Integración Numérica
===============================

Este módulo contiene implementaciones de métodos numéricos para calcular integrales definidas:
- Regla del Trapecio (simple y compuesta)
- Regla de Simpson (simple y compuesta)
- Cuadratura de Gauss-Legendre
- Métodos adaptativos
- Estimación de errores

Funciones disponibles:
- trapecio_simple: Integración básica con un solo intervalo
- trapecio_compuesto: Integración con múltiples subintervalos
- trapecio_compuesto_v2: Versión alternativa del trapecio compuesto
- trapecio_compuesto_datos: Para datos tabulados
- simpson_1_3_simple: Simpson básico con un intervalo
- simpson_1_3_compuesto: Simpson con múltiples subintervalos
- simpson_compuesta_funcion: Integración con función analítica
- simpson_compuesta_datos: Integración con datos tabulados
- simpson_compuesta_mejorada: Con estimación de error mejorada
- gauss_legendre_integration: Cuadratura de Gauss-Legendre (alta precisión)
- calcular_error_trapecio: Estimación de error para trapecio
- calcular_error_simpson: Estimación de error para Simpson
"""

import math
import numpy as np
from typing import Callable, Union, List, Tuple
import warnings


def simpson_compuesta_funcion(f: Callable, a: float, b: float, n: int) -> float:
    """
    Calcula la integral definida usando la Regla de Simpson Compuesta
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : floate
        Limite inferior de integracion
    b : float
        Limite superior de integracion
    n : int
        Numero de subintervalos (debe ser par)
    
    Retorna:
    --------
    float
        Aproximacion de la integral definida
    
    Raises:
    -------
    ValueError
        Si n no es par
    
    Ejemplo:
    --------
    >>> def f(x):
    ...     return x**2
    >>> resultado = simpson_compuesta_funcion(f, 0, 1, 100)
    >>> print(f"Integral de x^2 de 0 a 1: {resultado:.6f}")
    """
    
    # Verificar que n sea par
    if n % 2 != 0:
        raise ValueError("Error: n debe ser un numero par!")
    
    # Calcular el tamanio del paso
    h = (b - a) / n
    
    # Inicializar la suma con los valores extremos
    suma = f(a) + f(b)
    
    # Sumar terminos con coeficiente 4 (indices impares) y 2 (indices pares)
    for i in range(1, n):
        xi = a + i * h
        
        if i % 2 == 1:  # indice impar - coeficiente 4
            suma += 4 * f(xi)
        else:  # indice par - coeficiente 2
            suma += 2 * f(xi)
    
    # Aplicar la formula de Simpson compuesta
    integral = (h / 3) * suma
    
    return integral


def simpson_compuesta_datos(x_datos: Union[List, tuple], 
                           y_datos: Union[List, tuple]) -> float:
    """
    Calcula la integral usando Simpson Compuesta con datos tabulados
    
    Parametros:
    -----------
    x_datos : array-like
        Valores de x equiespaciados
    y_datos : array-like
        Valores de y correspondientes
    
    Retorna:
    --------
    float
        Aproximacion de la integral
    
    Raises:
    -------
    ValueError
        Si los datos no tienen la misma longitud o hay menos de 3 puntos
    
    Ejemplo:
    --------
    >>> x = [0, 0.5, 1.0, 1.5, 2.0]
    >>> y = [0, 0.25, 1.0, 2.25, 4.0]  # valores de x^2
    >>> resultado = simpson_compuesta_datos(x, y)
    >>> print(f"Integral aproximada: {resultado:.6f}")
    """
    
    # Convertir a listas si es necesario
    x = list(x_datos)
    y = list(y_datos)
    
    # Verificaciones
    if len(x) != len(y):
        raise ValueError("x_datos y y_datos deben tener la misma longitud")
    
    if len(x) < 3:
        raise ValueError("Se necesitan al menos 3 puntos para aplicar Simpson")
    
    # Determinar n basado en el numero de puntos
    m = len(x) - 1  # numero de intervalos
    
    if m % 2 == 0:  # m es par
        n = m
    else:  # m es impar - usar un punto menos
        n = m - 1
        warnings.warn(f"Numero de intervalos impar. Usando {n} intervalos y descartando el ultimo punto")
        x = x[:-1]
        y = y[:-1]
    
    # Calcular h
    h = (x[-1] - x[0]) / n
    
    # Inicializar suma con extremos
    suma = y[0] + y[n]
    
    # Sumar terminos intermedios
    for i in range(1, n):
        if i % 2 == 1:  # indice impar
            suma += 4 * y[i]
        else:  # indice par
            suma += 2 * y[i]
    
    # Calcular integral
    integral = (h / 3) * suma
    
    return integral


def simpson_compuesta_mejorada(f: Callable, a: float, b: float, n: int) -> Tuple[float, float]:
    """
    Version mejorada de Simpson Compuesta con estimacion de error
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : float
        Limite inferior
    b : float
        Limite superior
    n : int
        Numero de subintervalos (debe ser par)
    
    Retorna:
    --------
    tuple
        (integral_mejorada, error_estimado)
    
    Ejemplo:
    --------
    >>> def f(x):
    ...     return math.exp(-x**2)
    >>> integral, error = simpson_compuesta_mejorada(f, 0, 1, 50)
    >>> print(f"Integral: {integral:.8f} ± {error:.2e}")
    """
    
    # Verificar n par
    if n % 2 != 0:
        raise ValueError("n debe ser par!")
    
    # Calcular con n subintervalos
    I_n = simpson_compuesta_funcion(f, a, b, n)
    
    # Calcular con 2n subintervalos para estimar error
    I_2n = simpson_compuesta_funcion(f, a, b, 2 * n)
    
    # Estimacion del error usando Richardson
    error_estimado = abs(I_2n - I_n) / 15
    
    # Valor mejorado usando extrapolacion de Richardson
    integral_mejorada = I_2n + (I_2n - I_n) / 15
    
    return integral_mejorada, error_estimado


def trapecio_compuesto(f: Callable, a: float, b: float, n: int) -> float:
    """
    Calcula la integral definida usando la Regla del Trapecio Compuesta
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : float
        Limite inferior de integracion
    b : float
        Limite superior de integracion
    n : int
        Numero de subintervalos
    
    Retorna:
    --------
    float
        Aproximacion de la integral definida
    
    Ejemplo:
    --------
    >>> def f(x):
    ...     return x**2
    >>> resultado = trapecio_compuesto(f, 0, 1, 100)
    >>> print(f"Integral de x^2 de 0 a 1: {resultado:.6f}")
    """
    
    # Calcular el tamanio del paso
    h = (b - a) / n
    
    # Inicializar la suma con los valores extremos
    suma = f(a) + f(b)
    
    # Sumar terminos intermedios con coeficiente 2
    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)
    
    # Aplicar la formula del trapecio compuesto
    integral = (h / 2) * suma
    
    return integral


def trapecio_simple(f: Callable, a: float, b: float) -> float:
    """
    Calcula la integral de f en [a,b] usando el metodo del trapecio simple
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : float
        Limite inferior de integracion
    b : float
        Limite superior de integracion
    
    Retorna:
    --------
    float
        Aproximacion de la integral
        
    Ejemplo:
    --------
    >>> def f(x):
    ...     return x**2 + 1
    >>> resultado = trapecio_simple(f, 0, 3)
    >>> print(f"Integral aproximada: {resultado}")  # deberia dar 16.5
    """
    # Formula del trapecio: I = (b-a) * (f(a) + f(b)) / 2
    integral_aprox = (b - a) * (f(a) + f(b)) / 2
    
    return integral_aprox


def calcular_error_trapecio(f_segunda_derivada: Callable, a: float, b: float, c: float = None) -> float:
    """
    Estima el error del metodo del trapecio
    Error = -(b-a)^3 / 12 * f''(c), donde c esta en [a,b]
    
    Parametros:
    -----------
    f_segunda_derivada : Callable
        Segunda derivada de la funcion
    a : float
        Limite inferior
    b : float
        Limite superior  
    c : float, opcional
        Punto donde evaluar la segunda derivada (por defecto punto medio)
        
    Retorna:
    --------
    float
        Error absoluto estimado
    """
    if c is None:
        c = (a + b) / 2  # Usamos el punto medio si no se especifica c
    
    error = -((b - a)**3 / 12) * f_segunda_derivada(c)
    return abs(error)


def trapecio_compuesto_v2(f: Callable, a: float, b: float, n: int) -> float:
    """
    Calcula la integral usando la regla del trapecio compuesto (version alternativa)
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : float
        Limite inferior
    b : float
        Limite superior 
    n : int
        Numero de subintervalos
    
    Retorna:
    --------
    float
        Aproximacion de la integral
        
    Ejemplo:
    --------
    >>> def f(x):
    ...     return x**2 + 1
    >>> resultado = trapecio_compuesto_v2(f, 0, 3, 2)
    >>> print(f"Integral con 2 subintervalos: {resultado}")  # deberia dar 13.125
    """
    # Calculamos el tamanio del paso
    h = (b - a) / n
    
    # Inicializamos la suma con los extremos
    suma = f(a) + f(b)
    
    # Sumamos los puntos intermedios multiplicados por 2
    for i in range(1, n):
        x_i = a + i * h
        suma += 2 * f(x_i)
    
    # Aplicamos la formula del trapecio compuesto
    integral = (b - a) / (2 * n) * suma
    
    return integral


def trapecio_compuesto_datos(x_datos: Union[List, tuple], y_datos: Union[List, tuple]) -> float:
    """
    Version para datos tabulados equiespaciados
    
    Parametros:
    -----------
    x_datos : array-like
        Array de valores x equiespaciados
    y_datos : array-like
        Array de valores y correspondientes
    
    Retorna:
    --------
    float
        Aproximacion de la integral
        
    Ejemplo:
    --------
    >>> import numpy as np
    >>> x_datos = np.array([0, 1.5, 3])
    >>> y_datos = np.array([1, 3.25, 10])  # valores de x^2 + 1
    >>> resultado = trapecio_compuesto_datos(x_datos, y_datos)
    >>> print(f"Integral con datos tabulados: {resultado}")
    """
    n = len(x_datos) - 1  # numero de subintervalos
    
    if n <= 0:
        return 0
    
    # Verificamos que los datos esten equiespaciados
    h = x_datos[1] - x_datos[0]
    
    # Calculamos la suma
    suma = y_datos[0] + y_datos[-1]  # extremos
    
    # Puntos intermedios
    for i in range(1, n):
        suma += 2 * y_datos[i]
    
    # Formula del trapecio compuesto
    integral = h / 2 * suma
    
    return integral


def simpson_1_3_simple(f: Callable, a: float, b: float) -> float:
    """
    Calcula la integral usando la regla de Simpson 1/3 simple
    Usa 3 puntos: a, punto medio, b
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : float
        Limite inferior
    b : float
        Limite superior
    
    Retorna:
    --------
    float
        Aproximacion de la integral
        
    Ejemplo:
    --------
    >>> def f(x):
    ...     return x**2 + 1
    >>> resultado = simpson_1_3_simple(f, 0, 3)
    >>> print(f"Simpson 1/3 simple: {resultado}")  # deberia dar 12
    """
    # Calculamos el punto medio
    h = (b - a) / 2
    x_medio = (a + b) / 2
    
    # Formula de Simpson 1/3: h/3 * [f(a) + 4*f(x_medio) + f(b)]
    integral = h / 3 * (f(a) + 4 * f(x_medio) + f(b))
    
    return integral


def simpson_1_3_compuesto(f: Callable, a: float, b: float, n: int) -> float:
    """
    Regla de Simpson 1/3 compuesta
    n debe ser par para aplicar Simpson
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : float
        Limite inferior
    b : float
        Limite superior
    n : int
        Numero de subintervalos (debe ser par)
    
    Retorna:
    --------
    float
        Aproximacion de la integral
        
    Ejemplo:
    --------
    >>> def f(x):
    ...     return x**2 + 1
    >>> resultado = simpson_1_3_compuesto(f, 0, 3, 4)
    >>> print(f"Simpson 1/3 con 4 subintervalos: {resultado}")
    """
    # Verificamos que n sea par
    if n % 2 != 0:
        raise ValueError("n debe ser par para Simpson 1/3")
    
    h = (b - a) / n
    
    # Inicializamos con los extremos
    suma = f(a) + f(b)
    
    # Sumamos los terminos impares (multiplicados por 4)
    for i in range(1, n, 2):
        x_i = a + i * h
        suma += 4 * f(x_i)
    
    # Sumamos los terminos pares (multiplicados por 2)
    for i in range(2, n, 2):
        x_i = a + i * h
        suma += 2 * f(x_i)
    
    # Aplicamos la formula de Simpson compuesta
    integral = h / 3 * suma
    
    return integral


def calcular_error_simpson(f_cuarta_derivada: Callable, a: float, b: float, c: float = None) -> float:
    """
    Estima el error de Simpson 1/3
    Error = -(b-a)^5 / 2880 * f''''(c)
    
    Parametros:
    -----------
    f_cuarta_derivada : Callable
        Cuarta derivada de la funcion
    a : float
        Limite inferior
    b : float
        Limite superior
    c : float, opcional
        Punto donde evaluar la cuarta derivada (por defecto punto medio)
        
    Retorna:
    --------
    float
        Error absoluto estimado
    """
    if c is None:
        c = (a + b) / 2
    
    error = -((b - a)**5 / 2880) * f_cuarta_derivada(c)
    return abs(error)


def gauss_legendre_integration(f: Callable, a: float, b: float, n_points: int = 2) -> float:
    """
    Calcula la integral de una funcion usando cuadratura de Gauss-Legendre
    
    Parametros:
    -----------
    f : Callable
        Funcion a integrar
    a : float  
        Limite inferior de integracion
    b : float
        Limite superior de integracion  
    n_points : int
        Numero de puntos de Gauss (2 a 6)
        
    Retorna:
    --------
    float
        Aproximacion de la integral
        
    Ejemplo:
    --------
    >>> def f(x):
    ...     return 2 * x**3
    >>> resultado = gauss_legendre_integration(f, 0, 0.5, n_points=2)
    >>> print(f"Integral con 2 puntos: {resultado:.6f}")
    """
    
    # Definir pesos (c_i) y nodos (x_i) para diferentes numeros de puntos
    # Estos valores vienen de tablas precalculadas
    
    if n_points == 2:
        # Para 2 puntos
        c = [1.0, 1.0]
        x = [-0.577350269, 0.577350269]  # -1/sqrt(3) y 1/sqrt(3)
        
    elif n_points == 3:
        # Para 3 puntos  
        c = [0.555555556, 0.888888889, 0.555555556]
        x = [-0.774596669, 0.0, 0.774596669]
        
    elif n_points == 4:
        # Para 4 puntos
        c = [0.347854845, 0.652145155, 0.652145155, 0.347854845]
        x = [-0.861136312, -0.339981044, 0.339981044, 0.861136312]
        
    elif n_points == 5:
        # Para 5 puntos
        c = [0.236926885, 0.478628670, 0.568888889, 0.478628670, 0.236926885]
        x = [-0.906179846, -0.538469310, 0.0, 0.538469310, 0.906179846]
        
    elif n_points == 6:
        # Para 6 puntos
        c = [0.171324492, 0.360761573, 0.467913935, 
             0.467913935, 0.360761573, 0.171324492]
        x = [-0.932469514, -0.661209386, -0.238619186,
             0.238619186, 0.661209386, 0.932469514]
    else:
        raise ValueError("El numero de puntos debe estar entre 2 y 6")
    
    # Aplicar cambio de variables de [-1,1] a [a,b]
    # x = ((b-a)*x' + (b+a))/2
    # dx = (b-a)/2 * dx'
    
    integral = 0.0
    
    for i in range(n_points):
        # Transformar x_i del intervalo [-1,1] al intervalo [a,b]
        x_transformed = ((b - a) * x[i] + (b + a)) / 2
        
        # Evaluar la funcion en el punto transformado
        f_value = f(x_transformed)
        
        # Sumar la contribucion ponderada
        integral += c[i] * f_value
    
    # Multiplicar por el factor del cambio de variables
    integral *= (b - a) / 2
    
    return integral


