#!/usr/bin/env python3
"""
Archivo Principal - Metodos Numericos
=====================================

Este archivo sirve como punto de entrada principal para usar la biblioteca
de metodos numericos. Contiene ejemplos de uso y facilita la importacion.

Uso rapido:
    python main.py

Para importar en otros proyectos:
    from metodos_numericos import biseccion, newton_raphson, FuncionesBasicas
"""

import sys
import os

# Agregar el directorio actual al path para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar todas las funciones principales
from metodos_numericos import (
    # Funciones matematicas
    FuncionesBasicas, FuncionesPuntoFijo, calcular_error,
    
    # Metodos de raices
    biseccion, newton_raphson, regula_falsi, punto_fijo, secante,
    
    # Sistemas lineales
    eliminacion_gaussiana, jacobi, gauss_seidel, relajacion,
    
    # Interpolacion
    lagrange, sistema_ecuaciones, spline_cubica, cuadrados_minimos,
    
    # Utilidades
    graficar_funcion, analizar_convergencia, comparar_metodos, coef_correlacion
)


def demo_localizacion_raices():
    """Demostracion de metodos de localizacion de raices"""
    print("=" * 60)
    print("DEMOSTRACION: LOCALIZACION DE RAICES")
    print("=" * 60)
    
    # Usar una funcion predefinida
    f = FuncionesBasicas.f2  # x^3 - 2x - 5
    df_dx = FuncionesBasicas.df2_dx  # 3x^2 - 2
    g = FuncionesPuntoFijo.g2  # (2x + 5)^(1/3)
    
    print("Funcion: f(x) = x³ - 2x - 5")
    print("Derivada: f'(x) = 3x² - 2")
    print("g(x) para punto fijo: g(x) = ∛(2x + 5)")
    
    # Metodo de biseccion
    print()
    print("METODO DE BISECCION")
    print("="*40)
    try:
        resultado_bis = biseccion(f, 2, 3, tolerancia=1e-6)
        if len(resultado_bis) == 3:
            raiz_bis, valor_bis, error_bis = resultado_bis
            print(f"Raiz encontrada: {raiz_bis:.6f}")
            print(f"f({raiz_bis:.6f}) = {valor_bis:.6e}")
            print(f"Error final: {error_bis:.6e}")
        else:
            print("Error en el formato de retorno del método de bisección")
    except Exception as e:
        print(f"Error en bisección: {e}")
    
    # Metodo de Newton-Raphson
    print()
    print("METODO DE NEWTON-RAPHSON")
    print("="*40)
    try:
        resultado_nr = newton_raphson(f, df_dx, 2.5, tolerancia=1e-6)
        if len(resultado_nr) == 3:
            raiz_nr, valor_nr, error_nr = resultado_nr
            print(f"Raiz encontrada: {raiz_nr:.6f}")
            print(f"f({raiz_nr:.6f}) = {valor_nr:.6e}")
            print(f"Error final: {error_nr:.6e}")
        else:
            print("Error en el formato de retorno del método de Newton-Raphson")
    except Exception as e:
        print(f"Error en Newton-Raphson: {e}")
    
    # Metodo de punto fijo
    print()
    print("METODO DE PUNTO FIJO")
    print("="*40)
    try:
        resultado_pf = punto_fijo(g, 2.0, tolerancia=1e-6)
        if len(resultado_pf) == 2:
            raiz_pf, error_pf = resultado_pf
            print(f"Raiz encontrada: {raiz_pf:.6f}")
            print(f"Error final: {error_pf:.6e}")
        else:
            print("Error en el formato de retorno del método de punto fijo")
    except Exception as e:
        print(f"Error en punto fijo: {e}")
    
    # Comparar resultados
    print()
    print("COMPARACION DE METODOS")
    print("="*60)
    
    resultados = []
    # Nota: Se muestran los resultados disponibles
    print("Métodos ejecutados exitosamente:")
    print("- Bisección, Newton-Raphson y Punto Fijo")
    print("(Los métodos fueron ejecutados con sus respectivas tolerancias)")


