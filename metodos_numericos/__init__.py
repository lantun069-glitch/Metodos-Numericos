"""
Biblioteca de Metodos Numericos
===============================

Este paquete contiene implementaciones de diversos metodos numericos para:
- Localizacion de raices
- Sistemas de ecuaciones lineales
- Interpolacion y regresion
- Metodos iterativos
- Analysis estadistico y correlacion

Modulos disponibles:
- funciones: Definicion de funciones matematicas comunes
- localizacion_raices: Metodos para encontrar raices de ecuaciones
- sistemas_lineales: Metodos para resolver sistemas de ecuaciones
- interpolacion: Metodos de interpolacion y regresion
- utilidades: Funciones auxiliares, graficacion y analisis estadistico
"""

# Imports para facilitar el uso
from .funciones import (
    calcular_error, FuncionesBasicas, FuncionesPuntoFijo,
    verificar_cambio_signo, evaluar_funcion_segura, crear_funcion_personalizada
)
from .localizacion_raices import (
    biseccion, newton_raphson, regula_falsi, punto_fijo, secante
)
from .sistemas_lineales import (
    eliminacion_gaussiana, jacobi, gauss_seidel, relajacion
)
from .interpolacion import (
    lagrange, sistema_ecuaciones, spline_cubica, cuadrados_minimos
)
from .utilidades import (
    graficar_funcion, analizar_convergencia, comparar_metodos,
    formatear_matriz, formatear_vector, coef_correlacion
)

__version__ = "1.0.0"
__author__ = "Lucas Santiago Said Antun"