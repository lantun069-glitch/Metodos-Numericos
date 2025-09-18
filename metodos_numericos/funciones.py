"""
Modulo de Funciones Matematicas
===============================

Este modulo contiene funciones matematicas comunes utilizadas en metodos numericos.
Las funciones estan organizadas por categoria para facilitar su uso.
"""

import math
from typing import Callable


# FUNCIONES DE UTILIDAD PARA ERRORES

def calcular_error(x_nuevo: float, x_anterior: float, tipo_error: str = 'absoluto') -> float:
    """
    Calcula el error segun el tipo especificado
    
    Args:
        x_nuevo: Valor actual
        x_anterior: Valor anterior
        tipo_error: 'absoluto' o 'porcentual'
    
    Returns:
        Error calculado
    """
    if tipo_error.lower() == 'absoluto':
        return abs(x_nuevo - x_anterior)
    elif tipo_error.lower() == 'porcentual':
        if x_nuevo == 0:
            return float('inf')
        return abs((x_nuevo - x_anterior) / x_nuevo) * 100
    else:
        raise ValueError("tipo_error debe ser 'absoluto' o 'porcentual'")


# FUNCIONES MATEMATICAS PREDEFINIDAS

class FuncionesBasicas:
    """Clase con funciones matematicas basicas comunmente utilizadas"""
    
    @staticmethod
    def f1(x):
        """f(x) = sin(x) + log(2x) + 2"""
        return math.sin(x) + math.log(2*x) + 2
    
    @staticmethod
    def df1_dx(x):
        """Derivada de f1: f'(x) = cos(x) + 1/x"""
        return math.cos(x) + 1/x
    
    @staticmethod
    def f2(x):
        """f(x) = x^3 - 2x - 5"""
        return x**3 - 2*x - 5
    
    @staticmethod
    def df2_dx(x):
        """Derivada de f2: f'(x) = 3x^2 - 2"""
        return 3*x**2 - 2
    
    @staticmethod
    def f3(x):
        """f(x) = e^x - 3x"""
        return math.exp(x) - 3*x
    
    @staticmethod
    def df3_dx(x):
        """Derivada de f3: f'(x) = e^x - 3"""
        return math.exp(x) - 3
    
    @staticmethod
    def f4(x):
        """f(x) = x^2 - cos(x)"""
        return x**2 - math.cos(x)
    
    @staticmethod
    def df4_dx(x):
        """Derivada de f4: f'(x) = 2x + sin(x)"""
        return 2*x + math.sin(x)
    
    @staticmethod
    def f5(x):
        """f(x) = x^5 - 3x^3 - 2x^2 + 2"""
        return x**5 - 3*x**3 - 2*x**2 + 2
    
    @staticmethod
    def df5_dx(x):
        """Derivada de f5: f'(x) = 5x^4 - 9x^2 - 4x"""
        return 5*x**4 - 9*x**2 - 4*x


class FuncionesPuntoFijo:
    """Funciones para el metodo de punto fijo"""
    
    @staticmethod
    def g1(x):
        """g(x) = 4/x para f(x) = x^2 - 4"""
        return 4/x if x != 0 else 2
    
    @staticmethod
    def g2(x):
        """g(x) = (2x + 5)^(1/3) para f(x) = x^3 - 2x - 5"""
        return (2*x + 5)**(1/3)
    
    @staticmethod
    def g3(x):
        """g(x) = exp(x)/3 para f(x) = e^x - 3x"""
        return math.exp(x)/3
    
    @staticmethod
    def g4(x):
        """g(x) = cos(x)^(1/2) para f(x) = x^2 - cos(x)"""
        return math.sqrt(math.cos(x)) if math.cos(x) >= 0 else x


# FUNCIONES AUXILIARES

def verificar_cambio_signo(f: Callable[[float], float], a: float, b: float) -> bool:
    """
    Verifica si hay cambio de signo en el intervalo [a, b]
    
    Args:
        f: Funcion a evaluar
        a: Extremo izquierdo del intervalo
        b: Extremo derecho del intervalo
    
    Returns:
        True si hay cambio de signo, False en caso contrario
    """
    return f(a) * f(b) < 0


def evaluar_funcion_segura(f: Callable[[float], float], x: float) -> float:
    """
    Evalua una funcion de manera segura, manejando errores
    
    Args:
        f: Funcion a evaluar
        x: Punto de evaluacion
    
    Returns:
        Valor de la funcion o float('inf') si hay error
    """
    try:
        resultado = f(x)
        if math.isnan(resultado) or math.isinf(resultado):
            return float('inf')
        return resultado
    except:
        return float('inf')


def crear_funcion_personalizada(expresion: str, variable: str = 'x') -> Callable[[float], float]:
    """
    Crea una funcion a partir de una expresion string
    
    Args:
        expresion: Expresion matematica como string (ej: 'x**2 - 2*x - 3')
        variable: Variable de la funcion (por defecto 'x')
    
    Returns:
        Funcion evaluable
    """
    def funcion(x):
        # Namespace seguro para evaluacion
        namespace = {
            'x': x,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'log': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e,
        }
        return eval(expresion, {"__builtins__": {}}, namespace)
    
    return funcion


# EXPORTACIONES

__all__ = [
    'calcular_error',
    'FuncionesBasicas',
    'FuncionesPuntoFijo',
    'verificar_cambio_signo',
    'evaluar_funcion_segura',
    'crear_funcion_personalizada'
]