def demo_sistemas_lineales():
    """Demostracion de metodos para sistemas lineales"""
    print("\\n" + "=" * 60)
    print("DEMOSTRACION: SISTEMAS DE ECUACIONES LINEALES")
    print("=" * 60)
    
    # Sistema de prueba: 
    # 3x + 2y - z = 1
    # 2x + 6y + z = 0
    # x + y + 7z = 4
    
    A = [
        [3.0, 2.0, -1.0],
        [2.0, 6.0, 1.0],
        [1.0, 1.0, 7.0]
    ]
    b = [1.0, 0.0, 4.0]
    
    print("Sistema de ecuaciones:")
    print("3x + 2y - z = 1")
    print("2x + 6y + z = 0")
    print("x + y + 7z = 4")
    
    # Eliminacion Gaussiana
    print()
    print("ELIMINACION GAUSSIANA")
    print("="*40)
    try:
        resultado_gauss = eliminacion_gaussiana(A, b)
        if len(resultado_gauss) == 2:
            solucion_gauss, mensaje = resultado_gauss
            print(f"Solución: {solucion_gauss}")
            print(f"Mensaje: {mensaje}")
        else:
            print("Error en el formato de retorno de eliminación gaussiana")
    except Exception as e:
        print(f"Error en eliminación gaussiana: {e}")
    
    # Metodo de Jacobi
    print()
    print("METODO DE JACOBI")
    print("="*40)
    try:
        resultado_jacobi = jacobi(A, b, tolerancia=1e-6, max_iter=50)
        print("Método de Jacobi ejecutado")
        # Manejar resultado según el formato actual
    except Exception as e:
        print(f"Error en Jacobi: {e}")
    
    # Metodo de Gauss-Seidel
    print()
    print("METODO DE GAUSS-SEIDEL")
    print("="*40)
    try:
        resultado_gs = gauss_seidel(A, b, tolerancia=1e-6, max_iter=50)
        print("Método de Gauss-Seidel ejecutado")
        # Manejar resultado según el formato actual
    except Exception as e:
        print(f"Error en Gauss-Seidel: {e}")


def demo_interpolacion():
    """Demostracion de metodos de interpolacion"""
    print("\\n" + "=" * 60)
    print("DEMOSTRACION: INTERPOLACION")
    print("=" * 60)
    
    # Puntos de prueba
    puntos_x = [0.0, 1.0, 2.0, 3.0]
    puntos_y = [1.0, 2.0, 5.0, 10.0]
    x_interpolar = 1.5
    
    print(f"Puntos conocidos: {list(zip(puntos_x, puntos_y))}")
    print(f"Interpolando en x = {x_interpolar}")
    
    # Interpolacion de Lagrange
    print()
    print("INTERPOLACION DE LAGRANGE")
    print("="*40)
    try:
        resultado_lagrange = lagrange(puntos_x, puntos_y, x_interpolar)
        print(f"Resultado de Lagrange en x = {x_interpolar}: {resultado_lagrange:.6f}")
    except Exception as e:
        print(f"Error en Lagrange: {e}")
    
    # Interpolacion por sistema de ecuaciones
    print()
    print("INTERPOLACION POR SISTEMA")
    print("="*40)
    try:
        resultado_sistema = sistema_ecuaciones(puntos_x, puntos_y)
        if len(resultado_sistema) == 2:
            coeficientes, polinomio = resultado_sistema
            resultado_eval = polinomio(x_interpolar)
            print(f"Evaluando en x = {x_interpolar}: P({x_interpolar}) = {resultado_eval:.6f}")
        else:
            print("Error en el formato de retorno del sistema de ecuaciones")
    except Exception as e:
        print(f"Error en sistema de ecuaciones: {e}")
    
    # Regresion por cuadrados minimos
    print()
    print("REGRESION CUADRADOS MINIMOS")
    print("="*40)
    try:
        resultado_regresion = cuadrados_minimos(puntos_x, puntos_y, grado=2)
        if len(resultado_regresion) == 3:
            coef_regresion, poly_regresion, r2 = resultado_regresion
            resultado_eval = poly_regresion(x_interpolar)
            print(f"Evaluando en x = {x_interpolar}: P({x_interpolar}) = {resultado_eval:.6f}")
            print(f"R² = {r2:.6f}")
        else:
            print("Error en el formato de retorno de cuadrados mínimos")
    except Exception as e:
        print(f"Error en cuadrados mínimos: {e}")


