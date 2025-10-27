"""
Biblioteca de Metodos Numericos
===============================

Este paquete contiene implementaciones de diversos metodos numericos para:
- Localizacion de raices
- Sistemas de ecuaciones lineales
- Interpolacion y regresion
- Integracion numerica
- Diferenciacion numerica (diferencias finitas)
- Ecuaciones diferenciales ordinarias (EDOs)
- Metodos iterativos
- Analisis estadistico y correlacion

Modulos disponibles:
- funciones: Definicion de funciones matematicas comunes
- localizacion_raices: Metodos para encontrar raices de ecuaciones
- sistemas_lineales: Metodos para resolver sistemas de ecuaciones
- interpolacion: Metodos de interpolacion y regresion
- integracion: Metodos de integracion numerica
- diferencias_finitas: Metodos de diferenciacion numerica
- ecuaciones_diferenciales: Metodos para resolver EDOs
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
from .integracion import (
    trapecio_simple, trapecio_compuesto, trapecio_compuesto_v2, trapecio_compuesto_datos,
    simpson_1_3_simple, simpson_1_3_compuesto,
    simpson_compuesta_funcion, simpson_compuesta_datos, simpson_compuesta_mejorada,
    gauss_legendre_integration,
    calcular_error_trapecio, calcular_error_simpson
)
from .diferencias_finitas import (
    DiferenciasFinitas, PrecisionLevel
)
from .ecuaciones_diferenciales import (
    metodo_euler, metodo_heun, metodo_punto_medio, metodo_rk4, euler_sistema,
    calcular_error_convergencia, calcular_factor_convergencia_Q
)
from .utilidades import (
    graficar_funcion, analizar_convergencia, comparar_metodos,
    formatear_matriz, formatear_vector, coef_correlacion
)

__version__ = "1.0.0"
__author__ = "Lucas Santiago Said Antun"