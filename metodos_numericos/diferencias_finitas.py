"""
Métodos de Diferencias Finitas para Derivación Numérica
======================================================

Este módulo contiene implementaciones de métodos de diferencias finitas para calcular
derivadas numéricas hasta la cuarta orden usando diferentes esquemas:
- Diferencias hacia adelante
- Diferencias hacia atrás  
- Diferencias centradas

Con dos niveles de precisión (LOW/HIGH) que determinan el número de puntos utilizados.
"""

import numpy as np
from typing import Callable, Tuple, Optional
from enum import Enum

class PrecisionLevel(Enum):
    """Nivel de precision para las formulas de diferencias finitas"""
    LOW = 1    # Menos terminos, menos preciso
    HIGH = 2   # Mas terminos, mas preciso

class DiferenciasFinitas:
    """
    Clase para calcular derivadas numericas usando diferencias finitas
    Incluye formulas hacia adelante, atras y centradas hasta 4ta derivada
    """
    
    def __init__(self, f: Callable, x: np.ndarray, h: float = None):
        """
        Inicializa la clase con la funcion y puntos de evaluacion
        
        Parametros:
        -----------
        f : Callable
            Funcion a derivar
        x : np.ndarray
            Puntos de evaluacion
        h : float
            Paso entre puntos (calculado automaticamente si no se proporciona)
        """
        self.f = f
        self.x = x
        self.n = len(x) - 1
        
        # Calcular h si no se proporciona
        if h is None:
            self.h = x[1] - x[0] if len(x) > 1 else 0.01
        else:
            self.h = h
        
        # Pre-calcular valores de la funcion para eficiencia
        self._precompute_values()
    
    def _precompute_values(self):
        """Pre-calcula valores de la funcion en puntos necesarios"""
        # Extender el dominio para formulas de alta precision
        x_ext = np.arange(self.x[0] - 5*self.h, self.x[-1] + 5*self.h + self.h/2, self.h)
        self.f_values = {xi: self.f(xi) for xi in x_ext}
    
    def _get_f(self, xi: float) -> float:
        """Obtiene el valor de f(xi) del cache o lo calcula"""
        if xi not in self.f_values:
            self.f_values[xi] = self.f(xi)
        return self.f_values[xi]
    
    # ======================== DIFERENCIAS HACIA ADELANTE ========================
    
    def primera_derivada_adelante(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula primera derivada usando diferencias hacia adelante
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 2 puntos, HIGH: formula de 3 puntos
        
        Retorna:
        --------
        np.ndarray : Primera derivada en cada punto
        """
        df = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+h) - f(x)) / h
                df[i] = (self._get_f(xi + self.h) - self._get_f(xi)) / self.h
            else:
                # Formula mejorada: (-f(x+2h) + 4f(x+h) - 3f(x)) / 2h
                if i < self.n - 1:  # Verificar que hay suficientes puntos
                    df[i] = (-self._get_f(xi + 2*self.h) + 4*self._get_f(xi + self.h) - 3*self._get_f(xi)) / (2*self.h)
                else:
                    # Usar formula simple en el ultimo punto
                    df[i] = (self._get_f(xi) - self._get_f(xi - self.h)) / self.h
        
        return df
    
    def segunda_derivada_adelante(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula segunda derivada usando diferencias hacia adelante
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 3 puntos, HIGH: formula de 4 puntos
        
        Retorna:
        --------
        np.ndarray : Segunda derivada en cada punto
        """
        d2f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+2h) - 2f(x+h) + f(x)) / h^2
                d2f[i] = (self._get_f(xi + 2*self.h) - 2*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**2)
            else:
                # Formula mejorada: (-f(x+3h) + 4f(x+2h) - 5f(x+h) + 2f(x)) / h^2
                if i < self.n - 2:
                    d2f[i] = (-self._get_f(xi + 3*self.h) + 4*self._get_f(xi + 2*self.h) - 5*self._get_f(xi + self.h) + 2*self._get_f(xi)) / (self.h**2)
                else:
                    # Usar formula simple cerca del final
                    d2f[i] = (self._get_f(xi) - 2*self._get_f(xi - self.h) + self._get_f(xi - 2*self.h)) / (self.h**2)
        
        return d2f
    
    def tercera_derivada_adelante(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula tercera derivada usando diferencias hacia adelante
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 4 puntos, HIGH: formula de 5 puntos
        
        Retorna:
        --------
        np.ndarray : Tercera derivada en cada punto
        """
        d3f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+3h) - 3f(x+2h) + 3f(x+h) - f(x)) / h^3
                d3f[i] = (self._get_f(xi + 3*self.h) - 3*self._get_f(xi + 2*self.h) + 3*self._get_f(xi + self.h) - self._get_f(xi)) / (self.h**3)
            else:
                # Formula mejorada: (-3f(x+4h) + 14f(x+3h) - 24f(x+2h) + 18f(x+h) - 5f(x)) / 2h^3
                if i < self.n - 3:
                    d3f[i] = (-3*self._get_f(xi + 4*self.h) + 14*self._get_f(xi + 3*self.h) - 24*self._get_f(xi + 2*self.h) + 18*self._get_f(xi + self.h) - 5*self._get_f(xi)) / (2*self.h**3)
                else:
                    # Usar formula simple cerca del final
                    d3f[i] = (self._get_f(xi) - 3*self._get_f(xi - self.h) + 3*self._get_f(xi - 2*self.h) - self._get_f(xi - 3*self.h)) / (self.h**3)
        
        return d3f
    
    def cuarta_derivada_adelante(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula cuarta derivada usando diferencias hacia adelante
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 5 puntos, HIGH: formula de 6 puntos
        
        Retorna:
        --------
        np.ndarray : Cuarta derivada en cada punto
        """
        d4f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+4h) - 4f(x+3h) + 6f(x+2h) - 4f(x+h) + f(x)) / h^4
                d4f[i] = (self._get_f(xi + 4*self.h) - 4*self._get_f(xi + 3*self.h) + 6*self._get_f(xi + 2*self.h) - 4*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**4)
            else:
                # Formula mejorada: (-2f(x+5h) + 11f(x+4h) - 24f(x+3h) + 26f(x+2h) - 14f(x+h) + 3f(x)) / h^4
                if i < self.n - 4:
                    d4f[i] = (-2*self._get_f(xi + 5*self.h) + 11*self._get_f(xi + 4*self.h) - 24*self._get_f(xi + 3*self.h) + 26*self._get_f(xi + 2*self.h) - 14*self._get_f(xi + self.h) + 3*self._get_f(xi)) / (self.h**4)
                else:
                    # Usar formula simple cerca del final
                    d4f[i] = (self._get_f(xi) - 4*self._get_f(xi - self.h) + 6*self._get_f(xi - 2*self.h) - 4*self._get_f(xi - 3*self.h) + self._get_f(xi - 4*self.h)) / (self.h**4)
        
        return d4f
    
    # ======================== DIFERENCIAS HACIA ATRAS ========================
    
    def primera_derivada_atras(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula primera derivada usando diferencias hacia atras
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 2 puntos, HIGH: formula de 3 puntos
        
        Retorna:
        --------
        np.ndarray : Primera derivada en cada punto
        """
        df = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x) - f(x-h)) / h
                df[i] = (self._get_f(xi) - self._get_f(xi - self.h)) / self.h
            else:
                # Formula mejorada: (3f(x) - 4f(x-h) + f(x-2h)) / 2h
                if i > 1:
                    df[i] = (3*self._get_f(xi) - 4*self._get_f(xi - self.h) + self._get_f(xi - 2*self.h)) / (2*self.h)
                else:
                    # Usar formula simple en los primeros puntos
                    df[i] = (self._get_f(xi + self.h) - self._get_f(xi)) / self.h
        
        return df
    
    def segunda_derivada_atras(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula segunda derivada usando diferencias hacia atras
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 3 puntos, HIGH: formula de 4 puntos
        
        Retorna:
        --------
        np.ndarray : Segunda derivada en cada punto
        """
        d2f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x) - 2f(x-h) + f(x-2h)) / h^2
                d2f[i] = (self._get_f(xi) - 2*self._get_f(xi - self.h) + self._get_f(xi - 2*self.h)) / (self.h**2)
            else:
                # Formula mejorada: (2f(x) - 5f(x-h) + 4f(x-2h) - f(x-3h)) / h^2
                if i > 2:
                    d2f[i] = (2*self._get_f(xi) - 5*self._get_f(xi - self.h) + 4*self._get_f(xi - 2*self.h) - self._get_f(xi - 3*self.h)) / (self.h**2)
                else:
                    # Usar formula simple en los primeros puntos
                    d2f[i] = (self._get_f(xi + 2*self.h) - 2*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**2)
        
        return d2f
    
    def tercera_derivada_atras(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula tercera derivada usando diferencias hacia atras
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 4 puntos, HIGH: formula de 5 puntos
        
        Retorna:
        --------
        np.ndarray : Tercera derivada en cada punto
        """
        d3f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x) - 3f(x-h) + 3f(x-2h) - f(x-3h)) / h^3
                d3f[i] = (self._get_f(xi) - 3*self._get_f(xi - self.h) + 3*self._get_f(xi - 2*self.h) - self._get_f(xi - 3*self.h)) / (self.h**3)
            else:
                # Formula mejorada: (5f(x) - 18f(x-h) + 24f(x-2h) - 14f(x-3h) + 3f(x-4h)) / 2h^3
                if i > 3:
                    d3f[i] = (5*self._get_f(xi) - 18*self._get_f(xi - self.h) + 24*self._get_f(xi - 2*self.h) - 14*self._get_f(xi - 3*self.h) + 3*self._get_f(xi - 4*self.h)) / (2*self.h**3)
                else:
                    # Usar formula hacia adelante en los primeros puntos
                    d3f[i] = (self._get_f(xi + 3*self.h) - 3*self._get_f(xi + 2*self.h) + 3*self._get_f(xi + self.h) - self._get_f(xi)) / (self.h**3)
        
        return d3f
    
    def cuarta_derivada_atras(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula cuarta derivada usando diferencias hacia atras
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 5 puntos, HIGH: formula de 6 puntos
        
        Retorna:
        --------
        np.ndarray : Cuarta derivada en cada punto
        """
        d4f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x) - 4f(x-h) + 6f(x-2h) - 4f(x-3h) + f(x-4h)) / h^4
                d4f[i] = (self._get_f(xi) - 4*self._get_f(xi - self.h) + 6*self._get_f(xi - 2*self.h) - 4*self._get_f(xi - 3*self.h) + self._get_f(xi - 4*self.h)) / (self.h**4)
            else:
                # Formula mejorada: (3f(x) - 14f(x-h) + 26f(x-2h) - 24f(x-3h) + 11f(x-4h) - 2f(x-5h)) / h^4
                if i > 4:
                    d4f[i] = (3*self._get_f(xi) - 14*self._get_f(xi - self.h) + 26*self._get_f(xi - 2*self.h) - 24*self._get_f(xi - 3*self.h) + 11*self._get_f(xi - 4*self.h) - 2*self._get_f(xi - 5*self.h)) / (self.h**4)
                else:
                    # Usar formula hacia adelante en los primeros puntos
                    d4f[i] = (self._get_f(xi + 4*self.h) - 4*self._get_f(xi + 3*self.h) + 6*self._get_f(xi + 2*self.h) - 4*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**4)
        
        return d4f
    
    # ======================== DIFERENCIAS CENTRADAS ========================
    
    def primera_derivada_centrada(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula primera derivada usando diferencias centradas
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 2 puntos, HIGH: formula de 4 puntos
        
        Retorna:
        --------
        np.ndarray : Primera derivada en cada punto
        """
        df = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+h) - f(x-h)) / 2h
                if 0 < i < self.n:
                    df[i] = (self._get_f(xi + self.h) - self._get_f(xi - self.h)) / (2*self.h)
                elif i == 0:
                    df[i] = (self._get_f(xi + self.h) - self._get_f(xi)) / self.h
                else:
                    df[i] = (self._get_f(xi) - self._get_f(xi - self.h)) / self.h
            else:
                # Formula mejorada: (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)) / 12h
                if 1 < i < self.n - 1:
                    df[i] = (-self._get_f(xi + 2*self.h) + 8*self._get_f(xi + self.h) - 8*self._get_f(xi - self.h) + self._get_f(xi - 2*self.h)) / (12*self.h)
                else:
                    # Usar formula simple en los extremos
                    if i <= 1:
                        df[i] = (self._get_f(xi + self.h) - self._get_f(xi)) / self.h
                    else:
                        df[i] = (self._get_f(xi) - self._get_f(xi - self.h)) / self.h
        
        return df
    
    def segunda_derivada_centrada(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula segunda derivada usando diferencias centradas
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 3 puntos, HIGH: formula de 5 puntos
        
        Retorna:
        --------
        np.ndarray : Segunda derivada en cada punto
        """
        d2f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+h) - 2f(x) + f(x-h)) / h^2
                if 0 < i < self.n:
                    d2f[i] = (self._get_f(xi + self.h) - 2*self._get_f(xi) + self._get_f(xi - self.h)) / (self.h**2)
                else:
                    # Usar formulas hacia adelante o atras en los extremos
                    if i == 0:
                        d2f[i] = (self._get_f(xi + 2*self.h) - 2*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**2)
                    else:
                        d2f[i] = (self._get_f(xi) - 2*self._get_f(xi - self.h) + self._get_f(xi - 2*self.h)) / (self.h**2)
            else:
                # Formula mejorada: (-f(x+2h) + 16f(x+h) - 30f(x) + 16f(x-h) - f(x-2h)) / 12h^2
                if 1 < i < self.n - 1:
                    d2f[i] = (-self._get_f(xi + 2*self.h) + 16*self._get_f(xi + self.h) - 30*self._get_f(xi) + 16*self._get_f(xi - self.h) - self._get_f(xi - 2*self.h)) / (12*self.h**2)
                else:
                    # Usar formula simple en los extremos
                    if i == 0:
                        d2f[i] = (self._get_f(xi + 2*self.h) - 2*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**2)
                    elif i == self.n:
                        d2f[i] = (self._get_f(xi) - 2*self._get_f(xi - self.h) + self._get_f(xi - 2*self.h)) / (self.h**2)
                    else:
                        d2f[i] = (self._get_f(xi + self.h) - 2*self._get_f(xi) + self._get_f(xi - self.h)) / (self.h**2)
        
        return d2f
    
    def tercera_derivada_centrada(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula tercera derivada usando diferencias centradas
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 4 puntos, HIGH: formula de 6 puntos
        
        Retorna:
        --------
        np.ndarray : Tercera derivada en cada punto
        """
        d3f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+2h) - 2f(x+h) + 2f(x-h) - f(x-2h)) / 2h^3
                if 1 < i < self.n - 1:
                    d3f[i] = (self._get_f(xi + 2*self.h) - 2*self._get_f(xi + self.h) + 2*self._get_f(xi - self.h) - self._get_f(xi - 2*self.h)) / (2*self.h**3)
                else:
                    # Usar formulas hacia adelante o atras en los extremos
                    if i <= 1:
                        d3f[i] = (self._get_f(xi + 3*self.h) - 3*self._get_f(xi + 2*self.h) + 3*self._get_f(xi + self.h) - self._get_f(xi)) / (self.h**3)
                    else:
                        d3f[i] = (self._get_f(xi) - 3*self._get_f(xi - self.h) + 3*self._get_f(xi - 2*self.h) - self._get_f(xi - 3*self.h)) / (self.h**3)
            else:
                # Formula mejorada: (-f(x+3h) + 8f(x+2h) - 13f(x+h) + 13f(x-h) - 8f(x-2h) + f(x-3h)) / 8h^3
                if 2 < i < self.n - 2:
                    d3f[i] = (-self._get_f(xi + 3*self.h) + 8*self._get_f(xi + 2*self.h) - 13*self._get_f(xi + self.h) + 13*self._get_f(xi - self.h) - 8*self._get_f(xi - 2*self.h) + self._get_f(xi - 3*self.h)) / (8*self.h**3)
                else:
                    # Usar formula simple cerca de los extremos
                    if i <= 2:
                        d3f[i] = (self._get_f(xi + 3*self.h) - 3*self._get_f(xi + 2*self.h) + 3*self._get_f(xi + self.h) - self._get_f(xi)) / (self.h**3)
                    else:
                        d3f[i] = (self._get_f(xi) - 3*self._get_f(xi - self.h) + 3*self._get_f(xi - 2*self.h) - self._get_f(xi - 3*self.h)) / (self.h**3)
        
        return d3f
    
    def cuarta_derivada_centrada(self, precision: PrecisionLevel = PrecisionLevel.HIGH) -> np.ndarray:
        """
        Calcula cuarta derivada usando diferencias centradas
        
        Parametros:
        -----------
        precision : PrecisionLevel
            LOW: formula de 5 puntos, HIGH: formula de 7 puntos
        
        Retorna:
        --------
        np.ndarray : Cuarta derivada en cada punto
        """
        d4f = np.zeros_like(self.x)
        
        for i, xi in enumerate(self.x):
            if precision == PrecisionLevel.LOW:
                # Formula simple: (f(x+2h) - 4f(x+h) + 6f(x) - 4f(x-h) + f(x-2h)) / h^4
                if 1 < i < self.n - 1:
                    d4f[i] = (self._get_f(xi + 2*self.h) - 4*self._get_f(xi + self.h) + 6*self._get_f(xi) - 4*self._get_f(xi - self.h) + self._get_f(xi - 2*self.h)) / (self.h**4)
                else:
                    # Usar formulas hacia adelante o atras en los extremos
                    if i <= 1:
                        d4f[i] = (self._get_f(xi + 4*self.h) - 4*self._get_f(xi + 3*self.h) + 6*self._get_f(xi + 2*self.h) - 4*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**4)
                    else:
                        d4f[i] = (self._get_f(xi) - 4*self._get_f(xi - self.h) + 6*self._get_f(xi - 2*self.h) - 4*self._get_f(xi - 3*self.h) + self._get_f(xi - 4*self.h)) / (self.h**4)
            else:
                # Formula mejorada: coeficientes simetricos para derivada par de alta precision
                if 2 < i < self.n - 2:
                    d4f[i] = (-self._get_f(xi - 3*self.h) + 12*self._get_f(xi - 2*self.h) - 39*self._get_f(xi - self.h) + 
                             56*self._get_f(xi) - 39*self._get_f(xi + self.h) + 12*self._get_f(xi + 2*self.h) - 
                             self._get_f(xi + 3*self.h)) / (6*self.h**4)
                else:
                    # Usar formula simple cerca de los extremos
                    if i <= 2:
                        d4f[i] = (self._get_f(xi + 4*self.h) - 4*self._get_f(xi + 3*self.h) + 6*self._get_f(xi + 2*self.h) - 4*self._get_f(xi + self.h) + self._get_f(xi)) / (self.h**4)
                    else:
                        d4f[i] = (self._get_f(xi) - 4*self._get_f(xi - self.h) + 6*self._get_f(xi - 2*self.h) - 4*self._get_f(xi - 3*self.h) + self._get_f(xi - 4*self.h)) / (self.h**4)
        
        return d4f