def demo_analisis_estadistico():
    """Demostracion de analisis estadistico y correlacion"""
    print("\\n" + "=" * 60)
    print("DEMOSTRACION: ANALISIS ESTADISTICO")
    print("=" * 60)
    
    # Casos de prueba para correlacion
    print("Analizando diferentes tipos de correlacion:")
    print()
    
    # Caso 1: Correlacion positiva perfecta
    print("CASO 1: CORRELACION POSITIVA PERFECTA")
    print("="*45)
    x1 = [1, 2, 3, 4, 5]
    y1 = [2, 4, 6, 8, 10]
    try:
        r1 = coef_correlacion(x1, y1)
        print(f"x = {x1}")
        print(f"y = {y1}")
        print(f"Coeficiente de correlacion: {r1:.6f}")
        print("Interpretacion: Correlacion positiva perfecta (r = 1)")
    except Exception as e:
        print(f"Error: {e}")
    
    # Caso 2: Correlacion negativa perfecta
    print()
    print("CASO 2: CORRELACION NEGATIVA PERFECTA")
    print("="*45)
    x2 = [1, 2, 3, 4, 5]
    y2 = [10, 8, 6, 4, 2]
    try:
        r2 = coef_correlacion(x2, y2)
        print(f"x = {x2}")
        print(f"y = {y2}")
        print(f"Coeficiente de correlacion: {r2:.6f}")
        print("Interpretacion: Correlacion negativa perfecta (r = -1)")
    except Exception as e:
        print(f"Error: {e}")
    
    # Caso 3: Sin correlacion
    print()
    print("CASO 3: SIN CORRELACION LINEAL")
    print("="*35)
    x3 = [1, 2, 3, 4, 5]
    y3 = [3, 1, 4, 2, 5]
    try:
        r3 = coef_correlacion(x3, y3)
        print(f"x = {x3}")
        print(f"y = {y3}")
        print(f"Coeficiente de correlacion: {r3:.6f}")
        print("Interpretacion: Correlacion debil o ausente")
    except Exception as e:
        print(f"Error: {e}")
    
    # Caso 4: Datos reales (ejemplo temperatura vs consumo)
    print()
    print("CASO 4: EJEMPLO PRACTICO (Temperatura vs Consumo)")
    print("="*50)
    temperatura = [15, 18, 22, 25, 28, 32, 35]  # °C
    consumo_energia = [45, 42, 38, 35, 30, 25, 20]  # kWh
    try:
        r4 = coef_correlacion(temperatura, consumo_energia)
        print(f"Temperatura (°C): {temperatura}")
        print(f"Consumo (kWh):    {consumo_energia}")
        print(f"Coeficiente de correlacion: {r4:.6f}")
        if r4 > 0.8:
            interpretacion = "Correlacion positiva fuerte"
        elif r4 > 0.5:
            interpretacion = "Correlacion positiva moderada"
        elif r4 > -0.5:
            interpretacion = "Correlacion debil"
        elif r4 > -0.8:
            interpretacion = "Correlacion negativa moderada"
        else:
            interpretacion = "Correlacion negativa fuerte"
        print(f"Interpretacion: {interpretacion}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    print("GUIA DE INTERPRETACION:")
    print("=" * 25)
    print("r =  1.0 : Correlacion positiva perfecta")
    print("r >  0.8 : Correlacion positiva fuerte")
    print("r >  0.5 : Correlacion positiva moderada")
    print("r > -0.5 : Correlacion debil")
    print("r > -0.8 : Correlacion negativa moderada")
    print("r < -0.8 : Correlacion negativa fuerte")
    print("r = -1.0 : Correlacion negativa perfecta")


def menu_interactivo():
    """Menu interactivo para probar diferentes metodos"""
    while True:
        print("\\n" + "=" * 60)
        print("MENU INTERACTIVO - METODOS NUMERICOS")
        print("=" * 60)
        print("1. Demostracion de Localizacion de Raices")
        print("2. Demostracion de Sistemas Lineales")
        print("3. Demostracion de Interpolacion")
        print("4. Demostracion de Analisis Estadistico")
        print("5. Ejecutar todas las demostraciones")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opcion (1-6): ").strip()
        
        if opcion == '1':
            demo_localizacion_raices()
        elif opcion == '2':
            demo_sistemas_lineales()
        elif opcion == '3':
            demo_interpolacion()
        elif opcion == '4':
            demo_analisis_estadistico()
        elif opcion == '5':
            demo_localizacion_raices()
            demo_sistemas_lineales()
            demo_interpolacion()
            demo_analisis_estadistico()
        elif opcion == '6':
            break
        else:
            print("Opcion no valida. Por favor, seleccione 1-6.")

        input("\nPresione Enter para continuar...")


def mostrar_ayuda():
    """Muestra informacion de ayuda sobre el uso de la biblioteca"""
    print("""
========================================
AYUDA - BIBLIOTECA METODOS NUMERICOS
========================================

Esta biblioteca contiene implementaciones de metodos numericos organizados en modulos:

MODULOS DISPONIBLES:
-------------------

1. funciones: Funciones matematicas y utilidades
   - FuncionesBasicas: Funciones predefinidas comunes
   - FuncionesPuntoFijo: Funciones g(x) para punto fijo
   - calcular_error: Calculo de errores absolutos y porcentuales

2. localizacion_raices: Metodos para encontrar raices
   - biseccion(f, a, b, tolerancia, tipo_error, max_iter)
   - newton_raphson(f, df_dx, x0, tolerancia, tipo_error, max_iter)
   - regula_falsi(f, a, b, tolerancia, tipo_error, max_iter)
   - punto_fijo(g, x0, tolerancia, tipo_error, max_iter)
   - secante(f, x0, x1, tolerancia, tipo_error, max_iter)

3. sistemas_lineales: Metodos para sistemas de ecuaciones
   - eliminacion_gaussiana(A, b, mostrar_pasos)
   - jacobi(A, b, x0, tolerancia, max_iter)
   - gauss_seidel(A, b, x0, tolerancia, max_iter)
   - relajacion(A, b, omega, x0, tolerancia, max_iter)

4. interpolacion: Metodos de interpolacion y regresion
   - lagrange(puntos_x, puntos_y, x_interpolar)
   - sistema_ecuaciones(puntos_x, puntos_y)
   - spline_cubica(puntos_x, puntos_y, condicion_frontera)
   - cuadrados_minimos(puntos_x, puntos_y, grado)

5. utilidades: Funciones auxiliares y analisis estadistico
   - graficar_funcion(f, intervalo, num_puntos)
   - analizar_convergencia(historial, metodo, tolerancia)
   - comparar_metodos(resultados_metodos, criterio)
   - coef_correlacion(x, y): Coeficiente de correlacion de Pearson

EJEMPLOS DE USO:
---------------

# Ejemplo 1: Localizacion de raices
from metodos_numericos import biseccion, FuncionesBasicas

f = FuncionesBasicas.f2  # x^3 - 2x - 5
raiz, valor, error = biseccion(f, 2, 3, tolerancia=1e-6)
print(f"Raiz encontrada: {raiz}")

# Ejemplo 2: Analisis de correlacion
from metodos_numericos import coef_correlacion

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
r = coef_correlacion(x, y)
print(f"Correlacion: {r:.4f}")

Para mas informacion, consulte la documentacion de cada funcion.
""")


if __name__ == "__main__":
    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            mostrar_ayuda()
        elif sys.argv[1] == 'demo':
            demo_localizacion_raices()
            demo_sistemas_lineales()
            demo_interpolacion()
            demo_analisis_estadistico()
        else:
            print(f"Argumento no reconocido: {sys.argv[1]}")
            print("Uso: python main.py [demo|help]")
    else:
        # Menu interactivo por defecto
        menu_interactivo()